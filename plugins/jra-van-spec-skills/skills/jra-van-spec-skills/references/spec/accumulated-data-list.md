# 蓄積系提供データ一覧

出典: `context/蓄積系提供データ一覧.xls`

蓄積系データの データ種別 / レコード種別 / 区分ID / 保存ID と ファイル名パターンの対応表です。
ファイル名は `<レコード種別ID><区分ID><保存ID><作成日時>...<.jvd>` の形式です。
（データ種別ID・レコード種別は結合セルを前方補完しています）

| データ種別 | データ種別ID | レコード種別 | 種別ID | 区分 | 区分ID | 保存ID | 登録日 | 登録単位 | ファイル名 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|
| 特別登録馬 | TOKU | 特別登録馬 | TK | 最新分 | T | W | 日曜 | 当週＋翌週 | TKTWyyyymmddyyyymmddhhmmss.jvd | G1レースについては２週に渡って提供 |
| 特別登録馬 | TOKU | 特別登録馬 | TK | 最新分(ハンデあり） | H | W | 月曜 | 当週＋翌週 | TKHWyyyymmddyyyymmddhhmmss.jvd |  |
| 特別登録馬 | TOKU | 特別登録馬 | TK | 修正 | M | W | 随時 | 修正レコードのみ | TKMWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | TCOV<br>TCVN | 競走馬 | UM | 特別登録 | T | W | 月曜 | 特別登録馬に含まれる競走馬分 | UMTWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | TCOV<br>TCVN | 調教師 | CH | 登録馬分 | T | W | 月曜 | 特別登録馬に含まれる競走馬分 | CHTWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | TCOV<br>TCVN | 生産者 | BR | 特別登録 | T | W | 月曜 | 特別登録馬に含まれる競走馬分 | BRTWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | TCOV<br>TCVN | 馬主 | BN | 特別登録 | T | W | 月曜 | 特別登録馬に含まれる競走馬分 | BNTWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | TCOV<br>TCVN | レコード | RC | 該当レース分 | T | W | 月曜 |  | RCTWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | TCOV<br>TCVN | レース詳細 | RA | 特別登録　過去全走 | U | W | 月曜 |  | RAUWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | TCOV<br>TCVN | 馬毎レース情報 | SE | 特別登録　全走 | U | W | 月曜 |  | SEUWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | G1 | G | W | 木曜 | G1のみ | RAGWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | 出走馬名表 | P | W | 木曜 | １日全場 | RAPWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | 翌日分 | D | W | 金曜、土曜 | １日全場 | RADWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | 前売分 | B | W | 金曜 | 前売のみ | RABWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | 成績 | S | W | 月曜 | １日全場 | RASWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | 修正 | M | W | 随時 | 修正レコードのみ | RAMWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 馬毎レース情報 | SE | 出走馬名表　G1 | G | W | 木曜 | G1のみ | SEGWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 馬毎レース情報 | SE | 出走馬名表　出馬表 | P | W | 木曜 | １日全場 | SEPWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 馬毎レース情報 | SE | 翌日出走分　出馬表(前売含） | D | W | 金曜、土曜 | １日全場 | SEDWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 馬毎レース情報 | SE | 前売分 | B | W | 金曜 | 前売のみ | SEBWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 馬毎レース情報 | SE | 成績 | S | W | 月曜 | １日全場 | SESWyyyymmddyyyymmddhhmmss.jvd | 海外過去１５日分含む |
| レース情報 | RACE | 馬毎レース情報 | SE | 修正 | M | W | 随時 | 修正レコードのみ | SEMWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 払戻 | HR | 成績 | S | W | 月曜 | １日全場 | HRSWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 払戻 | HR | 修正 | M | W | 随時 | 修正レコードのみ | HRMWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 票数 | H1 | 成績 | S | W | 月曜 | １日全場 | H1SWyyyymmddyyyymmddhhmmss.jvd | H1（全賭式）のみ |
| レース情報 | RACE | 票数 | H1 | 修正 | M | W | 随時 | 修正レコードのみ | H1SMWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | オッズ | O1 | 成績 | S | W | 月曜 | １日全場 | O1SWyyyymmddyyyymmddhhmmss.jvd | O1（単複枠）からO6（３連単）まで |
| レース情報 | RACE | オッズ | O1 | 修正 | M | W | 随時 | 修正レコードのみ | O1MWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 重勝式 | WF | 成績 | S | W | 月曜 | 前週 | WFSWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 重勝式 | WF | 修正 | M | W | 随時 | 修正レコードのみ | WFMWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 競走馬除外情報 | JG | 出走馬名表<br>翌日出走分　出馬表(前売含） | D | W | 木曜<br>金曜、土曜 | １日全場 | JGDWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 競走馬除外情報 | JG | 修正 | M | W | 随時 | 修正レコードのみ | JGMWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | 競走馬 | UM | 出走馬名表 | P | W | 木曜 | 週 | UMPWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | 騎手 | KS | 全出走馬分 | P | W | 木曜 |  | KSPWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | 調教師 | CH | 全出走馬分 | P | W | 木曜 |  | CHPWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | 生産者 | BR | 出走馬名表 | P | W | 木曜 | 全件 | BRPWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | 馬主 | BN | 出走馬名表 | P | W | 木曜 | 全件 | BNPWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | レコード | RC | 該当レース分 | P | W | 月曜 |  | RCPWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | レース詳細 | RA | 出走馬名表　過去全走 | Q | W | 木曜 |  | RAQWyyyymmddyyyymmddhhmmss.jvd |  |
| 非蓄積系ソフト用<br>補てん情報 | RCOV<br>RCVN | 馬毎レース情報 | SE | 出走馬名表　全走 | Q | W | 木曜 | 週 | SEQWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 競走馬 | UM | 差分(土日成績反映含） | F | W | 月曜、木曜 |  | UMFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 競走馬 | UM | 修正 | O | W | 随時 | 修正レコードのみ | UMOWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 騎手 | KS | 差分 | F | W | 月曜、木曜 |  | KSFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 騎手 | KS | 修正 | O | W | 随時 | 修正レコードのみ | KSOWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 調教師 | CH | 差分 | F | W | 月曜、木曜 |  | CHFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 調教師 | CH | 修正 | O | W | 随時 | 修正レコードのみ | CHOWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 生産者 | BR | 差分 | F | W | 月曜、木曜 |  | BRFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 生産者 | BR | 修正 | O | W | 随時 | 修正レコードのみ | BROWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 馬主 | BN | 差分 | F | W | 月曜、木曜 |  | BNFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 馬主 | BN | 修正 | O | W | 随時 | 修正レコードのみ | BNOWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | レコード | RC | 差分 | F | W | 月曜 |  | RCFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | レコード | RC | 修正 | O | W | 随時 | 修正レコードのみ | RCOWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | レース詳細 | RA | 地方 | L | W | 月曜、木曜 | 週 | RALWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | レース詳細 | RA | 海外 | K | W | 月曜、木曜 | 週 | RAKWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | レース詳細 | RA | 修正 | O | W | 随時 | 修正レコードのみ | RAOWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 馬毎レース情報 | SE | 地方 | L | W | 月曜、木曜 | 週 | SELWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 馬毎レース情報 | SE | 海外 | K | W | 月曜、木曜 | 週 | SEKWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>蓄積情報 | DIFF<br>DIFN | 馬毎レース情報 | SE | 修正 | O | W | 随時 | 修正レコードのみ | SEOWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>血統情報 | BLOD<br>BLDN | 繁殖馬 | HN | 差分 | F | W | 月曜、木曜 |  | HNFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>血統情報 | BLOD<br>BLDN | 繁殖馬 | HN | 修正 | M | W | 随時 | 修正レコードのみ | HNMWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>血統情報 | BLOD<br>BLDN | 産駒 | SK | 差分 | F | W | 月曜、木曜 |  | SKFWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>血統情報 | BLOD<br>BLDN | 産駒 | SK | 修正 | M | W | 随時 | 修正レコードのみ | SKMWyyyymmddyyyymmddhhmmss.jvd |  |
| 蓄積系ソフト用<br>血統情報 | BLOD<br>BLDN | 系統情報 | BT | 差分 | F | W | 随時 |  | BTFWyyyymmddyyyymmddhhmmss.jvd | 修正データも差分として提供する |
| 坂路調教情報 | SLOP | 坂路調教 | HC | 当日分（美浦） | E | W | 毎日 | 当日分 | HCEWyyyymmddyyyymmddhhmmss.jvd |  |
| 坂路調教情報 | SLOP | 坂路調教 | HC | 当日分（栗東） | W | W | 毎日 | 当日分 | HCWWyyyymmddyyyymmddhhmmss.jvd |  |
| 坂路調教情報 | SLOP | 坂路調教 | HC | 修正 | M | W | 随時 | 修正レコードのみ | HCMWyyyymmddyyyymmddhhmmss.jvd |  |
| 開催スケジュール情報 | YSCH | 開催スケジュール | YS | 当年分 | N | W | 月曜 | 当年分 | YSNWyyyy9999yyyymmddhhmmss.jvd |  |
| 開催スケジュール情報 | YSCH | 開催スケジュール | YS | 修正 | M | W | 随時 | 修正レコードのみ | YSMWyyyy9999yyyymmddhhmmss.jvd |  |
| 競走馬市場取引価格情報 | HOSE | 競走馬市場取引価格情報 | HS | 差分 | F | W | 随時 |  | HSFWyyyymmddyyyymmddhhmmss.jvd | 月・木曜またはセリ終了時 |
| 出走時点情報 | SNAP<br>SNPN | 出走別着回数 | CK | 差分 | F | W | 木曜 | ２日全場 | CKFWyyyymmddyyyymmddhhmmss.jvd |  |
| 出走時点情報 | SNAP<br>SNPN | 出走別着回数 | CK | 変更分 | C | W | 月曜 | ２日全場 | CKCWyyyymmddyyyymmddhhmmss.jvd | 騎手変更分のみ |
| 出走時点情報 | SNAP<br>SNPN | 出走別着回数 | CK | 修正 | M | W | 随時 | 修正レコードのみ | CKMWyyyymmddyyyymmddhhmmss.jvd |  |
| 馬名の由来情報 | HOYU | 馬名の由来情報 | HY | 差分 | F | W | 火曜 |  | HYFWyyymmddyyyymmddhhmmss.jvd |  |
| 馬名の由来情報 | HOYU | 馬名の由来情報 | HY | 修正 | O | W | 随時 | 修正レコードのみ | HYOWyyyymmddyyyymmddhhmmss.jvd |  |
| 各種解説 | COMM | コース情報 | CS | 差分 | F | W | 随時 |  | CSFWyyyymmddyyyymmddhhmmss.jvd | 修正データも差分として提供する |
| マイニングデータ | MING | タイム型マイニングデータ | DM | 成績 | S | W | 月曜 | １日全場 | DMSWyyyymmddyyyymmddhhmmss.jvd |  |
| マイニングデータ | MING | 対戦型マイニングデータ | TM | 成績 | S | W | 月曜 | １日全場 | TMSWyyyymmddyyyymmddhhmmss.jvd |  |
| ウッドチップ調教情報 | WOOD | ウッドチップ調教 | WC | 当日分（美浦） | E | W | 毎日 | 当日分 | WCEWyyyymmddyyyymmddhhmmss.jvd |  |
| ウッドチップ調教情報 | WOOD | ウッドチップ調教 | WC | 当日分（栗東） | W | W | 毎日 | 当日分 | WCWWyyyymmddyyyymmddhhmmss.jvd |  |
| ウッドチップ調教情報 | WOOD | ウッドチップ調教 | WC | 修正 | M | W | 随時 | 修正レコードのみ | WCMWyyyymmddyyyymmddhhmmss.jvd |  |
| ウッドチップ調教情報 | WOOD | ウッドチップ調教 | WC | 修正 | O | W | 随時 | 修正レコードのみ | HSOWyyyymmddyyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | 月別 | V | M | 月次 | 月 | RAVMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | レース詳細 | RA | 修正 | M | M | 随時 | 修正レコードのみ | RAMMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 馬毎レース | SE | 月別 | V | M | 月次 | 月 | SEVMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 馬毎レース | SE | 修正 | M | M | 随時 | 修正レコードのみ | SEMMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 払戻 | HR | 月別 | V | M | 月次 | 月 | HRVMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 払戻 | HR | 修正 | M | M | 随時 | 修正レコードのみ | HRMMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 票数 | H1 | 月別 | V | M | 月次 | 月 | H1VMyyyymm99yyyymmddhhmmss.jvd | H1（全賭式）のみ |
| レース情報 | RACE | 票数 | H1 | 修正 | M | M | 随時 | 修正レコードのみ | H1MMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | オッズ | O1 | 月別 | V | M | 月次 | 月 | O1VMyyyymm99yyyymmddhhmmss.jvd | O1（単複枠）からO6（３連単）まで |
| レース情報 | RACE | オッズ | O1 | 修正 | M | M | 随時 | 修正レコードのみ | O1MMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 重勝式 | WF | 月別 | V | M | 月次 | 月 | WFVMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 重勝式 | WF | 修正 | M | M | 随時 | 修正レコードのみ | WFMMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 競走馬除外情報 | JG | 月別 | V | M | 月次 | 月 | JGVMyyyymm99yyyymmddhhmmss.jvd |  |
| レース情報 | RACE | 競走馬除外情報 | JG | 修正 | M | M | 随時 | 修正レコードのみ | JGMMyyyymm99yyyymmddhhmmss.jvd |  |
| 蓄積情報 | DIFF<br>DIFN | 競走馬 | UM | 全件マスター | X | M | 月次 | 全件 | UMXMyyyymm99yyyymmddhhmmss.jvd |  |
| 蓄積情報 | DIFF<br>DIFN | 騎手 | KS | 全件マスター | X | M | 月次 | 全件 | KSXMyyyymm99yyyymmddhhmmss.jvd |  |
| 蓄積情報 | DIFF<br>DIFN | 調教師 | CH | 全件マスター | X | M | 月次 | 全件 | CHXMyyyymm99yyyymmddhhmmss.jvd |  |
| 蓄積情報 | DIFF<br>DIFN | 生産者 | BR | 全件マスター | X | M | 月次 | 全件 | BRXMyyyymm99yyyymmddhhmmss.jvd |  |
| 蓄積情報 | DIFF<br>DIFN | 馬主 | BN | 全件マスター | X | M | 月次 | 全件 | BNXMyyyymm99yyyymmddhhmmss.jvd |  |
| 蓄積情報 | DIFF<br>DIFN | レコード | RC | 全件マスター | X | M | 月次 | 全件 | RCXMyyyymm99yyyymmddhhmmss.jvd |  |
| 血統情報 | BLOD<br>BLDN | 繁殖馬 | HN | 月別 | V | M | 月次 | 月 | HNVMyyyymm99yyyymmddhhmmss.jvd |  |
| 血統情報 | BLOD<br>BLDN | 繁殖馬 | HN | 修正 | M | M | 随時 | 修正レコードのみ | HNMMyyyymm99yyyymmddhhmmss.jvd |  |
| 血統情報 | BLOD<br>BLDN | 産駒 | SK | 月別 | V | M | 月次 | 月 | SKVMyyyymm99yyyymmddhhmmss.jvd |  |
| 血統情報 | BLOD<br>BLDN | 産駒 | SK | 修正 | M | M | 随時 | 修正レコードのみ | SKMMyyyymm99yyyymmddhhmmss.jvd |  |
| 血統情報 | BLOD<br>BLDN | 系統情報 | BT | 全件マスター | X | M | 月次 | 全件 | BTXMyyyymm99yyyymmddhhmmss.jvd |  |
| 坂路調教情報 | SLOP | 坂路調教 | HC | 月別 | V | M | 月次 | 月 | HCVMyyyymm99yyyymmddhhmmss.jvd |  |
| 坂路調教情報 | SLOP | 坂路調教 | HC | 修正 | M | M | 随時 | 修正レコードのみ | HCMMyyyymm99yyyymmddhhmmss.jvd |  |
| 開催スケジュール情報 | YSCH | 開催スケジュール | YS | 年別 | Y | M | 年次 | 当年分 | YSYMyyyy9999yyyymmddhhmmss.jvd |  |
| 開催スケジュール情報 | YSCH | 開催スケジュール | YS | 修正 | M | M | 随時 | 修正レコードのみ | YSMMyyyy9999yyyymmddhhmmss.jvd |  |
| 出走時点情報 | SNAP<br>SNPN | 出走別着回数 | CK | 月別 | V | M | 月次 | 月 | CKVMyyyymm99yyyymmddhhmmss.jvd |  |
| 出走時点情報 | SNAP<br>SNPN | 出走別着回数 | CK | 修正 | M | M | 随時 | 修正レコードのみ | CKMMyyyymm99yyyymmddhhmmss.jvd |  |
| 競走馬市場取引価格情報 | HOSE<br>HOSN | 競走馬市場取引価格情報 | HS | 全件マスター | X | M | 月次 | 月 | HSXMyyyymm99yyyymmddhhmmss.jvd |  |
| 馬名の由来情報 | HOYU | 馬名の由来情報 | HY | 全件マスター | X | M | 月次 | 月 | HYXMyyyymm99yyyymmddhhmmss.jvd |  |
| 各種解説 | COMM | コース情報 | CS | 全件マスター | X | M | 月次 | 全件 | CSXMyyyymm99yyyymmddhhmmss.jvd |  |
| マイニングデータ | MING | タイム型マイニングデータ | DM | 月別 | V | M | 月次 | 月 | DMVMyyyymmddyyyymmddhhmmss.jvd |  |
| マイニングデータ | MING | 対戦型マイニングデータ | TM | 月別 | V | M | 月次 | 月 | TMVMyyyymmddyyyymmddhhmmss.jvd |  |
| ウッドチップ調教情報 | WOOD | ウッドチップ調教 | WC | 月別 | V | M | 月次 | 月 | WCVMyyyymmddyyyymmddhhmmss.jvd |  |
| ウッドチップ調教情報 | WOOD | ウッドチップ調教 | WC | 修正 | M | M | 随時 | 修正レコードのみ | WCMMyyyymmddyyyymmddhhmmss.jvd |  |
