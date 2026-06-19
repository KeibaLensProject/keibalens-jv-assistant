# レコード早見表 (record-index)

全 38 レコード種別の統合インデックス。レコード種別ID から、フォーマット定義・C# 構造体・主な dataspec を一度に引ける。
- **フォーマット** = 項目の位置/バイト数/初期値/意味の正本(`references/spec/jv-data-spec/record-formats/`)。
- **構造体** = C# サンプル(`references/spec/jvdata-struct/`、2009 年版・項目サイズは要確認)。
- **主な dataspec** = JVOpen/JVRTOpen に渡すデータ種別ID。詳細は [dataspec-option.md](./dataspec-option.md)。

本文中のパスはスキル直下からの相対(`references/spec/...`)。下表のリンクはこのファイル(references/)からの相対(`spec/...`)。

| ID | 名称 | 長(byte) | 主な dataspec | フォーマット | C# 構造体ファイル | 主な構造体 |
|---|---|---|---|---|---|---|
| TK | 特別登録馬 | 21657 | TOKU | [record-formats/001-TK-特別登録馬.md](spec/jv-data-spec/record-formats/001-TK-特別登録馬.md) | [jvdata-struct/01-特別登録馬.md](spec/jvdata-struct/01-特別登録馬.md) | `JV_TK_TOKUUMA` |
| RA | レース詳細 | 1272 | RACE | [002-RA-レース詳細.md](spec/jv-data-spec/record-formats/002-RA-レース詳細.md) | [02-レース詳細.md](spec/jvdata-struct/02-レース詳細.md) | `JV_RA_RACE` |
| SE | 馬毎レース情報 | 555 | RACE | [003-SE-馬毎レース情報.md](spec/jv-data-spec/record-formats/003-SE-馬毎レース情報.md) | [03-馬毎レース情報.md](spec/jvdata-struct/03-馬毎レース情報.md) | `JV_SE_RACE_UMA` |
| HR | 払戻 | 719 | RACE | [004-HR-払戻.md](spec/jv-data-spec/record-formats/004-HR-払戻.md) | [04-払戻.md](spec/jvdata-struct/04-払戻.md) | `JV_HR_PAY` |
| H1 | 票数1(3連単以外) | 28955 | RACE / 0B20 | [005-H1-票数１.md](spec/jv-data-spec/record-formats/005-H1-票数１.md) | [05-票数(全掛式).md](spec/jvdata-struct/05-票数(全掛式).md) | `JV_H1_HYOSU_ZENKAKE` |
| H6 | 票数6(3連単) | 102890 | RACE / 0B20 | [006-H6-票数6(3連単).md](spec/jv-data-spec/record-formats/006-H6-票数6(3連単).md) | [05-票数(全掛式).md](spec/jvdata-struct/05-票数(全掛式).md) | `JV_H6_HYOSU_SANRENTAN` |
| O1 | オッズ1(単複枠) | 962 | RACE / 0B30 / 0B31 / 0B41 | [007-O1-オッズ1(単複枠).md](spec/jv-data-spec/record-formats/007-O1-オッズ1(単複枠).md) | [06-オッズ(単複枠).md](spec/jvdata-struct/06-オッズ(単複枠).md) | `JV_O1_ODDS_TANFUKUWAKU` |
| O2 | オッズ2(馬連) | 2042 | RACE / 0B30 / 0B32 / 0B42 | [008-O2-オッズ2(馬連).md](spec/jv-data-spec/record-formats/008-O2-オッズ2(馬連).md) | [07-オッズ(馬連).md](spec/jvdata-struct/07-オッズ(馬連).md) | `JV_O2_ODDS_UMAREN` |
| O3 | オッズ3(ワイド) | 2654 | RACE / 0B30 / 0B33 | [009-O3-オッズ3(ワイド).md](spec/jv-data-spec/record-formats/009-O3-オッズ3(ワイド).md) | [08-オッズ(ワイド).md](spec/jvdata-struct/08-オッズ(ワイド).md) | `JV_O3_ODDS_WIDE` |
| O4 | オッズ4(馬単) | 4031 | RACE / 0B30 / 0B34 | [010-O4-オッズ4(馬単).md](spec/jv-data-spec/record-formats/010-O4-オッズ4(馬単).md) | [09-オッズ(馬単).md](spec/jvdata-struct/09-オッズ(馬単).md) | `JV_O4_ODDS_UMATAN` |
| O5 | オッズ5(3連複) | 12293 | RACE / 0B30 / 0B35 | [011-O5-オッズ5(3連複).md](spec/jv-data-spec/record-formats/011-O5-オッズ5(3連複).md) | [10-オッズ(3連複).md](spec/jvdata-struct/10-オッズ(3連複).md) | `JV_O5_ODDS_SANREN` |
| O6 | オッズ6(3連単) | 83285 | RACE / 0B30 / 0B36 | [012-O6-オッズ6(3連単).md](spec/jv-data-spec/record-formats/012-O6-オッズ6(3連単).md) | [11-オッズ(3連単).md](spec/jvdata-struct/11-オッズ(3連単).md) | `JV_O6_ODDS_SANRENTAN` |
| UM | 競走馬マスタ | 1609 | DIFF/DIFN (補: TCOV/RCOV) | [013-UM-競走馬マスタ.md](spec/jv-data-spec/record-formats/013-UM-競走馬マスタ.md) | [12-競走馬マスタ.md](spec/jvdata-struct/12-競走馬マスタ.md) | `JV_UM_UMA` |
| KS | 騎手マスタ | 4173 | DIFF/DIFN (補: RCOV) | [014-KS-騎手マスタ.md](spec/jv-data-spec/record-formats/014-KS-騎手マスタ.md) | [13-騎手マスタ.md](spec/jvdata-struct/13-騎手マスタ.md) | `JV_KS_KISYU` |
| CH | 調教師マスタ | 3862 | DIFF/DIFN (補: TCOV/RCOV) | [015-CH-調教師マスタ.md](spec/jv-data-spec/record-formats/015-CH-調教師マスタ.md) | [14-調教師マスタ.md](spec/jvdata-struct/14-調教師マスタ.md) | `JV_CH_CHOKYOSI` |
| BR | 生産者マスタ | 545 | DIFF/DIFN (補: TCOV/RCOV) | [016-BR-生産者マスタ.md](spec/jv-data-spec/record-formats/016-BR-生産者マスタ.md) | [15-生産者マスタ.md](spec/jvdata-struct/15-生産者マスタ.md) | `JV_BR_BREEDER` |
| BN | 馬主マスタ | 477 | DIFF/DIFN (補: TCOV/RCOV) | [017-BN-馬主マスタ.md](spec/jv-data-spec/record-formats/017-BN-馬主マスタ.md) | [16-馬主マスタ.md](spec/jvdata-struct/16-馬主マスタ.md) | `JV_BN_BANUSI` |
| HN | 繁殖馬マスタ | 251 | BLOD/BLDN | [018-HN-繁殖馬マスタ.md](spec/jv-data-spec/record-formats/018-HN-繁殖馬マスタ.md) | [17-繁殖馬マスタ.md](spec/jvdata-struct/17-繁殖馬マスタ.md) | `JV_HN_HANSYOKU` |
| SK | 産駒マスタ | 208 | BLOD/BLDN | [019-SK-産駒マスタ.md](spec/jv-data-spec/record-formats/019-SK-産駒マスタ.md) | [18-産駒マスタ.md](spec/jvdata-struct/18-産駒マスタ.md) | `JV_SK_SANKU` |
| CK | 出走別着度数 | 6870 | SNAP/SNPN | [020-CK-出走別着度数.md](spec/jv-data-spec/record-formats/020-CK-出走別着度数.md) | [31-出走別着度数.md](spec/jvdata-struct/31-出走別着度数.md) | `JV_CK_UMA` ほか |
| RC | レコードマスタ | 501 | DIFF/DIFN (補: TCOV/RCOV) | [021-RC-レコードマスタ.md](spec/jv-data-spec/record-formats/021-RC-レコードマスタ.md) | [19-レコードマスタ.md](spec/jvdata-struct/19-レコードマスタ.md) | `JV_RC_RECORD` |
| HC | 坂路調教 | 60 | SLOP | [022-HC-坂路調教.md](spec/jv-data-spec/record-formats/022-HC-坂路調教.md) | [20-坂路調教.md](spec/jvdata-struct/20-坂路調教.md) | `JV_HC_HANRO` |
| HS | 競走馬市場取引価格 | 200 | HOSE/HOSN | [023-HS-競走馬市場取引価格.md](spec/jv-data-spec/record-formats/023-HS-競走馬市場取引価格.md) | [29-競走馬市場取引価格.md](spec/jvdata-struct/29-競走馬市場取引価格.md) | `JV_HS_SALE` |
| HY | 馬名の意味由来 | 123 | HOYU | [024-HY-馬名の意味由来.md](spec/jv-data-spec/record-formats/024-HY-馬名の意味由来.md) | [30-馬名の意味由来.md](spec/jvdata-struct/30-馬名の意味由来.md) | `JV_HY_BAMEIORIGIN` |
| YS | 開催スケジュール | 382 | YSCH | [025-YS-開催スケジュール.md](spec/jv-data-spec/record-formats/025-YS-開催スケジュール.md) | [28-開催スケジュール.md](spec/jvdata-struct/28-開催スケジュール.md) | `JV_YS_SCHEDULE` |
| BT | 系統情報 | 6889 | BLOD/BLDN | [026-BT-系統情報.md](spec/jv-data-spec/record-formats/026-BT-系統情報.md) | [32-系統情報.md](spec/jvdata-struct/32-系統情報.md) | `JV_BT_KEITO` |
| CS | コース情報 | 6829 | COMM | [027-CS-コース情報.md](spec/jv-data-spec/record-formats/027-CS-コース情報.md) | [33-コース情報.md](spec/jvdata-struct/33-コース情報.md) | `JV_CS_COURSE` |
| DM | タイム型データマイニング予想 | 303 | MING / 0B13 | [028-DM-タイム型データマイニング予想.md](spec/jv-data-spec/record-formats/028-DM-タイム型データマイニング予想.md) | [27-データマイニング予想.md](spec/jvdata-struct/27-データマイニング予想.md) | `JV_DM_INFO` |
| TM | 対戦型データマイニング予想 | 141 | MING / 0B17 | [029-TM-対戦型データマイニング予想.md](spec/jv-data-spec/record-formats/029-TM-対戦型データマイニング予想.md) | [34-対戦型データマイニング予想.md](spec/jvdata-struct/34-対戦型データマイニング予想.md) | `JV_TM_INFO` |
| WF | 重勝式(WIN5) | 7215 | RACE / 0B51 | [030-WF-重勝式(WIN5).md](spec/jv-data-spec/record-formats/030-WF-重勝式(WIN5).md) | [35-重勝式(WIN5).md](spec/jvdata-struct/35-重勝式(WIN5).md) | `JV_WF_INFO` |
| JG | 競走馬除外情報 | 80 | RACE | [031-JG-競走馬除外情報.md](spec/jv-data-spec/record-formats/031-JG-競走馬除外情報.md) | [36-競走馬除外情報.md](spec/jvdata-struct/36-競走馬除外情報.md) | `JV_JG_JOGAIBA` |
| WC | ウッドチップ調教 | 105 | WOOD | [032-WC-ウッドチップ調教.md](spec/jv-data-spec/record-formats/032-WC-ウッドチップ調教.md) | [37-ウッドチップ調教.md](spec/jvdata-struct/37-ウッドチップ調教.md) | `JV_WC_WOOD` |
| WH | 馬体重 | 847 | 0B11(速報のみ) | [101-WH-馬体重.md](spec/jv-data-spec/record-formats/101-WH-馬体重.md) | [21-馬体重.md](spec/jvdata-struct/21-馬体重.md) | `JV_WH_BATAIJYU` |
| WE | 天候馬場状態 | 42 | 0B14 / 0B16(速報のみ) | [102-WE-天候馬場状態.md](spec/jv-data-spec/record-formats/102-WE-天候馬場状態.md) | [22-天候馬場状態.md](spec/jvdata-struct/22-天候馬場状態.md) | `JV_WE_WEATHER` |
| AV | 出走取消・競走除外 | 78 | 0B14 / 0B16(速報のみ) | [103-AV-出走取消・競走除外.md](spec/jv-data-spec/record-formats/103-AV-出走取消・競走除外.md) | [23-出走取消・競走除外.md](spec/jvdata-struct/23-出走取消・競走除外.md) | `JV_AV_INFO` |
| JC | 騎手変更 | 161 | 0B14 / 0B16(速報のみ) | [104-JC-騎手変更.md](spec/jv-data-spec/record-formats/104-JC-騎手変更.md) | [24-騎手変更.md](spec/jvdata-struct/24-騎手変更.md) | `JV_JC_INFO` |
| TC | 発走時刻変更 | 45 | 0B14 / 0B16(速報のみ) | [105-TC-発走時刻変更.md](spec/jv-data-spec/record-formats/105-TC-発走時刻変更.md) | [25-発走時刻変更.md](spec/jvdata-struct/25-発走時刻変更.md) | `JV_TC_INFO` |
| CC | コース変更 | 50 | 0B14 / 0B16(速報のみ) | [106-CC-コース変更.md](spec/jv-data-spec/record-formats/106-CC-コース変更.md) | [26-コース変更.md](spec/jvdata-struct/26-コース変更.md) | `JV_CC_INFO` |

## 補足

- **dataspec 列**は代表的なものを示す。同じレコードが複数の dataspec(蓄積=DIFF/BLOD/SNAP… と補てん=TCOV/RCOV、
  速報=0Bxx)で提供されることがある。完全な対応は [dataspec-option.md](./dataspec-option.md) を参照。
- **WH/WE/AV/JC/TC/CC** は蓄積系 dataspec を持たない**速報専用**レコード。`JVRTOpen`(0B11/0B14/0B16)または
  `JVWatchEvent` で取得する。`JVOpen` では取得できない。
- **H1/H6** は同じ構造体ファイル `05-票数(全掛式).md` に `JV_H1_HYOSU_ZENKAKE` と
  `JV_H6_HYOSU_SANRENTAN` の 2 つが定義されている。
- **CK(出走別着度数)** は 1 レコード内に複数種の構造体(`JV_CK_UMA`/`JV_CK_KISYU`/`JV_CK_CHOKYOSI`/
  `JV_CK_BANUSI`/`JV_CK_BREEDER` など)を含む。詳細は構造体ファイルを参照。
