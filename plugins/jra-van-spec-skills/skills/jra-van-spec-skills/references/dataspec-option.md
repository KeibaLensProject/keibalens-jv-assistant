# dataspec(データ種別ID)と option

JV-Link の取得要求(`JVOpen` / `JVRTOpen`)で「何を」「どの範囲で」取るかを決めるのが **dataspec** と **option**。

- **dataspec**: 取得したいデータを表す **4 桁固定のデータ種別ID**。複数連結する場合は 4 の倍数桁にする
  (例: `"RACEDIFF"` = RACE + DIFF)。蓄積系は `JVOpen` に、速報系(0Bxx)は `JVRTOpen` に渡す。
- **option**(JVOpen のみ): 取得範囲の指定。
  - `1` 通常データ(全データから dataspec/fromtime に該当するもの。蓄積系ソフトの差分更新)
  - `2` 今週データ(直近の未来レース＋直前レース成績のみ。非蓄積系ソフト向け)
  - `3` セットアップデータ
  - `4` ダイアログ無しセットアップデータ(初回のみダイアログ表示)

詳細は `references/spec/jvlink-interface/methods/06-JVOpen.md`(蓄積系)、`07-JVRTOpen.md`(速報系)を参照。
完全なレコード対応は `references/spec/jv-data-spec/data-types.md` が正本。

## option × 指定可能な dataspec(蓄積系)

| option | 指定可能な dataspec |
|---|---|
| 1 | TOKU, RACE, DIFF, BLOD, SNAP, SLOP, WOOD, YSCH, HOSE, HOYU, DIFN, BLDN, SNPN, HOSN |
| 2 | TOKU, RACE, TCOV, RCOV, SNAP, TCVN, RCVN, SNPN |
| 3, 4 | TOKU, RACE, DIFF, BLOD, SNAP, SLOP, WOOD, YSCH, HOSE, HOYU, COMM, MING, DIFN, BLDN, SNPN, HOSN |

> **N 付き(DIFN/BLDN/SNPN/HOSN/TCVN/RCVN)** は 2023/8/8 以降提供の、繁殖登録番号・生産者コード/名の
> サイズ拡張に対応したデータ。新規実装では N 付きを使うのが基本。

## 蓄積系 dataspec → 含まれるレコード

`JVOpen` で取得する過去・蓄積データ。

| dataspec | 名称 | 含まれるレコード(ID) |
|---|---|---|
| TOKU | 特別登録馬情報 | TK |
| RACE | レース情報 | RA, SE, HR, H1, H6, O1, O2, O3, O4, O5, O6, WF, JG |
| DIFF / DIFN | 蓄積系ソフト用 蓄積情報 | UM, KS, CH, BR, BN, RC, RA(地方/海外), SE(地方/海外) |
| BLOD / BLDN | 血統情報 | HN, SK, BT |
| MING | マイニング情報 | DM, TM |
| SNAP / SNPN | 出走時点情報 | CK |
| SLOP | 坂路調教情報 | HC |
| WOOD | ウッドチップ調教情報 | WC |
| YSCH | 開催スケジュール | YS |
| HOSE / HOSN | 競走馬市場取引価格情報 | HS |
| HOYU | 馬名の意味由来情報 | HY |
| COMM | 各種解説情報 | CS(コース情報) ほか |
| TCOV / TCVN | 非蓄積系ソフト用 補てん情報(特別登録馬補てん) | UM, CH, BR, BN, RC, RA, SE |
| RCOV / RCVN | 非蓄積系ソフト用 補てん情報(レース情報補てん) | UM, KS, CH, BR, BN, RC, RA, SE |

## 速報系 dataspec(0Bxx) → 含まれるレコード

`JVRTOpen` で取得する当日・速報データ。option は不要(キーで対象レース等を指定)。

| dataspec | 名称 | 含まれるレコード(ID) |
|---|---|---|
| 0B12 | 速報レース情報(成績確定後) | RA, SE, HR |
| 0B15 | 速報レース情報(出走馬名表～) | RA, SE, HR |
| 0B30 | 速報オッズ(全賭式) | O1, O2, O3, O4, O5, O6 |
| 0B31 | 速報オッズ(単複枠) | O1 |
| 0B32 | 速報オッズ(馬連) | O2 |
| 0B33 | 速報オッズ(ワイド) | O3 |
| 0B34 | 速報オッズ(馬単) | O4 |
| 0B35 | 速報オッズ(3連複) | O5 |
| 0B36 | 速報オッズ(3連単) | O6 |
| 0B20 | 速報票数(全賭式) | H1, H6 |
| 0B11 | 速報馬体重 | WH |
| 0B14 | 速報開催情報(一括) | WE, AV, JC, TC, CC |
| 0B16 | 速報開催情報(指定) | WE, AV, JC, TC, CC |
| 0B13 | 速報タイム型データマイニング予想 | DM |
| 0B17 | 速報対戦型データマイニング予想 | TM |
| 0B41 | 時系列オッズ(単複枠) | O1 |
| 0B42 | 時系列オッズ(馬連) | O2 |
| 0B51 | 速報重勝式(WIN5) | WF |

## 取得 API の使い分け

| 用途 | API | 例 |
|---|---|---|
| 過去・蓄積データ、セットアップ、差分更新 | `JVOpen`(dataspec + fromtime + option) | 全レース履歴のセットアップ、週次の差分取込 |
| 当日の速報(オッズ・馬体重・開催変更など) | `JVRTOpen`(dataspec + key) | レース当日のオッズ・馬体重の取得 |
| 確定/変更の発生通知(イベント駆動) | `JVWatchEvent` / `JVWatchEventClose` | 速報の発生をプッシュで受ける |

- `JVOpen` の `fromtime` は前回取得位置(`lastfiletimestamp` / `m_CurrentFileTimestamp`)を保存して次回に渡すと
  差分取得・再開ができる(`references/spec/jvlink-interface/methods/06-JVOpen.md` 参照)。
- セットアップ系(TOKU/DIFF/HOSE/HOYU/COMM 等)は読み出し終了ポイント時刻を指定できない(指定すると -1)。
- 速報専用レコード(WH/WE/AV/JC/TC/CC)は蓄積系には含まれないため、`JVRTOpen`(0B11/0B14/0B16)または
  `JVWatchEvent` で取得する。
