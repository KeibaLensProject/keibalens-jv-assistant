"""context/sample1_VC2019 (C++ MFC サンプル) -> references/spec/sample-vc2019/ (Markdown)。

JV-Link の呼び出しフロー(JVInit→JVOpen→JVStatus→JVRead→JVClose 等)を示す
JRA-VAN 公式サンプル。C# 実装時の処理順序の参考にする。ソース(.cpp/.h)と
ReadMe/リソースをコードブロックで Markdown 化し、JV-Link メソッドの使用箇所を
README に相互参照としてまとめる。バイナリ/VS プロジェクトファイルは対象外。
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "plugins", "jra-van-spec-skills", "skills",
                    "jra-van-spec-skills", "references", "spec")
SRC = os.path.join(ROOT, "context", "sample1_VC2019")
OUT = os.path.join(SPEC, "sample-vc2019")

CONVERT_EXT = {".cpp": "cpp", ".h": "cpp", ".txt": "text",
               ".rc": "text", ".htm": "html", ".html": "html"}
SKIP_EXT = {".ncb", ".ico", ".dsp", ".dsw", ".sln", ".vcxproj",
            ".filters", ".manifest", ".rc2", ".aps", ".user"}

# JV-Link メソッド(インターフェース仕様書 2.メソッド)
JV_METHODS = [
    "JVInit", "JVSetUIProperties", "JVSetServiceKey", "JVSetSaveFlag",
    "JVSetSavePath", "JVOpen", "JVRTOpen", "JVStatus", "JVRead", "JVGets",
    "JVSkip", "JVCancel", "JVClose", "JVFiledelete", "JVFukuFile", "JVFuku",
    "JVMVCheck", "JVMVCheckWithType", "JVMVPlay", "JVMVPlayWithType",
    "JVMVOpen", "JVMVRead", "JVCourseFile", "JVCourseFile2",
    "JVWatchEvent", "JVWatchEventClose",
]
METHOD_RE = re.compile(r"\b(" + "|".join(JV_METHODS) + r")\b")

ROLES = {
    "ReadMe.txt": "プロジェクト構成の概要(AppWizard 生成)",
    "sample1.cpp": "アプリケーションクラス CSample1App(エントリポイント)",
    "sample1.h": "アプリケーションの中心インクルード",
    "sample1Dlg1.cpp": "設定ダイアログ。JVInit / JVSetUIProperties を呼ぶ",
    "sample1Dlg1.h": "設定ダイアログのヘッダ",
    "sample1Dlg2.cpp": "データ取得ダイアログ。JVOpen→JVStatus→JVRead→JVClose の中核",
    "sample1Dlg2.h": "データ取得ダイアログのヘッダ",
    "sample1Del.cpp": "ファイル削除処理。JVFiledelete を呼ぶ",
    "sample1Del.h": "ファイル削除処理のヘッダ",
    "dlgDel.cpp": "削除確認ダイアログ",
    "dlgDel.h": "削除確認ダイアログのヘッダ",
    "jvlink.cpp": "JV-Link COM ラッパ実装(#import 生成)",
    "jvlink.h": "JV-Link COM ラッパ宣言(IJVLink インターフェース)",
    "stdafx.cpp": "プリコンパイル済みヘッダ",
    "stdafx.h": "共通インクルード",
    "resource.h": "リソース ID 定義",
    "sample1.rc": "リソーススクリプト(ダイアログ/メニュー定義)",
}


def read_text(path):
    b = open(path, "rb").read()
    for e in ("utf-8-sig", "utf-8", "cp932"):
        try:
            return b.decode(e)
        except UnicodeDecodeError:
            continue
    return b.decode("cp932", errors="replace")


def flat_name(rel):
    return rel.replace(os.sep, "_").replace(".", "-") + ".md"


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        import shutil
        shutil.rmtree(OUT)

    converted = []     # (rel, mdname, lang, role)
    skipped = []       # rel
    usage = {m: [] for m in JV_METHODS}

    for root, _, files in os.walk(SRC):
        for fn in sorted(files):
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, SRC)
            ext = os.path.splitext(fn)[1].lower()
            if ext in SKIP_EXT:
                skipped.append(rel)
                continue
            lang = CONVERT_EXT.get(ext)
            if lang is None:
                skipped.append(rel)
                continue
            text = read_text(full)
            mdname = flat_name(rel)
            role = ROLES.get(rel.replace(os.sep, "\\").split("\\")[-1], "")
            fence = "~~~" if "```" in text else "```"
            body = (f"# {rel}\n\n"
                    f"出典: `context/sample1_VC2019/{rel.replace(os.sep, '/')}`\n\n"
                    + (f"{role}\n\n" if role else "")
                    + f"{fence}{lang}\n{text}\n{fence}\n")
            write(os.path.join(OUT, mdname), body)
            converted.append((rel, mdname, lang, role))
            if ext in (".cpp", ".h"):
                for i, line in enumerate(text.splitlines(), 1):
                    for m in METHOD_RE.findall(line):
                        usage[m].append((rel, i))

    # README
    md = ["# JRA-VAN サンプルプログラム sample1 (C++ / MFC, VC2019)",
          "",
          "出典: `context/sample1_VC2019/`",
          "",
          "JRA-VAN 公式の C++ (MFC) サンプルです。**JV-Link の呼び出しフロー**"
          "(初期化→取得要求→進捗→読み込み→終了)を示しており、C# 実装時の"
          "処理順序・エラーハンドリングの参考になります。",
          "",
          "## JV-Link 呼び出しフロー(蓄積系)",
          "",
          "```",
          "JVInit                  設定ダイアログ初期化時 (sample1Dlg1.cpp)",
          "JVSetUIProperties       設定変更         (sample1Dlg1.cpp)",
          "JVOpen                  データ取得要求    (sample1Dlg2.cpp)",
          "  JVStatus              ダウンロード進捗  (sample1Dlg2.cpp)",
          "  JVRead / JVGets       レコード読み込み  (sample1Dlg2.cpp)",
          "  JVSkip                読みとばし",
          "JVClose                 取り込み終了      (sample1Dlg2.cpp)",
          "```",
          "",
          "## ファイル一覧",
          "",
          "| ファイル | 役割 | 変換 |",
          "|---|---|---|"]
    for rel, mdname, lang, role in converted:
        md.append(f"| `{rel}` | {role} | [{mdname}](./{mdname}) |")
    md.append("")
    md.append("## JV-Link メソッド使用箇所")
    md.append("")
    md.append("| メソッド | 使用箇所(ファイル:行) |")
    md.append("|---|---|")
    for m in JV_METHODS:
        locs = usage[m]
        if not locs:
            continue
        cell = ", ".join(f"`{r}:{ln}`" for r, ln in locs[:8])
        if len(locs) > 8:
            cell += f" ほか{len(locs) - 8}件"
        md.append(f"| {m} | {cell} |")
    if skipped:
        md.append("")
        md.append("## 変換対象外(バイナリ/プロジェクト/ビルド設定)")
        md.append("")
        md.append(", ".join(f"`{s}`" for s in sorted(skipped)))
    md.append("")
    write(os.path.join(OUT, "README.md"), "\n".join(md))

    print(f"converted: {len(converted)} files, skipped: {len(skipped)}")
    used = {m: len(v) for m, v in usage.items() if v}
    print("JV methods used:", used)
    print("done")


if __name__ == "__main__":
    main()
