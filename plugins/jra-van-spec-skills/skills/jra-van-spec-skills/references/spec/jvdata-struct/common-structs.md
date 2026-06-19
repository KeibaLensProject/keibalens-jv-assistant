# 共通構造体

出典: `context/JVData_Struct.cs` (JRA-VAN提供サンプル, 最終更新 2009-12-08)

複数レコードで共有される構造体 (年月日・時分秒・着差など)。

定義: `YMD`, `HMS`, `HM`, `MDHM`, `RECORD_ID`, `RACE_ID`, `RACE_ID2`, `SEI_RUIKEI_INFO`, `SAIKIN_JYUSYO_INFO`, `HON_ZEN_RUIKEISEI_INFO`, `RACE_INFO`, `TENKO_BABA_INFO`, `CHAKUKAISU3_INFO`, `CHAKUKAISU4_INFO`, `CHAKUKAISU5_INFO`, `CHAKUKAISU6_INFO`, `RACE_JYOKEN`

```csharp
    /// <summary>
    /// 年月日
    /// </summary>
    public struct YMD
    {
        public string Year;     // 年
        public string Month;    // 月

        public string Day;      // 日

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Year = MidB2S(ref bBuff, 1, 4);
            Month = MidB2S(ref bBuff, 5, 2);
            Day = MidB2S(ref bBuff, 7, 2);
        }
    }

    /// <summary>
    /// 時分秒

    /// </summary>
    public struct HMS
    {
        public string Hour;     // 時

        public string Minute;   // 分

        public string Second;   // 秒


        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Hour = MidB2S(ref bBuff, 1, 2);
            Minute = MidB2S(ref bBuff, 3, 2);
            Second = MidB2S(ref bBuff, 5, 2);
        }
    }

    /// <summary>
    /// 時分
    /// </summary>
    public struct HM
    {
        public string Hour;     // 時

        public string Minute;   // 分


        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Hour = MidB2S(ref bBuff, 1, 2);
            Minute = MidB2S(ref bBuff, 3, 2);
        }
    }

    /// <summary>
    /// 月日時分
    /// </summary>
    public struct MDHM
    {
        public string Month;    // 月

        public string Day;      // 日
        public string Hour;     // 時

        public string Minute;   // 分


        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Month = MidB2S(ref bBuff, 1, 2);
            Day = MidB2S(ref bBuff, 3, 2);
            Hour = MidB2S(ref bBuff, 5, 2);
            Minute = MidB2S(ref bBuff, 7, 2);
        }
    }

    /// <summary>
    /// レコードヘッダ
    /// </summary>
    public struct RECORD_ID
    {
        public string RecordSpec;   // レコード種別
        public string DataKubun;    // データ区分

        public YMD MakeDate;        // データ作成年月日

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            RecordSpec = MidB2S(ref bBuff, 1, 2);
            DataKubun = MidB2S(ref bBuff, 3, 1);
            MakeDate.SetDataB(MidB2B(ref bBuff, 4, 8));
        }
    }

    /// <summary>
    /// 競走識別情報
    /// </summary>
    public struct RACE_ID
    {
        public string Year;         // 開催年
        public string MonthDay;     // 開催月日
        public string JyoCD;        // 競馬場コード

        public string Kaiji;        // 開催回[第N回]
        public string Nichiji;      // 開催日目[N日目]
        public string RaceNum;      // レース番号

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Year = MidB2S(ref bBuff, 1, 4);
            MonthDay = MidB2S(ref bBuff, 5, 4);
            JyoCD = MidB2S(ref bBuff, 9, 2);
            Kaiji = MidB2S(ref bBuff, 11, 2);
            Nichiji = MidB2S(ref bBuff, 13, 2);
            RaceNum = MidB2S(ref bBuff, 15, 2);
        }
    }

    /// <summary>
    /// 競走識別情報2
    /// </summary>
    public struct RACE_ID2
    {
        public string Year;         // 開催年
        public string MonthDay;     // 開催月日
        public string JyoCD;        // 競馬場コード

        public string Kaiji;        // 開催回[第N回]
        public string Nichiji;      // 開催日目[N日目]

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Year = MidB2S(ref bBuff, 1, 4);
            MonthDay = MidB2S(ref bBuff, 5, 4);
            JyoCD = MidB2S(ref bBuff, 9, 2);
            Kaiji = MidB2S(ref bBuff, 11, 2);
            Nichiji = MidB2S(ref bBuff, 13, 2);
        }
    }

    /// <summary>
    /// 本年・累計成績情報
    /// </summary>
    public struct SEI_RUIKEI_INFO
    {
        public string SetYear;          // 設定年
        public string HonSyokinTotal;   // 本賞金合計

        public string FukaSyokin;       // 付加賞金合計

        public string[] ChakuKaisu;     // 着回数

        // 配列の初期化

        public void Initialize()
        {
            ChakuKaisu = new string[6];
        }

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Initialize();
            SetYear = MidB2S(ref bBuff, 1, 4);
            HonSyokinTotal = MidB2S(ref bBuff, 5, 10);
            FukaSyokin = MidB2S(ref bBuff, 15, 10);

            for (int i = 0; i < 6; i++)
            {
                ChakuKaisu[i] = MidB2S(ref bBuff, 25 + (6 * i), 6);
            }
        }
    }

    /// <summary>
    /// 最近重賞勝利情報
    /// </summary>
    public struct SAIKIN_JYUSYO_INFO
    {
        public RACE_ID SaikinJyusyoid;  // <年月日場回日R>
        public string Hondai;           // 競走名本題

        public string Ryakusyo10;       // 競走名略称10字

        public string Ryakusyo6;        // 競走名略称6字

        public string Ryakusyo3;        // 競走名略称3字

        public string GradeCD;          // グレードコード

        public string SyussoTosu;       // 出走頭数
        public string KettoNum;         // 血統登録番号
        public string Bamei;            // 馬名


        // データセット
        public void SetDataB(byte[] bBuff)
        {
            SaikinJyusyoid.SetDataB(MidB2B(ref bBuff, 1, 16));
            Hondai = MidB2S(ref bBuff, 17, 60);
            Ryakusyo10 = MidB2S(ref bBuff, 77, 20);
            Ryakusyo6 = MidB2S(ref bBuff, 97, 12);
            Ryakusyo3 = MidB2S(ref bBuff, 109, 6);
            GradeCD = MidB2S(ref bBuff, 115, 1);
            SyussoTosu = MidB2S(ref bBuff, 116, 2);
            KettoNum = MidB2S(ref bBuff, 118, 10);
            Bamei = MidB2S(ref bBuff, 128, 36);
        }
    }

    /// <summary>
    /// 本年・前年・累計成績情報
    /// </summary>
    public struct HON_ZEN_RUIKEISEI_INFO
    {
        public string SetYear;                      // 設定年
        public string HonSyokinHeichi;              // 平地本賞金合計

        public string HonSyokinSyogai;              // 障害本賞金合計

        public string FukaSyokinHeichi;             // 平地付加賞金合計

        public string FukaSyokinSyogai;             // 障害付加賞金合計

        public CHAKUKAISU6_INFO ChakuKaisuHeichi;   // 平地着回数
        public CHAKUKAISU6_INFO ChakuKaisuSyogai;   // 障害着回数
        public CHAKUKAISU6_INFO[] ChakuKaisuJyo;    // 競馬場別着回数
        public CHAKUKAISU6_INFO[] ChakuKaisuKyori;  // 距離別着回数

        // 配列の初期化

        public void Initialize()
        {
            ChakuKaisuJyo = new CHAKUKAISU6_INFO[20];
            ChakuKaisuKyori = new CHAKUKAISU6_INFO[6];
        }

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Initialize();
            int i;

            SetYear = MidB2S(ref bBuff, 1, 4);
            HonSyokinHeichi = MidB2S(ref bBuff, 5, 10);
            HonSyokinSyogai = MidB2S(ref bBuff, 15, 10);
            FukaSyokinHeichi = MidB2S(ref bBuff, 25, 10);
            FukaSyokinSyogai = MidB2S(ref bBuff, 35, 10);
            ChakuKaisuHeichi.SetDataB(MidB2B(ref bBuff, 45, 36));
            ChakuKaisuSyogai.SetDataB(MidB2B(ref bBuff, 81, 36));
            
            for (i = 0; i < 20; i++)
            {
                ChakuKaisuJyo[i].SetDataB(MidB2B(ref bBuff, 117 + (36 * i), 36));
            }
            for (i = 0; i < 6; i++)
            {
                ChakuKaisuKyori[i].SetDataB(MidB2B(ref bBuff, 837 + (36 * i), 36));
            }

        }
    }

    /// <summary>
    /// レース情報
    /// </summary>
    public struct RACE_INFO
    {
        public string YoubiCD;      // 曜日コード

        public string TokuNum;      // 特別競走番号
        public string Hondai;       // 競走名本題

        public string Fukudai;      // 競走名副題

        public string Kakko;        // 競走名カッコ内

        public string HondaiEng;    // 競走名本題欧字

        public string FukudaiEng;   // 競走名副題欧字

        public string KakkoEng;     // 競走名カッコ内欧字

        public string Ryakusyo10;   // 競走名略称１０字

        public string Ryakusyo6;    // 競走名略称６字

        public string Ryakusyo3;    // 競走名略称３字

        public string Kubun;        // 競走名区分

        public string Nkai;         // 重賞回次[第N回]

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            YoubiCD = MidB2S(ref bBuff, 1, 1);
            TokuNum = MidB2S(ref bBuff, 2, 4);
            Hondai = MidB2S(ref bBuff, 6, 60);
            Fukudai = MidB2S(ref bBuff, 66, 60);
            Kakko = MidB2S(ref bBuff, 126, 60);
            HondaiEng = MidB2S(ref bBuff, 186, 120);
            FukudaiEng = MidB2S(ref bBuff, 306, 120);
            KakkoEng = MidB2S(ref bBuff, 426, 120);
            Ryakusyo10 = MidB2S(ref bBuff, 546, 20);
            Ryakusyo6 = MidB2S(ref bBuff, 566, 12);
            Ryakusyo3 = MidB2S(ref bBuff, 578, 6);
            Kubun = MidB2S(ref bBuff, 584, 1);
            Nkai = MidB2S(ref bBuff, 585, 3);
        }
    }

    /// <summary>
    /// 天候・馬場状態

    /// </summary>
    public struct TENKO_BABA_INFO
    {
        public string TenkoCD;      // 天候コード

        public string SibaBabaCD;   // 芝馬場状態コード

        public string DirtBabaCD;   // ダート馬場状態コード


        // データセット
        public void SetDataB(byte[] bBuff)
        {
            TenkoCD = MidB2S(ref bBuff, 1, 1);
            SibaBabaCD = MidB2S(ref bBuff, 2, 1);
            DirtBabaCD = MidB2S(ref bBuff, 3, 1);
        }
    }

    /// <summary>
    /// 着回数(サイズ3byte)
    /// </summary>
    public struct CHAKUKAISU3_INFO
    {
        public string[] ChakuKaisu;

        // 配列の初期化

        public void Initialize()
        {
            ChakuKaisu = new string[6];
        }

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Initialize();
            
            for (int i = 0; i < 6; i++)
            {
                ChakuKaisu[i] = MidB2S(ref bBuff, 1 + (3 * i), 3);
            }
        }
    }

    /// <summary>
    /// 着回数(サイズ4byte)
    /// </summary>
    public struct CHAKUKAISU4_INFO
    {
        public string[] ChakuKaisu;

        // 配列の初期化

        public void Initialize()
        {
            ChakuKaisu = new string[6];
        }

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Initialize();

            for (int i = 0; i < 6; i++)
            {
                ChakuKaisu[i] = MidB2S(ref bBuff, 1 + (4 * i), 4);
            }
        }
    }

    /// <summary>
    /// 着回数(サイズ5byte)
    /// </summary>
    public struct CHAKUKAISU5_INFO
    {
        public string[] ChakuKaisu;

        // 配列の初期化

        public void Initialize()
        {
            ChakuKaisu = new string[6];
        }

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Initialize();

            for (int i = 0; i < 6; i++)
            {
                ChakuKaisu[i] = MidB2S(ref bBuff, 1 + (5 * i), 5);
            }
        }
    }

    /// <summary>
    /// 着回数(サイズ6byte)
    /// </summary>
    public struct CHAKUKAISU6_INFO
    {
        public string[] ChakuKaisu;

        // 配列の初期化

        public void Initialize()
        {
            ChakuKaisu = new string[6];
        }

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Initialize();

            for (int i = 0; i < 6; i++)
            {
                ChakuKaisu[i] = MidB2S(ref bBuff, 1 + (6 * i), 6);
            }
        }
    }

    /// <summary>
    /// 競走条件コード

    /// </summary>
    public struct RACE_JYOKEN
    {
        public string SyubetuCD;    // 競走種別コード

        public string KigoCD;       // 競走記号コード

        public string JyuryoCD;     // 重量種別コード

        public string[] JyokenCD;   // 競走条件コード


        // 配列の初期化

        public void Initialize()
        {
            JyokenCD = new string[5];
        }

        // データセット
        public void SetDataB(byte[] bBuff)
        {
            Initialize();
            SyubetuCD = MidB2S(ref bBuff, 1, 2);
            KigoCD = MidB2S(ref bBuff, 3, 3);
            JyuryoCD = MidB2S(ref bBuff, 6, 1);
            
            for (int i = 0; i < 5; i++)
            {
                JyokenCD[i] = MidB2S(ref bBuff, 7 + (3 * i), 3);
            }
        }
    }
```
