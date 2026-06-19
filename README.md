<div align="center">

# 🏇 keibalens-jv-assistant

**JRA-VAN Data Lab. の JV-Data 仕様 ＆ JV-Link COM API を、AI エージェントが“正確に”引けるようにする Agent Plugin**

レコードのバイト位置も、コードの意味も、`JVOpen` の `dataspec` も。<br>
推測ではなく **変換済みの一次資料** を根拠に、エージェントが仕様レベルで回答・実装支援します。

[![GitHub Copilot CLI](https://img.shields.io/badge/GitHub%20Copilot%20CLI-plugin-000000?logo=githubcopilot&logoColor=white)](https://github.com/github/copilot-cli)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97757?logo=anthropic&logoColor=white)](https://docs.anthropic.com/en/docs/claude-code)
![Plugin](https://img.shields.io/badge/plugin-v1.0.0-1f6feb)
![JV-Data](https://img.shields.io/badge/JV--Data-4.9.0.x-2ea44f)
![JV-Link](https://img.shields.io/badge/JV--Link-4.9.0.x-2ea44f)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

</div>

---

## これは何？

`keibalens-jv-assistant` は、**JRA-VAN Data Lab.** 対応ソフトを開発するときに必要になる
**JV-Data 仕様（レコードフォーマット／コード表）** と **JV-Link COM API（メソッド・エラーコード・dataspec・option）** を、
AI エージェントが正確に参照できるようにする **Agent Plugin** です。

GitHub Copilot CLI / Claude Code などにインストールすると、JRA-VAN・競馬データに関する質問で
**スキルが自動的に発火**し、Markdown 化された仕様ドキュメントを一次資料として根拠つきで回答します。

> 💡 仕様の細部（項目のバイト位置・コードの値・メソッドの引数）は「記憶」ではなく
> **同梱ドキュメント** を開いて確認してから答える設計です。版差による誤りを抑えます。

---

## ✨ 特徴

- 📐 **全 38 レコード種別** の項目を一次資料から回答 — 位置（1始まり）・バイト数・初期値・繰返し・キー項目
- 🔢 **19 種のコード表** を即引き — 競馬場 / 馬場状態 / 競走種別 / グレード など
- 🔌 **JV-Link COM API 24 メソッド** — `JVInit` / `JVOpen` / `JVRTOpen` / `JVRead` / `JVGets` / `JVStatus` / `JVWatchEvent` / `JVClose` の引数・戻り値・エラーコード
- 🧭 **dataspec / option 早見** — 蓄積系（`JVOpen`）・速報系（`JVRTOpen`）・イベント（`JVWatchEvent`）の使い分け
- 💻 **C# 実装ガイド** — Shift_JIS 固定長レコードのパース（エンコーディング登録・`MidB2S`・繰返し項目・未知レコードのスキップ）
- 🎯 **自動発火** — JRA-VAN / JV-Data / JV-Link / 競馬データ取得・解析・C# 実装の質問でスキルが自動的に参照される

> 📚 収録ドキュメント：**158 ファイル**（レコードフォーマット 38・コード表 19・JV-Link メソッド 24・C# 構造体 38・開発ガイド／サンプル ほか）

---

## 📦 インストール

### GitHub Copilot CLI（対話セッション内）

```text
/plugin marketplace add KeibaLensProject/keibalens-jv-assistant
/plugin install jra-van-spec-skills@keibalens-jv-assistant
```

- 1 行目：このリポジトリをマーケットプレイスとして登録（`OWNER/REPO`）
- 2 行目：マーケットプレイス `keibalens-jv-assistant` からプラグイン `jra-van-spec-skills` を導入

### ターミナル（セッション外）

```shell
copilot plugin marketplace add KeibaLensProject/keibalens-jv-assistant
copilot plugin install jra-van-spec-skills@keibalens-jv-assistant
```

### マーケットプレイスを介さず直接インストール

```shell
copilot plugin install KeibaLensProject/keibalens-jv-assistant:plugins/jra-van-spec-skills
```

導入確認は `/plugin list` ・ `/skills list`。インストール後は、JRA-VAN / JV-Data / JV-Link / 競馬データの
取得・解析・C# 実装に関する質問で、このスキルが自動的に参照されます。

---

## 💬 こんな質問に答えます

```text
「SE レコードの確定着順は何バイト目？」
「当日のリアルタイムオッズを取る dataspec は？」
「JVOpen が -202 を返す原因は？」
「O2（馬連オッズ）を C# でパースする方法は？」
「速報のみのレコード（WH/WE/AV/JC/TC/CC）はどう取得する？」
「RA / SE / HR / O1〜O6 / H1 / H6 の構造とレコード長を教えて」
```

質問の種類に応じて、スキルが適切なドキュメント（レコードフォーマット表・コード表・メソッド詳細・
自作の早見ガイド）を開いて回答します。

---

## 🗂️ 構成

```text
keibalens-jv-assistant/
├─ .github/plugin/
│  └─ marketplace.json                 # マーケットプレイス定義（source = plugins/jra-van-spec-skills）
└─ plugins/
   └─ jra-van-spec-skills/             # ← プラグイン本体（インストール時はここが配布される）
      ├─ plugin.json                   #   プラグイン マニフェスト（skills を宣言）
      └─ skills/
         └─ jra-van-spec-skills/       #   スキル本体（自己完結）
            ├─ SKILL.md                #     発火条件＆参照ルーティング
            └─ references/
               ├─ record-index.md      #       全 38 レコード 統合早見表
               ├─ dataspec-option.md   #       dataspec / option 早見
               ├─ csharp-parsing.md    #       C# パース実装ガイド
               ├─ jvlink-flow.md       #       JV-Link 呼び出しフロー
               └─ spec/                #       仕様ドキュメント（一次資料・158 ファイル）
                  ├─ jv-data-spec/     #         レコードフォーマット 38 / コード表 19 ほか
                  ├─ jvlink-interface/ #         JV-Link メソッド 24・プロパティ・コード表
                  ├─ jvdata-struct/    #         C# 構造体サンプル（38）
                  └─ sample-vc2019/    #         C++/MFC 呼び出しフロー実例
```

スキルは一次資料 `references/spec/` を内包して **自己完結** しているため、配布物はそれ単体で動作します。

---

## 🤖 対応エージェント

| エージェント | 導入方法 |
|---|---|
| **GitHub Copilot CLI** | `/plugin marketplace add` → `/plugin install`（上記） |
| **Claude Code** | 同じ `/plugin` コマンド体系（marketplace add → install）に対応 |

標準的なプラグイン マニフェスト（`marketplace.json` ＋ `plugin.json` ＋ `SKILL.md`）形式のため、
互換のプラグイン機構を持つエージェントで利用できます。

---

## 🏇 前提・関連リンク

本プラグインは **仕様の参照と実装支援** を行うものです。実際に JRA-VAN Data Lab. のデータを取得・利用するには、
JRA-VAN が配布する **SDK（JV-Link 等）** が別途必要です。

- 🔗 [JRA-VAN Data Lab. SDK（developer.jra-van.jp）](https://developer.jra-van.jp/t/topic/45)
- 🔗 [JRA-VAN Data Lab.](https://jra-van.jp/dlab/)

> 本プロジェクトは JRA-VAN の公式提供物ではありません。

---

## 📄 ライセンス

[MIT License](./LICENSE) © 2026 KeibaLensProject