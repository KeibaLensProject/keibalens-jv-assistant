"""JV-Linkインターフェース仕様書(Win).pdf -> references/spec/jvlink-interface/ (Markdown).

PyMuPDF(fitz)でフォントサイズを使って構造抽出する。
  - size>=13.5 : メソッド名/章見出し
  - size 12    : メソッドの一行説明
  - size 10.8-11.5 : パラメータ名/小見出し
  - size 10.5  : 本文
セクション境界はマーカー(修正履歴/1.プロパティ/2.メソッド/3.コード表)で自動検出。
メソッド詳細はメソッド名見出しで分割。同一ページに連続する JV* 見出しで本文が
空の場合は co-documented メソッドとして1ファイルに結合する(例: JVMVCheck /
JVMVCheckWithType)。
"""
import io
import os
import re
import sys
import unicodedata

import fitz
import pdfplumber

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "plugins", "jra-van-spec-skills", "skills",
                    "jra-van-spec-skills", "references", "spec")
SRC = os.path.join(ROOT, "context", "JV-Linkインターフェース仕様書_4.9.0.1(Win).pdf")
OUT = os.path.join(SPEC, "jvlink-interface")
VERSION = "4.9.0.1"
RUNNING_HEADER = "JV-Linkインターフェース仕様書"
HEAD = 13.5      # メソッド名/章見出し
DESC_MIN = 11.6  # 一行説明の下限
PARAM_MIN, PARAM_MAX = 10.8, 11.5
SECTION_LABELS = {"【構文】", "【パラメータ】", "【戻り値】", "【解説】", "【補足】", "【使用例】"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    return s.replace("\u3000", " ")


def safe_name(s: str) -> str:
    s = re.sub(r'[<>:"/\\|?*]', "", s)
    return s.strip().replace(" ", "")


def page_lines(page):
    """[(size, text)] を読み順(上→下,左→右)で返す。"""
    blocks = page.get_text("dict")["blocks"]
    rows = []
    for b in blocks:
        lines = b.get("lines")
        if not lines:
            continue
        y0, x0 = b["bbox"][1], b["bbox"][0]
        rows.append((round(y0, 1), round(x0, 1), lines))
    rows.sort(key=lambda r: (r[0], r[1]))
    out = []
    for _, _, lines in rows:
        for ln in lines:
            spans = ln["spans"]
            text = "".join(s["text"] for s in spans)
            t = norm(text).rstrip()
            if not t.strip():
                continue
            size = max((s["size"] for s in spans), default=0.0)
            out.append((size, t))
    return out


def strip_running(lines, pageno):
    out = []
    for size, t in lines:
        s = t.strip()
        if s == RUNNING_HEADER:
            continue
        if re.fullmatch(r"\d{1,3}", s) and int(s) == pageno:
            continue
        out.append((size, t))
    return out


def md_escape(s: str) -> str:
    return s.replace("|", "\\|")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def fmt_body(lines):
    """メソッド本文の (size,text) 行を Markdown 文字列へ整形。

    PDF の折返しで分割された和文行は同一段落へ連結する。段落は
    節ラベル(【...】)/パラメータ名(size~11)/構文ブロックで区切る。
    """
    md = []
    para = []
    in_syntax = False
    syntax_buf = []

    def flush_para():
        if para:
            md.append("".join(para))
            md.append("")
        para.clear()

    def flush_syntax():
        nonlocal in_syntax
        if syntax_buf:
            md.append("```")
            md.extend(syntax_buf)
            md.append("```")
            md.append("")
        syntax_buf.clear()
        in_syntax = False

    for size, t in lines:
        s = t.strip()
        if s in SECTION_LABELS:
            flush_para()
            if in_syntax:
                flush_syntax()
            label = s.strip("【】")
            md.append(f"### {label}")
            md.append("")
            in_syntax = (s == "【構文】")
            continue
        if in_syntax:
            syntax_buf.append(s)
            continue
        if PARAM_MIN <= size <= PARAM_MAX and len(s) < 40:
            flush_para()
            md.append(f"**{s}**")
            md.append("")
        else:
            para.append(s)
    flush_para()
    flush_syntax()
    res = []
    for line in md:
        if line == "" and res and res[-1] == "":
            continue
        res.append(line)
    return "\n".join(res).strip() + "\n"


def build_code_tables(sec3):
    """コード表をメソッド群ごとの3列表に再構成。

    群ラベル(JVInit 等)とテーブルを y 座標でマージし、戻り値列が
    非空の行を論理行の開始として複数行セルを連結する。
    """
    label_pat = re.compile(r"^JV[A-Za-z0-9]+(?:/JV[A-Za-z0-9]+)*$")
    groups = []          # [(name, [ (戻り値, 意味, 原因と対処), ... ])]
    index = {}
    cur = None

    doc = fitz.open(SRC)
    with pdfplumber.open(SRC) as pdf:
        for pno in range(sec3, doc.page_count):
            events = []
            for b in doc[pno].get_text("dict")["blocks"]:
                for ln in b.get("lines", []):
                    t = norm("".join(s["text"] for s in ln["spans"])).strip()
                    if label_pat.match(t):
                        events.append((round(b["bbox"][1], 1), "label", t))
            for tb in pdf.pages[pno].find_tables():
                events.append((round(tb.bbox[1], 1), "table", tb.extract()))
            events.sort(key=lambda e: e[0])
            for _, kind, payload in events:
                if kind == "label":
                    if payload not in index:
                        index[payload] = len(groups)
                        groups.append((payload, []))
                    cur = index[payload]
                else:
                    if cur is None:
                        index["(冒頭)"] = len(groups)
                        groups.append(("(冒頭)", []))
                        cur = index["(冒頭)"]
                    rows = groups[cur][1]
                    for r in payload:
                        c = [norm(x).strip() if x else "" for x in (r + ["", "", ""])[:3]]
                        if c == ["戻り値", "意味", "原因と対処"]:
                            continue
                        if not any(c):
                            continue
                        if c[0]:
                            rows.append(c)
                        elif rows:
                            rows[-1][1] += c[1]
                            rows[-1][2] += c[2]
    doc.close()

    out = ["# JV-Link コード表(メソッド戻り値)",
           "",
           f"出典: `context/{os.path.basename(SRC)}`",
           "",
           "各メソッドの戻り値とその意味・対処です。`0` は正常、負値はエラーの理由コードです。",
           ""]
    for name, rows in groups:
        out.append(f"## {name}")
        out.append("")
        out.append("| 戻り値 | 意味 | 原因と対処 |")
        out.append("|---|---|---|")
        for r0, r1, r2 in rows:
            out.append(f"| {md_escape(r0)} | {md_escape(r1)} | {md_escape(r2)} |")
        out.append("")
    return "\n".join(out).strip() + "\n", len(groups)


def build_properties(pages, sec1, sec2):
    """プロパティ表を | 型 | プロパティ | 説明 | に再構成。

    PDF はセル罫線を持たないため、型キーワード(Integer/String/Long)+既知の
    プロパティ名の境界でテキストを分割する。
    """
    names = ["m_TotalReadFilesize", "m_CurrentReadFilesize", "m_CurrentFileTimestamp",
             "m_JVLinkVersion", "m_servicekey", "m_savepath", "m_saveflag",
             "m_payflag", "ParentHWnd"]
    alt = "|".join(names)
    raw = "".join(t for i in range(sec1, sec2) for _, t in pages[i])
    raw = raw.replace("プロパティ説明", "")          # 表ヘッダ除去
    raw = re.sub(rf"^.*?(?=(?:Integer|String|Long)(?:{alt}))", "", raw, count=1)
    chunks = re.split(rf"(?=(?:Integer|String|Long)(?:{alt}))", raw)
    rows = []
    for ch in chunks:
        m = re.match(rf"(Integer|String|Long)({alt})(.*)", ch, re.S)
        if not m:
            continue
        rows.append((m.group(1), m.group(2), m.group(3).strip()))
    out = [f"# JV-Link プロパティ\n\n出典: `context/{os.path.basename(SRC)}`\n",
           "JV-Link が公開するプロパティです。`m_savepath`/`m_servicekey` は設定値、"
           "`m_CurrentFileTimestamp` は再開用、`m_TotalReadFilesize` は進捗表示に使います。\n",
           "| 型 | プロパティ | 説明 |", "|---|---|---|"]
    for typ, name, desc in rows:
        out.append(f"| {typ} | {md_escape(name)} | {md_escape(desc)} |")
    return "\n".join(out) + "\n", len(rows)


def main():
    doc = fitz.open(SRC)
    if os.path.isdir(OUT):
        import shutil
        shutil.rmtree(OUT)
    npages = doc.page_count
    pages = [strip_running(page_lines(doc[i]), i + 1) for i in range(npages)]

    def has_head(i, pred):
        return any(size >= HEAD and pred(t.strip()) for size, t in pages[i])

    rev_start = next(i for i in range(npages)
                     if any(t.strip() == "修正履歴" for _, t in pages[i]))
    toc = next(i for i in range(npages)
               if any("...." in t for _, t in pages[i]))
    sec1 = next(i for i in range(npages)
                if has_head(i, lambda s: s.startswith("1.") and "プロパティ" in s))
    sec2 = next(i for i in range(npages)
                if has_head(i, lambda s: s.startswith("2.") and "メソッド" in s))
    sec3 = next(i for i in range(npages)
                if has_head(i, lambda s: s.startswith("3.") and "コード表" in s))

    # --- 修正履歴 ---
    rev = []
    for i in range(rev_start, toc):
        rev += [t for _, t in pages[i]]
    write(os.path.join(OUT, "revision-history.md"),
          "# JV-Link インターフェース仕様書 修正履歴\n\n出典: `context/" +
          os.path.basename(SRC) + "`\n\n```\n" + "\n".join(rev) + "\n```\n")

    # --- 目次(overview) ---
    toc_lines = []
    for i in range(0, rev_start):       # 表紙
        toc_lines += [t for _, t in pages[i]]
    toc_body = []
    for i in range(toc, sec1):
        toc_body += [t for _, t in pages[i]]
    write(os.path.join(OUT, "overview.md"),
          f"# JV-Link インターフェース仕様書 概要 (v{VERSION})\n\n"
          f"出典: `context/{os.path.basename(SRC)}`\n\n"
          "JRA-VAN Data Lab. の JV-Link COM コンポーネントが提供する API 仕様書です。"
          "C# からの JV-Data 取得処理はこの JV-Link を経由します。\n\n"
          "## 目次\n\n```\n" + "\n".join(toc_body) + "\n```\n\n"
          "- [プロパティ](./properties.md)\n"
          "- [メソッド一覧と詳細](./methods/README.md)\n"
          "- [コード表(戻り値)](./code-table.md)\n"
          "- [修正履歴](./revision-history.md)\n")

    # --- プロパティ ---
    prop_md, nprops = build_properties(pages, sec1, sec2)
    write(os.path.join(OUT, "properties.md"), prop_md)

    # --- コード表 ---
    code_md, ngroups = build_code_tables(sec3)
    write(os.path.join(OUT, "code-table.md"), code_md)

    # --- メソッド詳細を分割 ---
    method_lines = []
    for i in range(sec2, sec3):
        method_lines += pages[i]

    methods = []           # [{"names":[...], "desc":str, "body":[(size,t)]}]
    intro = []             # 2.1 メソッド一覧 など(最初のメソッド見出し前)
    cur = None
    for size, t in method_lines:
        s = t.strip()
        if size >= HEAD:
            if s.startswith("JV"):
                if cur and not cur["body"] and not cur["desc"]:
                    cur["names"].append(s)          # co-documented で結合
                else:
                    cur = {"names": [s], "desc": "", "body": []}
                    methods.append(cur)
                continue
            elif cur is None:
                intro.append((size, t))             # 2.メソッド / 2.1 など
                continue
            elif not cur["body"] and not cur["desc"]:
                cur["names"][-1] += s                # 折返し継続(例: 'JVSetUIPropertie'+'s')
                continue
            else:
                cur["body"].append((size, t))
                continue
        # 継続フラグメント('s' など, JVで始まらない大文字でないもの)
        if cur is None:
            intro.append((size, t))
            continue
        if DESC_MIN <= size and not cur["body"] and not cur["desc"]:
            cur["desc"] = s
            continue
        cur["body"].append((size, t))

    # --- メソッド一覧(intro)から名前→説明を取得 ---
    desc_map = {}
    intro_txt = [t.strip() for _, t in intro]
    for j, line in enumerate(intro_txt):
        if re.fullmatch(r"JV[A-Za-z0-9]+", line) and j + 1 < len(intro_txt):
            nxt = intro_txt[j + 1]
            if not re.fullmatch(r"JV[A-Za-z0-9]+", nxt):
                desc_map.setdefault(line, nxt)

    # --- 各メソッドファイル ---
    os.makedirs(os.path.join(OUT, "methods"), exist_ok=True)
    index_rows = []
    for n, m in enumerate(methods, 1):
        primary = m["names"][0]
        fname = f"{n:02d}-{'-'.join(m['names'])}.md"
        fname = safe_name(fname)
        title = " / ".join(m["names"])
        desc = m["desc"] or desc_map.get(primary, "")
        parts = [f"# {title}", ""]
        if desc:
            parts += [f"*{desc}*", ""]
        parts.append(fmt_body(m["body"]))
        write(os.path.join(OUT, "methods", fname), "\n".join(parts))
        index_rows.append((primary, m["names"], desc, fname))

    # --- methods/README.md(一覧) ---
    idx = ["# JV-Link メソッド一覧",
           "",
           f"出典: `context/{os.path.basename(SRC)}`",
           "",
           "JV-Link が提供する COM メソッドの一覧です。C# からはこれらを呼び出して"
           "JV-Data の取得・読み込み・映像再生などを行います。",
           "",
           "| メソッド | 処理内容 | 詳細 |",
           "|---|---|---|"]
    for primary, names, desc, fname in index_rows:
        label = " / ".join(names)
        d = desc_map.get(primary, desc)
        idx.append(f"| {md_escape(label)} | {md_escape(d)} | [リンク](./{fname}) |")
    idx += ["", "## 関連", "",
            "- [プロパティ](../properties.md)",
            "- [コード表(戻り値)](../code-table.md)",
            "- [概要・目次](../overview.md)", ""]
    write(os.path.join(OUT, "methods", "README.md"), "\n".join(idx))

    # --- jvlink-interface/README.md ---
    write(os.path.join(OUT, "README.md"),
          f"# JV-Link インターフェース仕様 (v{VERSION})\n\n"
          f"出典: `context/{os.path.basename(SRC)}`\n\n"
          "JRA-VAN Data Lab. の **JV-Link** COM コンポーネント API 仕様です。"
          "C# (および VB) から JV-Data を取得する際の中核 API で、初期化・データ取得要求・"
          "読み込み・進捗取得・映像再生などのメソッドを提供します。\n\n"
          "## 目次\n\n"
          "- [概要・目次](./overview.md)\n"
          "- [プロパティ](./properties.md)\n"
          f"- [メソッド一覧と詳細](./methods/README.md) ({len(methods)}メソッド)\n"
          "- [コード表(戻り値)](./code-table.md)\n"
          "- [修正履歴](./revision-history.md)\n\n"
          "## 主要メソッドの流れ(蓄積系)\n\n"
          "```\n"
          "JVInit            … 初期化(最初に1回)\n"
          "  └ JVSetServiceKey/JVSetSaveFlag/JVSetSavePath … 設定(任意)\n"
          "JVOpen            … 蓄積系データ取得要求(dataspec/option/fromtime)\n"
          "  └ JVStatus      … ダウンロード進捗\n"
          "  └ JVRead/JVGets … JV-Data を1レコードずつ読み込み\n"
          "  └ JVSkip        … 読みとばし\n"
          "JVClose           … 取り込み終了\n"
          "```\n\n"
          "リアルタイム系は `JVRTOpen` を使用します。確定・変更通知は "
          "`JVWatchEvent`/`JVWatchEventClose` を使用します。\n")

    print(f"methods: {len(methods)}")
    print(f"properties: {nprops}")
    print(f"code-table groups: {ngroups}")
    print("done")


if __name__ == "__main__":
    main()
