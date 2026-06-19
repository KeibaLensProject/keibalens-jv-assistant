"""蓄積系提供データ一覧.xls -> references/spec/accumulated-data-list.md

データ種別 / レコード種別 / 区分ID / 保存ID / ファイル名 の対応表。
使い方: python tools/convert_datalist_xls.py
"""
import io
import os
import sys
import xlrd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "plugins", "jra-van-spec-skills", "skills",
                    "jra-van-spec-skills", "references", "spec")
SRC = os.path.join(ROOT, "context", "蓄積系提供データ一覧.xls")
OUT = os.path.join(SPEC, "accumulated-data-list.md")
FFILL = 4  # データ種別/データ種別ID/レコード種別/種別ID を前方補完


def c(s):
    s = str(s).replace("\r\n", "\n").replace("\r", "\n")
    return s.replace("|", "\\|").replace("\n", "<br>").strip()


def main():
    book = xlrd.open_workbook(SRC)
    sh = book.sheet_by_index(0)
    rows = []
    for r in range(sh.nrows):
        vals = []
        for col in range(sh.ncols):
            v = sh.cell_value(r, col)
            if isinstance(v, float) and v == int(v):
                v = int(v)
            vals.append(str(v).strip())
        rows.append(vals)

    # 先頭の空行を除去、最初の非空行をヘッダとする
    rows = [r for r in rows if any(r)]
    header = [h.replace("\n", "") for h in rows[0]]
    data = rows[1:]

    last = [""] * sh.ncols
    filled = []
    for row in data:
        row = row[:]
        for i in range(min(FFILL, len(row))):
            if row[i] == "":
                row[i] = last[i]
            else:
                last[i] = row[i]
        filled.append(row)

    out = [
        "# 蓄積系提供データ一覧", "",
        "出典: `context/蓄積系提供データ一覧.xls`", "",
        "蓄積系データの データ種別 / レコード種別 / 区分ID / 保存ID と "
        "ファイル名パターンの対応表です。",
        "ファイル名は `<レコード種別ID><区分ID><保存ID><作成日時>...<.jvd>` の形式です。",
        "（データ種別ID・レコード種別は結合セルを前方補完しています）", "",
        "| " + " | ".join(header) + " |",
        "|" + "|".join(["---"] * len(header)) + "|",
    ]
    for row in filled:
        row = row + [""] * (len(header) - len(row))
        out.append("| " + " | ".join(c(x) for x in row[: len(header)]) + " |")
    out.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print("wrote", os.path.relpath(OUT, ROOT), f"({len(filled)} rows)")


if __name__ == "__main__":
    main()
