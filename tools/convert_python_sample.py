"""context/sample1_Python3.14 (Python サンプル) -> references/spec/sample-python/ (Markdown)。

SDK Ver.5.0.0 (64bit版) で追加された Python 3.14 (Tkinter + pywin32) サンプルプログラム。
JV-Link COM オブジェクト生成(win32com.client.Dispatch("JVDTLab.JVLink"))、
JVInit → JVOpen → JVStatus → JVGets(memview.tobytes().decode("cp932")) → JVClose の
一連の呼び出しフローを Markdown 化する。

使い方: python tools/convert_python_sample.py
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "plugins", "jra-van-spec-skills", "skills",
                    "jra-van-spec-skills", "references", "spec")
SRC = os.path.join(ROOT, "context", "sample1_Python3.14")
OUT = os.path.join(SPEC, "sample-python")

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
    "Form1.py": "メイン画面。win32com.client.Dispatch(\"JVDTLab.JVLink\") 生成・JVInit・JVSetUIProperties・JVFiledelete を呼ぶ",
    "Form2.py": "データ取込みダイアログ。別スレッドで JVOpen → JVStatus → JVGets (cp932 デコード) / JVRead → JVCancel / JVClose を呼ぶ",
}


def read_text(path):
    b = open(path, "rb").read()
    for e in ("utf-8-sig", "utf-8", "cp932"):
        try:
            return b.decode(e)
        except UnicodeDecodeError:
            continue
    return b.decode("cp932", errors="replace")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        import shutil
        shutil.rmtree(OUT)

    converted = []
    usage = {m: [] for m in JV_METHODS}

    for fn in sorted(os.listdir(SRC)):
        full = os.path.join(SRC, fn)
        if not os.path.isfile(full) or not fn.endswith(".py"):
            continue
        text = read_text(full)
        mdname = fn.replace(".", "-") + ".md"
        role = ROLES.get(fn, "")
        fence = "~~~" if "```" in text else "```"
        body = (f"# {fn}\n\n"
                f"出典: `context/sample1_Python3.14/{fn}` (SDK Ver.5.0.0 64bit版同梱)\n\n"
                + (f"{role}\n\n" if role else "")
                + f"{fence}python\n{text}\n{fence}\n")
        write(os.path.join(OUT, mdname), body)
        converted.append((fn, mdname, role))
        for i, line in enumerate(text.splitlines(), 1):
            for m in METHOD_RE.findall(line):
                usage[m].append((fn, i))

    md = [
        "# JRA-VAN サンプルプログラム sample1 (Python 3.14 / pywin32)",
        "",
        "出典: `context/sample1_Python3.14/` (SDK Ver.5.0.0 64bit版同梱)",
        "",
        "SDK Ver.5.0.0 (64bit版) で追加された JRA-VAN 公式の Python (`tkinter` + `pywin32`) サンプルです。",
        "64bit Python から 64bit 版 JV-Link (`JVDTLab.JVLink`) を呼び出す際の **COM 生成・タプル戻り値の受け取り・"
        "`JVGets` による `memoryview` 取得と `cp932` デコード** の公式実装例になります。",
        "",
        "## JV-Link 呼び出しフロー (Python / 蓄積系)",
        "",
        "```",
        "win32com.client.Dispatch(\"JVDTLab.JVLink\")  COM オブジェクト生成 (Form1.py)",
        "JVInit(\"UNKNOWN\")                           初期化 (Form1.py)",
        "JVSetUIProperties()                         JV-Link 設定画面表示 (Form1.py)",
        "JVOpen(dataspec, fromdate, option, 0, 0, \"\") 取得要求 → (rc, read_count, download_count, lastfiletime) (Form2.py)",
        "  JVStatus()                                ダウンロード進捗ポーリング (Form2.py)",
        "  JVGets(buff, buffsize, buffname)          1レコード読込 → (ret, memview, fname), memview.tobytes().decode(\"cp932\") (Form2.py)",
        "  JVCancel()                                ダウンロード/読込中止 (Form2.py)",
        "JVClose()                                   取り込み終了 (Form2.py)",
        "JVFiledelete(filename)                      ダウンロードファイル削除 (Form1.py)",
        "```",
        "",
        "## ファイル一覧",
        "",
        "| ファイル | 役割 | 変換 |",
        "|---|---|---|",
    ]
    for fn, mdname, role in converted:
        md.append(f"| `{fn}` | {role} | [{mdname}](./{mdname}) |")
    md.append("")
    md.append("## JV-Link メソッド使用箇所")
    md.append("")
    md.append("| メソッド | 使用箇所(ファイル:行) |")
    md.append("|---|---|")
    for m in JV_METHODS:
        locs = usage[m]
        if not locs:
            continue
        cell = ", ".join(f"`{r}:{ln}`" for r, ln in locs)
        md.append(f"| {m} | {cell} |")
    md.append("")
    write(os.path.join(OUT, "README.md"), "\n".join(md))

    print(f"converted: {len(converted)} files")
    print("done")


if __name__ == "__main__":
    main()
