# JV-Link インターフェース仕様 (v4.9.0.1)

出典: `context/JV-Linkインターフェース仕様書_4.9.0.1(Win).pdf`

JRA-VAN Data Lab. の **JV-Link** COM コンポーネント API 仕様です。C# (および VB) から JV-Data を取得する際の中核 API で、初期化・データ取得要求・読み込み・進捗取得・映像再生などのメソッドを提供します。

## 目次

- [概要・目次](./overview.md)
- [プロパティ](./properties.md)
- [メソッド一覧と詳細](./methods/README.md) (24メソッド)
- [コード表(戻り値)](./code-table.md)
- [修正履歴](./revision-history.md)

## 主要メソッドの流れ(蓄積系)

```
JVInit            … 初期化(最初に1回)
  └ JVSetServiceKey/JVSetSaveFlag/JVSetSavePath … 設定(任意)
JVOpen            … 蓄積系データ取得要求(dataspec/option/fromtime)
  └ JVStatus      … ダウンロード進捗
  └ JVRead/JVGets … JV-Data を1レコードずつ読み込み
  └ JVSkip        … 読みとばし
JVClose           … 取り込み終了
```

リアルタイム系は `JVRTOpen` を使用します。確定・変更通知は `JVWatchEvent`/`JVWatchEventClose` を使用します。
