# JV-Data C# 構造体定義

出典: `context/JVData_Struct.cs` (JRA-VAN提供サンプル, 最終更新 2009-12-08)

JRA-VAN が提供する C# 版 JV-Data 構造体サンプルを領域ごとに Markdown 化したものです。
C# プロジェクトでの JV-Data パース実装の参照に利用できます。

> 注: このサンプルは **2009年版** のため、最新の JV-Data仕様書(4.9.0.1)で追加されたレコード・項目は含まれません。フィールドの正確な位置/バイト数は [レコードフォーマット](../jv-data-spec/record-formats/README.md) を正とします。

## バイト切り出しヘルパ

Shift_JIS バイト列から項目を切り出す共通メソッドです。

```csharp
    /// <summary>
    /// 文字列をバイト長で切出し

    /// </summary>
    /// <param name="myByte">文字列</param>
    /// <param name="bSt">開始位置</param>
    /// <param name="bLen">バイト長</param>
    /// <returns>文字列</returns>
    public static string MidB2S(ref byte[] myByte, int bSt, int bLen)
    {
        // 文字を任意に切出す

        return Encoding.GetEncoding("Shift_JIS").GetString(myByte, bSt - 1, bLen);
    }

    /// <summary>
    /// バイト配列をバイト長で切出し

    /// </summary>
    /// <param name="myByte">文字列</param>
    /// <param name="bSt">開始位置</param>
    /// <param name="bLen">バイト長</param>
    /// <returns>文字列</returns>
    public static byte[] MidB2B(ref byte[] myByte, int bSt, int bLen)
    {
        byte[] cBt = new byte[bLen];
        int j = 0;

        // 文字列バイト任意切り出し

        for (int i = bSt - 1; i < bSt - 1 + bLen; i++)
        {
            cBt[j] = myByte[i];
            j++;
        }

        return cBt;
    }

    /// <summary>
    /// 文字列をバイト配列に変換
    /// </summary>
    /// <param name="myString">文字列</param>
    /// <returns>バイト配列</returns>
    public static byte[] Str2Byte(ref string myString)
    {
        // Shift JISに変換する
        return Encoding.GetEncoding("Shift_JIS").GetBytes(myString);
    }
```

## 構造体ファイル一覧

- [共通構造体](./common-structs.md)

| No | レコード | ファイル | 主な構造体 |
|---|---|---|---|
| 1 | 特別登録馬 | [01-特別登録馬.md](./01-特別登録馬.md) | `TOKUUMA_INFO`, `JV_TK_TOKUUMA` |
| 2 | レース詳細 | [02-レース詳細.md](./02-レース詳細.md) | `CORNER_INFO`, `JV_RA_RACE` |
| 3 | 馬毎レース情報 | [03-馬毎レース情報.md](./03-馬毎レース情報.md) | `CHAKUUMA_INFO`, `JV_SE_RACE_UMA` |
| 4 | 払戻 | [04-払戻.md](./04-払戻.md) | `PAY_INFO1`, `PAY_INFO2`, `PAY_INFO3`, `PAY_INFO4`… |
| 5 | 票数(全掛式) | [05-票数(全掛式).md](./05-票数(全掛式).md) | `HYO_INFO1`, `HYO_INFO2`, `HYO_INFO3`, `HYO_INFO4`… |
| 6 | オッズ(単複枠) | [06-オッズ(単複枠).md](./06-オッズ(単複枠).md) | `ODDS_TANSYO_INFO`, `ODDS_FUKUSYO_INFO`, `ODDS_WAKUREN_INFO`, `JV_O1_ODDS_TANFUKUWAKU` |
| 7 | オッズ(馬連) | [07-オッズ(馬連).md](./07-オッズ(馬連).md) | `ODDS_UMAREN_INFO`, `JV_O2_ODDS_UMAREN` |
| 8 | オッズ(ワイド) | [08-オッズ(ワイド).md](./08-オッズ(ワイド).md) | `ODDS_WIDE_INFO`, `JV_O3_ODDS_WIDE` |
| 9 | オッズ(馬単) | [09-オッズ(馬単).md](./09-オッズ(馬単).md) | `ODDS_UMATAN_INFO`, `JV_O4_ODDS_UMATAN` |
| 10 | オッズ(3連複) | [10-オッズ(3連複).md](./10-オッズ(3連複).md) | `ODDS_SANREN_INFO`, `JV_O5_ODDS_SANREN` |
| 10-1 | オッズ(3連単) | [11-オッズ(3連単).md](./11-オッズ(3連単).md) | `ODDS_SANRENTAN_INFO`, `JV_O6_ODDS_SANRENTAN` |
| 11 | 競走馬マスタ | [12-競走馬マスタ.md](./12-競走馬マスタ.md) | `KETTO3_INFO`, `JV_UM_UMA` |
| 12 | 騎手マスタ | [13-騎手マスタ.md](./13-騎手マスタ.md) | `HATUKIJYO_INFO`, `HATUSYORI_INFO`, `JV_KS_KISYU` |
| 13 | 調教師マスタ | [14-調教師マスタ.md](./14-調教師マスタ.md) | `JV_CH_CHOKYOSI` |
| 14 | 生産者マスタ | [15-生産者マスタ.md](./15-生産者マスタ.md) | `JV_BR_BREEDER` |
| 15 | 馬主マスタ | [16-馬主マスタ.md](./16-馬主マスタ.md) | `JV_BN_BANUSI` |
| 16 | 繁殖馬マスタ | [17-繁殖馬マスタ.md](./17-繁殖馬マスタ.md) | `JV_HN_HANSYOKU` |
| 17 | 産駒マスタ | [18-産駒マスタ.md](./18-産駒マスタ.md) | `JV_SK_SANKU` |
| 18 | レコードマスタ | [19-レコードマスタ.md](./19-レコードマスタ.md) | `RECUMA_INFO`, `JV_RC_RECORD` |
| 19 | 坂路調教 | [20-坂路調教.md](./20-坂路調教.md) | `JV_HC_HANRO` |
| 20 | 馬体重 | [21-馬体重.md](./21-馬体重.md) | `BATAIJYU_INFO`, `JV_WH_BATAIJYU` |
| 21 | 天候馬場状態 | [22-天候馬場状態.md](./22-天候馬場状態.md) | `JV_WE_WEATHER` |
| 22 | 出走取消・競走除外 | [23-出走取消・競走除外.md](./23-出走取消・競走除外.md) | `JV_AV_INFO` |
| 23 | 騎手変更 | [24-騎手変更.md](./24-騎手変更.md) | `JC_INFO`, `JV_JC_INFO` |
| 23-1 | 発走時刻変更 | [25-発走時刻変更.md](./25-発走時刻変更.md) | `TC_INFO`, `JV_TC_INFO` |
| 23-2 | コース変更 | [26-コース変更.md](./26-コース変更.md) | `CC_INFO`, `JV_CC_INFO` |
| 24 | データマイニング予想 | [27-データマイニング予想.md](./27-データマイニング予想.md) | `DM_INFO`, `JV_DM_INFO` |
| 25 | 開催スケジュール | [28-開催スケジュール.md](./28-開催スケジュール.md) | `JYUSYO_INFO`, `JV_YS_SCHEDULE` |
| 26 | 競走馬市場取引価格 | [29-競走馬市場取引価格.md](./29-競走馬市場取引価格.md) | `JV_HS_SALE` |
| 27 | 馬名の意味由来 | [30-馬名の意味由来.md](./30-馬名の意味由来.md) | `JV_HY_BAMEIORIGIN` |
| 28 | 出走別着度数 | [31-出走別着度数.md](./31-出走別着度数.md) | `JV_CK_UMA`, `JV_CK_HON_RUIKEISEI_INFO`, `JV_CK_KISYU`, `JV_CK_CHOKYOSI`… |
| 29 | 系統情報 | [32-系統情報.md](./32-系統情報.md) | `JV_BT_KEITO` |
| 30 | コース情報 | [33-コース情報.md](./33-コース情報.md) | `JV_CS_COURSE` |
| 31 | 対戦型データマイニング予想 | [34-対戦型データマイニング予想.md](./34-対戦型データマイニング予想.md) | `TM_INFO`, `JV_TM_INFO` |
| 32 | 重勝式(WIN5) | [35-重勝式(WIN5).md](./35-重勝式(WIN5).md) | `WF_RACE_INFO`, `WF_YUKO_HYO_INFO`, `WF_PAY_INFO`, `JV_WF_INFO` |
| 33 | 競走馬除外情報 | [36-競走馬除外情報.md](./36-競走馬除外情報.md) | `JV_JG_JOGAIBA` |
| 34 | ウッドチップ調教 | [37-ウッドチップ調教.md](./37-ウッドチップ調教.md) | `JV_WC_WOOD` |
