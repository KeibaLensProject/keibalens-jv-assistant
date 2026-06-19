"""JVData_Struct.cs -> references/spec/jvdata-struct/ (領域ごとに分割)

C# の JV-Data 構造体定義 (JRA-VAN 提供サンプル, 最終更新 2009-12-08)。
#region 単位で分割し、C# ソースを忠実にコードブロックとして残す。
使い方: python tools/convert_struct_cs.py
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "plugins", "jra-van-spec-skills", "skills",
                    "jra-van-spec-skills", "references", "spec")
SRC = os.path.join(ROOT, "context", "JVData_Struct.cs")
OUT = os.path.join(SPEC, "jvdata-struct")
NOTE = "出典: `context/JVData_Struct.cs` (JRA-VAN提供サンプル, 最終更新 2009-12-08)"


def safe(s):
    s = re.sub(r'[<>:"/\\|?*]', "", s)
    return s.replace("（", "(").replace("）", ")").strip().strip(".")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("  wrote", os.path.relpath(path, ROOT))


def structs_in(body):
    """領域内の struct 名と直前の <summary> を抽出。"""
    out = []
    for i, l in enumerate(body):
        m = re.match(r"\s*public\s+struct\s+(\w+)", l)
        if m:
            summary = ""
            for j in range(i - 1, max(i - 8, -1), -1):
                t = body[j].strip()
                sm = re.search(r"<summary>\s*(.*?)\s*</summary>", t)
                if "<summary>" in t and "</summary>" not in t:
                    for k in range(j + 1, i):
                        ct = body[k].strip().lstrip("/").strip()
                        if ct and "</summary>" not in ct:
                            summary = ct
                            break
                    break
                if sm:
                    summary = sm.group(1)
                    break
            out.append((m.group(1), summary))
    return out


def code_block(body):
    text = "\n".join(body).strip("\n")
    return "```csharp\n" + text + "\n```"


def main():
    lines = open(SRC, encoding="utf-8-sig").read().splitlines()

    # #region を入れ子対応でパース
    stack = []
    regions = []  # (title, depth, start, end, parent_title)
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("#region"):
            title = s[len("#region"):].strip()
            stack.append({"title": title, "start": i, "depth": len(stack),
                          "parent": stack[-1]["title"] if stack else None})
        elif s.startswith("#endregion"):
            if stack:
                r = stack.pop()
                r["end"] = i
                regions.append(r)

    by_title = {r["title"]: r for r in regions}
    helper = by_title.get("セットデータのプログラミングパーツ")
    common = by_title.get("共通構造体")
    data = by_title.get("データ構造体")
    records = [r for r in regions if r["parent"] == "データ構造体"]
    records.sort(key=lambda r: r["start"])

    # 共通構造体ファイル
    if common:
        body = lines[common["start"] + 1: common["end"]]
        sts = structs_in(body)
        out = ["# 共通構造体", "", NOTE, "",
               "複数レコードで共有される構造体 (年月日・時分秒・着差など)。", ""]
        if sts:
            out += ["定義: " + ", ".join(f"`{n}`" for n, _ in sts), ""]
        out += [code_block(body), ""]
        write(os.path.join(OUT, "common-structs.md"), "\n".join(out))

    # レコード領域ファイル
    index = []
    for idx, r in enumerate(records, 1):
        title = r["title"]
        m = re.match(r"^([\d.\-]+)\.(.*)$", title)
        num = m.group(1) if m else str(idx)
        name = m.group(2) if m else title
        body = lines[r["start"] + 1: r["end"]]
        sts = structs_in(body)
        fname = f"{idx:02d}-{safe(name)}.md"
        out = [f"# {title}", "", NOTE, ""]
        if sts:
            out.append("| 構造体 | 概要 |")
            out.append("|---|---|")
            for n, sm in sts:
                out.append(f"| `{n}` | {sm} |")
            out.append("")
        out += [code_block(body), ""]
        write(os.path.join(OUT, fname), "\n".join(out))
        index.append((num, name, fname, [n for n, _ in sts]))

    # README (ヘルパ + 索引)
    out = [
        "# JV-Data C# 構造体定義", "", NOTE, "",
        "JRA-VAN が提供する C# 版 JV-Data 構造体サンプルを領域ごとに Markdown 化したものです。",
        "C# プロジェクトでの JV-Data パース実装の参照に利用できます。", "",
        "> 注: このサンプルは **2009年版** のため、最新の JV-Data仕様書(4.9.0.1)で追加された"
        "レコード・項目は含まれません。フィールドの正確な位置/バイト数は "
        "[レコードフォーマット](../jv-data-spec/record-formats/README.md) を正とします。", "",
        "## バイト切り出しヘルパ", "",
        "Shift_JIS バイト列から項目を切り出す共通メソッドです。", "",
    ]
    if helper:
        out += [code_block(lines[helper["start"] + 1: helper["end"]]), ""]
    out += ["## 構造体ファイル一覧", "",
            "- [共通構造体](./common-structs.md)", "",
            "| No | レコード | ファイル | 主な構造体 |", "|---|---|---|---|"]
    for num, name, fname, sts in index:
        s = ", ".join(f"`{x}`" for x in sts[:4]) + ("…" if len(sts) > 4 else "")
        out.append(f"| {num} | {name} | [{fname}](./{fname}) | {s} |")
    out.append("")
    write(os.path.join(OUT, "README.md"), "\n".join(out))
    print(f"done: {len(records)} record regions")


if __name__ == "__main__":
    main()
