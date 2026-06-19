# JRA-VAN 仕様ドキュメント (Markdown)

`context/` に置かれた JRA-VAN Data Lab. の公式仕様書・サンプルを Markdown 化したものです。
KeibaLens など **C# 実装** から JV-Link 経由で JV-Data を取得・解析するための一次資料として使います。

> 変換元と再生成スクリプトは `tools/` にあります(仕様バージョン更新時はそれを再実行)。

## 一覧

| ドキュメント | 由来 | 内容 |
|---|---|---|
| [JV-Data 仕様書](./jv-data-spec/README.md) | `JV-Data仕様書_4.9.0.1.xlsx` | **最重要**。全レコードフォーマット(38種)/コード表(19種)/変更履歴/特記事項/データ種別/提供タイミング |
| [JV-Link インターフェース仕様](./jvlink-interface/README.md) | `JV-Linkインターフェース仕様書(Win).pdf` | **C# 実装必須**。JV-Link COM API(24メソッド)・プロパティ・戻り値コード表 |
| [C# 構造体定義](./jvdata-struct/README.md) | `JVData_Struct.cs` | 全レコードの C# 構造体サンプル(2009年版・要バージョン注意) |
| [蓄積系提供データ一覧](./accumulated-data-list.md) | `蓄積系提供データ一覧.xls` | ファイル名規則(データ種別ID×レコード種別) |
| [開発ガイド](./dev-guide.md) | `開発ガイド_4.2.2.pdf` | 開発環境・SDK・取得概念・プログラミング手順 |
| [開発ガイド(イベント C++)](./dev-guide-event-cpp.md) | `開発ガイド(イベント C++).pdf` | `JVWatchEvent` によるイベント駆動の実装 |
| [サンプルプログラム sample1](./sample-vc2019/README.md) | `sample1_VC2019/` | C++/MFC サンプル。JV-Link 呼び出しフローの実例 |
| [JV-Data 仕様書(PDF・補助)](./jv-data-spec/source-pdf.md) | `JV-Data仕様書_4.9.0.1.pdf` | xlsx と同内容の生テキスト(検索用) |

## 目的別の入口

- **レコードの項目・位置・バイト数を調べる** → [record-formats](./jv-data-spec/record-formats/README.md)
- **コードの値(場コード・馬場状態など)を調べる** → [code-tables](./jv-data-spec/code-tables/README.md)
- **JV-Link の API(JVOpen/JVRead 等)の使い方** → [jvlink-interface/methods](./jvlink-interface/methods/README.md)
- **JV-Link 戻り値(エラーコード)の意味** → [jvlink-interface/code-table](./jvlink-interface/code-table.md)
- **C# でのパース構造体** → [jvdata-struct](./jvdata-struct/README.md)
- **取得処理の流れ(初期化→取得→読込→終了)** → [sample-vc2019](./sample-vc2019/README.md)
- **ファイル名・データ種別IDの規則** → [accumulated-data-list](./accumulated-data-list.md)

## 共通事項

- 文字コード: 全角 = Shift_JIS(2バイト)、半角(英数・半角カナ)= JIS8(1バイト)。
- データ仕様の**正本は xlsx 由来**(`jv-data-spec/`)。PDF 版は補助。
- C# 構造体サンプルは 2009 年版のため、最新レコード/項目は [record-formats](./jv-data-spec/record-formats/README.md) を正とする。
- バージョン: JV-Data 4.9.0.1 / JV-Link 4.9.0.1 / 開発ガイド 4.2.2。
