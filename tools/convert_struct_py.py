"""JVData_Struct.py -> references/spec/jvdata-struct-py/ (領域ごとに分割)

Python の JV-Data 構造体定義 (JRA-VAN 提供サンプル, 最終更新 2026-07-31, SDK Ver.5.0.0 64bit版同梱)。
# region 単位で分割し、Python ソース(@dataclass + SetDataB)を忠実にコードブロックとして残す。
2009年版の C# 構造体サンプル(JVData_Struct.cs)と異なり、JV-Data 仕様書 4.9.0.1
(2023年 N付き拡張の繁殖登録番号10桁・生産者コード8桁・生産者名72バイト、2021年 WC 10ハロン等)の
最新バイト位置・サイズに準拠している。

使い方: python tools/convert_struct_py.py
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "plugins", "jra-van-spec-skills", "skills",
                    "jra-van-spec-skills", "references", "spec")
SRC = os.path.join(ROOT, "context", "JVData_Struct.py")
OUT = os.path.join(SPEC, "jvdata-struct-py")
NOTE = "出典: `context/JVData_Struct.py` (JRA-VAN提供サンプル, 最終更新 2026-07-31, SDK Ver.5.0.0)"


def safe(s):
    s = re.sub(r'[<>:"/\\|?*]', "", s)
    return s.replace("（", "(").replace("）", ")").strip().strip(".")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("  wrote", os.path.relpath(path, ROOT))


def classes_in(body, fallback_summary=""):
    """領域内の class 名と直後の docstring を抽出。"""
    out = []
    for i, l in enumerate(body):
        m = re.match(r"\s*class\s+(\w+)", l)
        if m:
            cname = m.group(1)
            summary = ""
            if i + 1 < len(body):
                dm = re.search(r'"""\s*(.*?)\s*"""', body[i + 1])
                if dm:
                    summary = dm.group(1)
            if not summary and cname.startswith("JV_"):
                summary = fallback_summary
            out.append((cname, summary))
    return out


def code_block(body):
    text = "\n".join(body).strip("\n")
    return "```python\n" + text + "\n```"


def main():
    lines = open(SRC, encoding="utf-8-sig").read().splitlines()

    # # region を入れ子対応でパース
    stack = []
    regions = []  # (title, depth, start, end, parent_title)
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("# region"):
            title = s[len("# region"):].strip()
            stack.append({"title": title, "start": i, "depth": len(stack),
                          "parent": stack[-1]["title"] if stack else None})
        elif s.startswith("# endregion"):
            if stack:
                r = stack.pop()
                r["end"] = i
                regions.append(r)

    by_title = {r["title"]: r for r in regions}
    helper = by_title.get("セットデータのプログラミングパーツ")
    common = by_title.get("共通構造体")
    records = [r for r in regions if r["parent"] == "データ構造体"]
    records.sort(key=lambda r: r["start"])

    # 共通構造体ファイル
    if common:
        body = lines[common["start"] + 1: common["end"]]
        cls_list = classes_in(body)
        out = ["# 共通構造体 (Python)", "", NOTE, "",
               "複数レコードで共有される `@dataclass` 構造体 (年月日・時分秒・着差・着回数など)。", ""]
        if cls_list:
            out += ["定義: " + ", ".join(f"`{n}`" for n, _ in cls_list), ""]
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
        cls_list = classes_in(body, fallback_summary=name)
        fname = f"{idx:02d}-{safe(name)}.md"
        out = [f"# {title} (Python)", "", NOTE, ""]
        if cls_list:
            out.append("| クラス (`@dataclass`) | 概要 |")
            out.append("|---|---|")
            for n, sm in cls_list:
                out.append(f"| `{n}` | {sm} |")
            out.append("")
        out += [code_block(body), ""]
        write(os.path.join(OUT, fname), "\n".join(out))
        index.append((num, name, fname, [n for n, _ in cls_list]))

    # README (ヘルパ + 索引)
    out = [
        "# JV-Data Python 構造体定義 (`JVData_Struct.py`)", "", NOTE, "",
        "JRA-VAN Data Lab. SDK Ver.5.0.0 (64bit版) に収録されている Python 版 JV-Data 構造体サンプルを"
        "領域ごとに Markdown 化したものです。",
        "Python (`@dataclass` + `SetDataB(b: bytes)`) での JV-Data パース実装にそのまま利用でき、"
        "**2026年7月31日更新のため最新の JV-Data 仕様書 (4.9.0.1) のバイト位置・サイズに完全準拠**しています。", "",
        "> 💡 C# 版構造体サンプル (`../jvdata-struct/`) は 2009 年版のため、2023 年の N付きデータ種別拡張"
        "（繁殖登録番号 8→10 バイト、生産者コード 6→8 バイト、生産者名 70→72 バイト）や 2021 年の"
        "ウッドチップ調教 10 ハロン拡張が未反映ですが、**本 Python 版はすべて最新仕様 (4.9.0.1) に更新済み**です。"
        "C# で最新オフセットを実装する際の参照コードとしても活用できます。", "",
        "## バイト切り出しヘルパ (`MidB2S` / `MidB2B`)", "",
        "Shift_JIS バイト列 (`bytes`) から 1 始まりの位置とバイト長で項目を切り出す共通関数です。", "",
    ]
    if helper:
        out += [code_block(lines[helper["start"] + 1: helper["end"]]), ""]
    out += ["## 構造体ファイル一覧", "",
            "- [共通構造体](./common-structs.md)", "",
            "| 仕様書No | レコード | ファイル | 主なクラス |", "|---|---|---|---|"]
    for num, name, fname, cls_names in index:
        s = ", ".join(f"`{x}`" for x in cls_names[:4]) + ("…" if len(cls_names) > 4 else "")
        out.append(f"| {num} | {name} | [{fname}](./{fname}) | {s} |")
    out.append("")
    write(os.path.join(OUT, "README.md"), "\n".join(out))
    print(f"done: {len(records)} record regions")


if __name__ == "__main__":
    main()
