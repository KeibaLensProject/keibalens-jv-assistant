# JV-Data Python 構造体定義 (`JVData_Struct.py`)

出典: `context/JVData_Struct.py` (JRA-VAN提供サンプル, 最終更新 2026-07-31, SDK Ver.5.0.0)

JRA-VAN Data Lab. SDK Ver.5.0.0 (64bit版) に収録されている Python 版 JV-Data 構造体サンプルを領域ごとに Markdown 化したものです。
Python (`@dataclass` + `SetDataB(b: bytes)`) での JV-Data パース実装にそのまま利用でき、**2026年7月31日更新のため最新の JV-Data 仕様書 (4.9.0.1) のバイト位置・サイズに完全準拠**しています。

> 💡 C# 版構造体サンプル (`../jvdata-struct/`) は 2009 年版のため、2023 年の N付きデータ種別拡張（繁殖登録番号 8→10 バイト、生産者コード 6→8 バイト、生産者名 70→72 バイト）や 2021 年のウッドチップ調教 10 ハロン拡張が未反映ですが、**本 Python 版はすべて最新仕様 (4.9.0.1) に更新済み**です。C# で最新オフセットを実装する際の参照コードとしても活用できます。

## バイト切り出しヘルパ (`MidB2S` / `MidB2B`)

Shift_JIS バイト列 (`bytes`) から 1 始まりの位置とバイト長で項目を切り出す共通関数です。

```python
def MidB2S(b: bytes, start: int, length: int) -> str:
    """
    文字列をバイト長で切出し
    
    :param b: 文字列
    :type b: bytes
    :param start: 開始位置
    :type start: int
    :param length: バイト長
    :type length: int
    :return: 文字列
    :rtype: str
    """
    # 文字を任意に切出す
    return b[start-1:start-1+length].decode("shift_jis", errors="ignore")

def MidB2B(b: bytes, start: int, length: int) -> bytes:
    """
    バイト配列をバイト長で切出し
    
    :param b: 文字列
    :type b: bytes
    :param start: 開始位置
    :type start: int
    :param length: バイト長
    :type length: int
    :return: 文字列
    :rtype: bytes
    """
    # 文字列バイト任意切り出し
    return b[start-1:start-1+length]
```

## 構造体ファイル一覧

- [共通構造体](./common-structs.md)

| 仕様書No | レコード | ファイル | 主なクラス |
|---|---|---|---|
| 1 | 特別登録馬 | [01-特別登録馬.md](./01-特別登録馬.md) | `TOKUUMA_INFO`, `JV_TK_TOKUUMA` |
| 2 | レース詳細 | [02-レース詳細.md](./02-レース詳細.md) | `CORNER_INFO`, `JV_RA_RACE` |
| 3 | 馬毎レース情報 | [03-馬毎レース情報.md](./03-馬毎レース情報.md) | `CHAKUUMA_INFO`, `JV_SE_RACE_UMA` |
| 4 | 払戻 | [04-払戻.md](./04-払戻.md) | `PAY_INFO1`, `PAY_INFO2`, `PAY_INFO3`, `PAY_INFO4`… |
| 5.6 | 票数(全掛式、三連単) | [05-票数(全掛式、三連単).md](./05-票数(全掛式、三連単).md) | `HYO_INFO1`, `HYO_INFO2`, `HYO_INFO3`, `HYO_INFO4`… |
| 7 | オッズ(単複枠) | [06-オッズ(単複枠).md](./06-オッズ(単複枠).md) | `ODDS_TANSYO_INFO`, `ODDS_FUKUSYO_INFO`, `ODDS_WAKUREN_INFO`, `JV_O1_ODDS_TANFUKUWAKU` |
| 8 | オッズ(馬連) | [07-オッズ(馬連).md](./07-オッズ(馬連).md) | `ODDS_UMAREN_INFO`, `JV_O2_ODDS_UMAREN` |
| 9 | オッズ(ワイド) | [08-オッズ(ワイド).md](./08-オッズ(ワイド).md) | `ODDS_WIDE_INFO`, `JV_O3_ODDS_WIDE` |
| 10 | オッズ(馬単) | [09-オッズ(馬単).md](./09-オッズ(馬単).md) | `ODDS_UMATAN_INFO`, `JV_O4_ODDS_UMATAN` |
| 11 | オッズ(3連複) | [10-オッズ(3連複).md](./10-オッズ(3連複).md) | `ODDS_SANREN_INFO`, `JV_O5_ODDS_SANREN` |
| 12 | オッズ(3連単) | [11-オッズ(3連単).md](./11-オッズ(3連単).md) | `ODDS_SANRENTAN_INFO`, `JV_O6_ODDS_SANRENTAN` |
| 13 | 競走馬マスタ | [12-競走馬マスタ.md](./12-競走馬マスタ.md) | `KETTO3_INFO`, `JV_UM_UMA` |
| 14 | 騎手マスタ | [13-騎手マスタ.md](./13-騎手マスタ.md) | `HATUKIJYO_INFO`, `HATUSYORI_INFO`, `JV_KS_KISYU` |
| 15 | 調教師マスタ | [14-調教師マスタ.md](./14-調教師マスタ.md) | `JV_CH_CHOKYOSI` |
| 16 | 生産者マスタ | [15-生産者マスタ.md](./15-生産者マスタ.md) | `JV_BR_BREEDER` |
| 17 | 馬主マスタ | [16-馬主マスタ.md](./16-馬主マスタ.md) | `JV_BN_BANUSI` |
| 18 | 繁殖馬マスタ | [17-繁殖馬マスタ.md](./17-繁殖馬マスタ.md) | `JV_HN_HANSYOKU` |
| 19 | 産駒マスタ | [18-産駒マスタ.md](./18-産駒マスタ.md) | `JV_SK_SANKU` |
| 20 | 出走別着度数 | [19-出走別着度数.md](./19-出走別着度数.md) | `JV_CK_UMA`, `JV_CK_HON_RUIKEISEI_INFO`, `JV_CK_KISYU`, `JV_CK_CHOKYOSI`… |
| 21 | レコードマスタ | [20-レコードマスタ.md](./20-レコードマスタ.md) | `RECUMA_INFO`, `JV_RC_RECORD` |
| 22 | 坂路調教 | [21-坂路調教.md](./21-坂路調教.md) | `JV_HC_HANRO` |
| 23 | 競走馬市場取引価格 | [22-競走馬市場取引価格.md](./22-競走馬市場取引価格.md) | `JV_HS_SALE` |
| 24 | 馬名の意味由来 | [23-馬名の意味由来.md](./23-馬名の意味由来.md) | `JV_HY_BAMEIORIGIN` |
| 25 | 開催スケジュール | [24-開催スケジュール.md](./24-開催スケジュール.md) | `JYUSYO_INFO`, `JV_YS_SCHEDULE` |
| 26 | 系統情報 | [25-系統情報.md](./25-系統情報.md) | `JV_BT_KEITO` |
| 27 | コース情報 | [26-コース情報.md](./26-コース情報.md) | `JV_CS_COURSE` |
| 28 | タイム型データマイニング予想 | [27-タイム型データマイニング予想.md](./27-タイム型データマイニング予想.md) | `DM_INFO`, `JV_DM_INFO` |
| 29 | 対戦型データマイニング予想 | [28-対戦型データマイニング予想.md](./28-対戦型データマイニング予想.md) | `TM_INFO`, `JV_TM_INFO` |
| 30 | 重勝式(WIN5) | [29-重勝式(WIN5).md](./29-重勝式(WIN5).md) | `WF_RACE_INFO`, `WF_YUKO_HYO_INFO`, `WF_PAY_INFO`, `JV_WF_INFO` |
| 31 | 競走馬除外情報 | [30-競走馬除外情報.md](./30-競走馬除外情報.md) | `JV_JG_JOGAIBA` |
| 32 | ウッドチップ調教 | [31-ウッドチップ調教.md](./31-ウッドチップ調教.md) | `JV_WC_WOOD` |
| 101 | 馬体重 | [32-馬体重.md](./32-馬体重.md) | `BATAIJYU_INFO`, `JV_WH_BATAIJYU` |
| 102 | 天候馬場状態 | [33-天候馬場状態.md](./33-天候馬場状態.md) | `JV_WE_WEATHER` |
| 103 | 出走取消・競走除外 | [34-出走取消・競走除外.md](./34-出走取消・競走除外.md) | `JV_AV_INFO` |
| 104 | 騎手変更 | [35-騎手変更.md](./35-騎手変更.md) | `JC_INFO`, `JV_JC_INFO` |
| 105 | 発走時刻変更 | [36-発走時刻変更.md](./36-発走時刻変更.md) | `TC_INFO`, `JV_TC_INFO` |
| 106 | コース変更 | [37-コース変更.md](./37-コース変更.md) | `CC_INFO`, `JV_CC_INFO` |
