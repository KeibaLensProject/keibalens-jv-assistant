# JV-Link メソッド一覧

出典: `context/JV-Linkインターフェース仕様書_4.9.0.1(Win).pdf`

JV-Link が提供する COM メソッドの一覧です。C# からはこれらを呼び出してJV-Data の取得・読み込み・映像再生などを行います。

| メソッド | 処理内容 | 詳細 |
|---|---|---|
| JVInit | JV-Link の初期化をします。 | [リンク](./01-JVInit.md) |
| JVSetUIProperties | JV-Link の設定変更(ダイアログ版)をします。 | [リンク](./02-JVSetUIProperties.md) |
| JVSetServiceKey | JV-Link の設定変更(利用キー)をします。 | [リンク](./03-JVSetServiceKey.md) |
| JVSetSaveFlag | JV-Link の設定変更(保存フラグ)をします。 | [リンク](./04-JVSetSaveFlag.md) |
| JVSetSavePath | JV-Link の設定変更(保存パス)をします。 | [リンク](./05-JVSetSavePath.md) |
| JVOpen | 蓄積系データの取得要求をします。 | [リンク](./06-JVOpen.md) |
| JVRTOpen | リアルタイム系データの取得要求をします。 | [リンク](./07-JVRTOpen.md) |
| JVStatus | ダウンロード進捗情報の取得をします。 | [リンク](./08-JVStatus.md) |
| JVRead | JV-Data の読み込みをします。 | [リンク](./09-JVRead.md) |
| JVGets | JV-Data の読み込みをします。 | [リンク](./10-JVGets.md) |
| JVSkip | JV-Data の読みとばしをします。 | [リンク](./11-JVSkip.md) |
| JVCancel | ダウンロードスレッドの停止をします。 | [リンク](./12-JVCancel.md) |
| JVClose | JV-Data 読み込み処理の終了をします。 | [リンク](./13-JVClose.md) |
| JVFiledelete | ダウンロードしたファイルの削除をします。 | [リンク](./14-JVFiledelete.md) |
| JVFukuFile | 勝負服画像情報要求をします。 | [リンク](./15-JVFukuFile.md) |
| JVFuku | 勝負服画像情報要求(バイナリ)をします。 | [リンク](./16-JVFuku.md) |
| JVMVCheck / JVMVCheckWithType | JRA レーシングビュアーレース映像公開チェック要求をします。 | [リンク](./17-JVMVCheck-JVMVCheckWithType.md) |
| JVMVPlay / JVMVPlayWithType | JRA レーシングビュアーレース映像再生要求をします。 | [リンク](./18-JVMVPlay-JVMVPlayWithType.md) |
| JVMVOpen | 動画リストの取得要求をします。 | [リンク](./19-JVMVOpen.md) |
| JVMVRead | 動画リストの読み込みをします。 | [リンク](./20-JVMVRead.md) |
| JVCourseFile | コース図の取得要求をします。 | [リンク](./21-JVCourseFile.md) |
| JVCourseFile2 | コース図の取得要求をします。 | [リンク](./22-JVCourseFile2.md) |
| JVWatchEvent | 確定・変更情報の発生を通知するイベント通知を開始します。 | [リンク](./23-JVWatchEvent.md) |
| JVWatchEventClose | イベント通知を終了します。 | [リンク](./24-JVWatchEventClose.md) |

## 関連

- [プロパティ](../properties.md)
- [コード表(戻り値)](../code-table.md)
- [概要・目次](../overview.md)
