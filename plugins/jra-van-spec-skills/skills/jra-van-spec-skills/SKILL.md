---
name: jra-van-spec-skills
description: >-
  JRA-VAN Data Lab. の JV-Data 仕様と JV-Link COM API の参照ガイド。JV-Data の
  レコードフォーマット(項目の位置・バイト数・初期値・繰返し)、コード表(競馬場/馬場状態/競走種別/
  グレード等)、JV-Link のメソッド(JVInit/JVOpen/JVRTOpen/JVRead/JVGets/JVStatus/JVClose 等)・
  戻り値(エラー)コード・データ種別ID(dataspec)・option・ファイル名規則、C# 構造体定義と
  固定長 Shift_JIS レコードのパース手法を、変換済みドキュメントから探して正確に答える。
  JRA-VAN・JV-Data・JV-Link・競馬データの取得/解析・C# 実装に関する質問では必ずこのスキルを使うこと。
  レコードの項目位置やバイト数、コードの意味、JVOpen の dataspec/option の指定、エラーコードの意味、
  馬毎レース情報(SE)・レース詳細(RA)・払戻(HR)・オッズ(O1〜O6)・票数(H1/H6)・各マスタの構造を
  聞かれたら、推測せず必ずこのスキルで変換済みドキュメントを参照して回答すること。keibalens など競馬予想ソフトの
  データ取り込み実装でも使う。
---

# JRA-VAN 仕様ガイド (JV-Data / JV-Link)

JRA-VAN Data Lab. SDK (Ver.5.0.0) の公式仕様書・構造体・サンプルを Markdown 化した `references/spec/` を一次資料として、
**JV-Data 仕様**と **JV-Link COM API (64bit版 / 32bit版)** に関する質問に正確に答え、**C# / Python での取得・パース実装**を支援するスキルです。

> **重要**: 仕様の細部(項目のバイト位置・コードの値・メソッドの引数など)は記憶で答えず、必ず
> `references/spec/` の該当ファイルを開いて確認してから回答すること。仕様は版で変わるため、一次資料が正です。

## ドキュメントの場所

本スキルは付属の `references/spec/`（スキル直下の `references/` 配下）を一次資料として参照します。本文中のパスはこのスキル直下（SKILL.md のある場所）からの相対です。

```
references/spec/
  README.md                       全体インデックス
  jv-data-spec/                   ← JV-Data 仕様(xlsx 由来・正本, 4.9.0.1)
    record-formats/               レコードフォーマット(38種, ID ごと)
    code-tables/                  コード表(19種, 番号ごと)
    change-history.md / special-notes.md / data-types.md / data-timing.md
  jvlink-interface/               ← JV-Link COM API(PDF 由来, 32bit/64bit 共通)
    methods/                      メソッド詳細(24個)
    properties.md / code-table.md / overview.md
  jvdata-struct/                  ← C# 構造体サンプル(JVData_Struct.cs 由来, 2009年版)
  jvdata-struct-py/               ← Python 構造体サンプル(JVData_Struct.py 由来, 2026年版・4.9.0.1準拠)
  accumulated-data-list.md        ファイル名規則・提供単位
  dev-guide.md                    開発ガイド(第4.2.3版: VS2026・64bit対応・Python追加)
  dev-guide-event-cpp.md          イベント開発ガイド(C++ / VS2026, 第4.0.0版)
  dev-guide-event-python.md       イベント開発ガイド(Python / pywin32, 第1.0.0版)
  sample-vc2019/                  C++/MFC サンプル(sample1_VC2026 由来・呼び出しフロー実例)
  sample-python/                  Python 3.14 サンプル(sample1_Python3.14 由来・JVGets 呼び出し実例)
```

## 質問 → 参照先ルーティング

まず質問の種類を見分け、対応するドキュメントを開く。

| 質問の種類 | 開くドキュメント |
|---|---|
| あるレコードの**項目の位置・バイト数・初期値・意味** | `references/spec/jv-data-spec/record-formats/<連番>-<ID>-<名称>.md` |
| **どのレコードがどの ID か**／レコード長の一覧 | `references/spec/jv-data-spec/record-formats/README.md`、または本スキルの [references/record-index.md](./references/record-index.md) |
| **コードの値の意味**(競馬場・馬場状態・競走種別・グレード等) | `references/spec/jv-data-spec/code-tables/<番号>-<名称>.md` |
| **JV-Link メソッドの引数・戻り値・使い方**(JVOpen/JVRead/JVGets 等) | `references/spec/jvlink-interface/methods/<連番>-<名称>.md` |
| **JV-Link の戻り値(エラー)コードの意味** | `references/spec/jvlink-interface/code-table.md` |
| **JV-Link のプロパティ**(m_servicekey 等) | `references/spec/jvlink-interface/properties.md` |
| **JV-Link 64bit版 / 32bit版の仕様・共存・利用キー・Python 連携** | 本スキルの [references/jvlink-flow.md](./references/jvlink-flow.md)、`references/spec/dev-guide.md`、`references/spec/dev-guide-event-python.md` |
| **dataspec(データ種別ID)・option の指定**、どの dataspec にどのレコードが含まれるか | 本スキルの [references/dataspec-option.md](./references/dataspec-option.md)、`references/spec/jv-data-spec/data-types.md` |
| **ファイル名の規則・提供タイミング・提供単位** | `references/spec/accumulated-data-list.md`、`references/spec/jv-data-spec/data-timing.md` |
| **C# 構造体**(JV_RA_RACE 等)とフィールド | `references/spec/jvdata-struct/<連番>-<名称>.md`、一覧は `references/spec/jvdata-struct/README.md` |
| **Python 構造体(`@dataclass`)**・最新 4.9.0.1 オフセット実装 | `references/spec/jvdata-struct-py/<連番>-<名称>.md`、一覧は `references/spec/jvdata-struct-py/README.md` |
| **取得処理の全体フロー**(初期化→取得→読込→終了) | 本スキルの [references/jvlink-flow.md](./references/jvlink-flow.md)、`references/spec/sample-vc2019/README.md`、`references/spec/sample-python/README.md` |
| **C# / Python で固定長レコードをパースする方法** | 本スキルの [references/csharp-parsing.md](./references/csharp-parsing.md) |
| 仕様の**変更履歴**・特記事項 | `references/spec/jv-data-spec/change-history.md` / `special-notes.md` |

レコード種別ID(TK/RA/SE/HR/H1/H6/O1〜O6/UM/KS/CH/BR/BN/HN/SK/CK/RC/HC/HS/HY/YS/BT/CS/DM/TM/WF/JG/WC/WH/WE/AV/JC/TC/CC)
からファイルを引く早見表は [references/record-index.md](./references/record-index.md) にある。

## JV-Data の基礎(回答前に押さえる)

- **固定長レコード**: 1 レコード = レコード種別ごとに決まったバイト長(例: RA=1272, SE=555)。
  各項目は「位置(1 始まり)」と「バイト長」で定義される。レコードフォーマット表の **位置/バイト** 列がそのまま
  パースのオフセットになる。
- **文字コード**: 全角 = Shift_JIS(2 バイト)、半角(英数・半角カナ) = JIS8(1 バイト)。
  C# では `Encoding.GetEncoding("Shift_JIS")` でデコードする(.NET Core 以降は
  `System.Text.Encoding.CodePagesEncodingProvider` の登録が必要)。
- **レコード先頭 = レコード種別ID(2 バイト)**: 読み込んだ行の先頭 2 バイトでレコード種別を判定し、
  対応するフォーマットでパースする。**未知のレコード種別IDは読み飛ばす**こと(仕様追加で増えるため)。
- **キー項目**: フォーマット表の「キー」列が JRA-VAN 推奨の主キー。収録順は不定なので、DB 反映時は
  キー項目とデータ作成年月日で突き合わせる。
- **初期値**: `0`=半角"0", `sp`=半角スペース, `Ｓ`=全角スペース。未設定項目はこの値で埋まる。

## C# / Python 実装の最短ルート

1. **取得**: JV-Link(COM `JVDTLab.JVLink`)を使い `JVInit → (設定) → JVOpen/JVRTOpen → JVStatus/JVRead/JVGets → JVClose`。
   SDK Ver.5.0.0 より **64bit版 JV-Link** と **32bit版 JV-Link** の両方が利用でき、呼び出しプロセスの bit 数(x64/x86)に応じた方が使われる。
   詳細フローと C# / Python (`pywin32`) 擬似コードは [references/jvlink-flow.md](./references/jvlink-flow.md)。
2. **どの dataspec を JVOpen に渡すか**は [references/dataspec-option.md](./references/dataspec-option.md) で確認。
   蓄積系(過去データ)は `JVOpen`、速報系(当日)は `JVRTOpen`、確定/変更通知は `JVWatchEvent`。
3. **パース**: 取得した 1 レコード(Shift_JIS バイト列)を、該当レコードフォーマット表の 位置/バイト に従って
   切り出す。C# は `references/spec/jvdata-struct/`、Python は `references/spec/jvdata-struct-py/`（2026年版・4.9.0.1 最新オフセット準拠）の `MidB2S(buf, 位置, バイト)` ヘルパと構造体サンプルがそのまま使える。
   手順は [references/csharp-parsing.md](./references/csharp-parsing.md)。

## 注意点(よくある落とし穴)

- **C# 構造体サンプル(`jvdata-struct/`)は 2009 年版、Python 構造体サンプル(`jvdata-struct-py/`)は 2026 年版**。
  C# 版は 2023 年の N付き拡張（繁殖登録番号 8→10B、生産者コード 6→8B、生産者名 70→72B）や 2021 年の WC 10ハロン拡張が未反映だが、Python 版は 4.9.0.1 の最新サイズに完全準拠している。フィールドの位置/バイト数の**正本は必ず
  `references/spec/jv-data-spec/record-formats/`（または `jvdata-struct-py/`）を参照**すること。
- **JV-Link 64bit版 / 32bit版の共存と利用キー**: SDK Ver.5.0.0（2026年8月公開）で 64bit版 JV-Link が追加された。
  同一 PC に 32bit版と 64bit版を共存インストール可能だが、**それぞれに異なる利用キーを登録する必要がある**（同一キーを両方に設定すると `-301` エラー）。ソフトID(`JVInit`)は共通。ポート番号は重複不可、設定画面(`JVSetUIProperties`)の同時起動は不可（詳細は [references/jvlink-flow.md](./references/jvlink-flow.md)）。
- **データ仕様の正本は xlsx 由来の `references/spec/jv-data-spec/`**。`references/spec/jv-data-spec/source-pdf.md` は同内容の PDF
  生テキスト(検索補助)で、表は xlsx 由来が正。
- **位置は 1 始まり**。C# / Python のバイト配列(0 始まり)に直すときは `位置 - 1`。`MidB2S` ヘルパは内部で `-1` 済み。
- **速報のみのレコード**(WH/WE/AV/JC/TC/CC)は蓄積系 dataspec を持たず、`JVRTOpen`(0B11/0B14/0B16 等)
  または `JVWatchEvent` 経由で取得する。蓄積取得(`JVOpen`)では取れない。
- **馬単(O4)・3連単(O6/H6)** はオッズ・票数として仕様上は存在する。取得要否はアプリ側の方針で決める
  (本スキルは仕様参照が目的なので全レコードを対象に説明する)。

## references（必要に応じて読む）

- [references/record-index.md](./references/record-index.md) — 全 38 レコードの統合早見表
  (レコード種別ID・名称・レコード長・主な dataspec・フォーマット/C#・Python 構造体ファイル・主な構造体)。
- [references/dataspec-option.md](./references/dataspec-option.md) — dataspec(データ種別ID)と option の対応、
  蓄積系/速報系/セットアップの区分、JVOpen/JVRTOpen/JVWatchEvent の使い分け。
- [references/csharp-parsing.md](./references/csharp-parsing.md) — 固定長 Shift_JIS レコードを C# / Python でパースする
  実装手順(エンコーディング登録・MidB2S・繰返し項目・数値/日付変換・未知レコードのスキップ)。
- [references/jvlink-flow.md](./references/jvlink-flow.md) — JV-Link 呼び出しフロー(蓄積/リアルタイム/イベント)、
  Ver.5.0.0(64bit/32bit)の仕様・注意点、C# / Python (`pywin32`) 擬似コード。
