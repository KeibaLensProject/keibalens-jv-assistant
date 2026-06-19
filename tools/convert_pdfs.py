"""PDF ガイド類 -> references/spec/ (Markdown)。

対象:
  - JRA-VAN Data Lab.開発ガイド_4.2.2.pdf            -> references/spec/dev-guide.md
  - JRA-VAN Data Lab.開発ガイド(イベント C++).pdf    -> references/spec/dev-guide-event-cpp.md
  - JV-Data仕様書_4.9.0.1.pdf                         -> references/spec/jv-data-spec/source-pdf.md (補助)

開発ガイドは見出しを検出して構造化:
  - size>=13            : 大見出し(H1)
  - 行頭 N.N / N.N.N    : 小見出し(階層は数値の段数)
  - 行頭スペース        : 段落の開始
繰返し行(ヘッダ/フッタ)とページ番号は除去する。

JV-Data 仕様書 PDF は xlsx 由来の references/spec/jv-data-spec/ と同内容(表は xlsx が正)
のため、誘導注記つきのページ別生テキストとして出力する。
"""
import io
import os
import re
import sys
import unicodedata
from collections import Counter

import fitz

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "plugins", "jra-van-spec-skills", "skills",
                    "jra-van-spec-skills", "references", "spec")
CTX = os.path.join(ROOT, "context")
DOCS = SPEC
H1 = 13.0
NUM_HEAD = re.compile(r"^(\d+\.\d+(?:\.\d+)*)\s+(\S.*)$")


def norm(s: str) -> str:
    return unicodedata.normalize("NFKC", s).replace("\u3000", " ")


def page_lines(page):
    blocks = page.get_text("dict")["blocks"]
    rows = []
    for b in blocks:
        if not b.get("lines"):
            continue
        rows.append((round(b["bbox"][1], 1), round(b["bbox"][0], 1), b["lines"]))
    rows.sort(key=lambda r: (r[0], r[1]))
    out = []
    for _, _, lines in rows:
        for ln in lines:
            spans = ln["spans"]
            text = norm("".join(s["text"] for s in spans)).rstrip()
            if not text.strip():
                continue
            size = max((s["size"] for s in spans), default=0.0)
            out.append((size, text))
    return out


def find_repeated(all_lines, npages, ratio=0.4):
    """>= ratio のページに現れる行(ヘッダ/フッタ)を集合で返す。"""
    seen = Counter()
    for plines in all_lines:
        for t in {ln[1].strip() for ln in plines}:
            seen[t] += 1
    thr = max(2, int(npages * ratio))
    return {t for t, c in seen.items() if c >= thr and len(t) > 3}


def md_escape(s):
    return s.replace("|", "\\|")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def is_skip_page(plines):
    """目次/修正履歴/ドットリーダ主体のページを真とする。"""
    texts = [t.strip() for _, t in plines]
    if any(x in ("目次", "修正履歴") for x in texts):
        return True
    if texts:
        leader = sum(1 for x in texts if re.search(r"\.{3,}|…|‥|・{3,}", x))
        if leader >= max(3, 0.3 * len(texts)):
            return True
    return False


def convert_guide(src_name, out_md, title, intro):
    src = os.path.join(CTX, src_name)
    doc = fitz.open(src)
    npages = doc.page_count
    all_lines = [page_lines(doc[i]) for i in range(npages)]
    repeated = find_repeated(all_lines, npages)

    headings = []          # (level, text)
    body = []              # md lines
    para = []

    def flush_para():
        if para:
            body.append("".join(para))
            body.append("")
        para.clear()

    # 表紙/修正履歴/目次(複数ページ)をまとめて除外: 本文は実見出し「はじめに」から
    start = next((i for i in range(npages)
                  if any(t.strip() == "はじめに" and size >= H1
                         for size, t in all_lines[i])), 1)
    for i in range(start, npages):
        if is_skip_page(all_lines[i]):
            continue
        for size, t in all_lines[i]:
            s = t.strip()
            if s in repeated:
                continue
            if re.fullmatch(r"\d{1,3}", s):
                continue
            if size >= H1 and not re.fullmatch(r"[A-Za-z]\d{1,2}", s):
                flush_para()
                headings.append((1, s))
                body.append(f"# {s}")
                body.append("")
            elif NUM_HEAD.match(s):
                flush_para()
                lvl = min(NUM_HEAD.match(s).group(1).count(".") + 1, 4)
                headings.append((lvl, s))
                body.append(f"{'#' * (lvl + 1)} {s}")
                body.append("")
            elif re.match(r"^[A-Z]\.\d+(?:\.\d+)*\s", s):      # A.1 付録小見出し
                flush_para()
                headings.append((3, s))
                body.append(f"#### {s}")
                body.append("")
            elif re.match(r"^[A-Z]\.[^\d\s]", s):              # A.サンプル... 付録見出し
                flush_para()
                headings.append((2, s))
                body.append(f"### {s}")
                body.append("")
            else:
                if t.startswith(" ") and para:
                    flush_para()
                para.append(s)
    flush_para()

    toc = ["## 目次", ""]
    for lvl, s in headings:
        toc.append(f"{'  ' * (lvl - 1)}- {s}")
    toc.append("")

    head = [f"# {title}", "",
            f"出典: `context/{src_name}`", "",
            intro, ""]
    out = "\n".join(head + toc + body)
    out = re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"
    write(os.path.join(DOCS, out_md), out)
    doc.close()
    return npages, len(headings)


def convert_jvdata_pdf():
    src_name = "JV-Data仕様書_4.9.0.1.pdf"
    src = os.path.join(CTX, src_name)
    doc = fitz.open(src)
    npages = doc.page_count
    all_lines = [page_lines(doc[i]) for i in range(npages)]
    repeated = find_repeated(all_lines, npages)

    parts = [
        "# JV-Data 仕様書 (PDF・補助)", "",
        f"出典: `context/{src_name}`", "",
        "> **注記**: この PDF は xlsx 版 `JV-Data仕様書_4.9.0.1.xlsx` と同一内容です。"
        "レコードフォーマット・コード表など**構造化された正本は同フォルダの以下**を参照してください"
        "(本ファイルは検索用のページ別生テキスト抽出です)。", "",
        "- [レコードフォーマット](./record-formats/README.md)",
        "- [コード表](./code-tables/README.md)",
        "- [変更履歴](./change-history.md) / [特記事項](./special-notes.md) / "
        "[データ種別](./data-types.md) / [データ提供タイミング](./data-timing.md)", "",
        "---", "",
    ]
    for i in range(npages):
        lines = [t for size, t in all_lines[i]
                 if t.strip() not in repeated and not re.fullmatch(r"\d{1,3}", t.strip())]
        if not lines:
            continue
        parts.append(f"## p.{i + 1}")
        parts.append("")
        parts.append("```")
        parts.extend(lines)
        parts.append("```")
        parts.append("")
    write(os.path.join(DOCS, "jv-data-spec", "source-pdf.md"), "\n".join(parts))
    doc.close()
    return npages


def main():
    n1, h1 = convert_guide(
        "JRA-VAN Data Lab.開発ガイド_4.2.2.pdf", "dev-guide.md",
        "JRA-VAN Data Lab. SDK 開発ガイド",
        "JV-Link を使った競馬ソフト開発の手引きです。開発環境・SDK インストール・"
        "JV-Data 取得の概念・プログラミング手順(C#/VB)を解説します。")
    n2, h2 = convert_guide(
        "JRA-VAN Data Lab.開発ガイド(イベント C++).pdf", "dev-guide-event-cpp.md",
        "JRA-VAN Data Lab. SDK 開発ガイド(イベント C++)",
        "JV-Link のイベント通知(確定・変更情報の受信)を C++ で扱う手引きです。"
        "`JVWatchEvent` を用いたイベント駆動の実装手順を解説します。")
    n3 = convert_jvdata_pdf()
    print(f"dev-guide.md: {n1}p, {h1} headings")
    print(f"dev-guide-event-cpp.md: {n2}p, {h2} headings")
    print(f"jv-data-spec/source-pdf.md: {n3}p")
    print("done")


if __name__ == "__main__":
    main()
