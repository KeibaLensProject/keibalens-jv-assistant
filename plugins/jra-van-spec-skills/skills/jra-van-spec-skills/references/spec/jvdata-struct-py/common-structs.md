# 共通構造体 (Python)

出典: `context/JVData_Struct.py` (JRA-VAN提供サンプル, 最終更新 2026-07-31, SDK Ver.5.0.0)

複数レコードで共有される `@dataclass` 構造体 (年月日・時分秒・着差・着回数など)。

定義: `YMD`, `HMS`, `HM`, `MDHM`, `RECORD_ID`, `RACE_ID`, `RACE_ID2`, `SEI_RUIKEI_INFO`, `SAIKIN_JYUSYO_INFO`, `HON_ZEN_RUIKEISEI_INFO`, `RACE_INFO`, `TENKO_BABA_INFO`, `CHAKUKAISU3_INFO`, `CHAKUKAISU4_INFO`, `CHAKUKAISU5_INFO`, `CHAKUKAISU6_INFO`, `RACE_JYOKEN`

```python
@dataclass
class YMD:
    """年月日"""
    Year: str   # 年
    Month: str  # 月
    Day: str    # 日

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 4),
            MidB2S(b, 5, 2),
            MidB2S(b, 7, 2),
        )

@dataclass
class HMS:
    """時分秒"""
    Hour: str       # 時
    Minute: str     # 分
    Second: str     # 秒

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 2),
            MidB2S(b, 3, 2),
            MidB2S(b, 5, 2),
        )

@dataclass
class HM:
    """時分"""
    Hour: str       # 時
    Minute: str     # 分

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 2),
            MidB2S(b, 3, 2),
        )

@dataclass
class MDHM:
    """月日時分"""
    Month: str      # 月
    Day: str        # 日
    Hour: str       # 時
    Minute: str     # 分

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 2),
            MidB2S(b, 3, 2),
            MidB2S(b, 5, 2),
            MidB2S(b, 7, 2),
        )

@dataclass
class RECORD_ID:
    """レコードヘッダ"""
    RecordSpec: str     # レコード種別
    DataKubun: str      # データ区分
    MakeDate: YMD       # データ作成年月日

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 2),
            MidB2S(b, 3, 1),
            YMD.SetDataB(MidB2B(b, 4, 8)),
        )

@dataclass
class RACE_ID:
    """競走識別情報"""
    Year: str       # 開催年
    MonthDay: str   # 開催月日
    JyoCD: str      # 競馬場コード
    Kaiji: str      # 開催回[第N回]
    Nichiji: str    # 開催日目[N日目]
    RaceNum: str    # レース番号

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 4),
            MidB2S(b, 5, 4),
            MidB2S(b, 9, 2),
            MidB2S(b, 11, 2),
            MidB2S(b, 13, 2),
            MidB2S(b, 15, 2),
        )

@dataclass
class RACE_ID2:
    """競走識別情報2"""
    Year: str       # 開催年
    MonthDay: str   # 開催月日
    JyoCD: str      # 競馬場コード
    Kaiji: str      # 開催回[第N回]
    Nichiji: str    # 開催日目[N日目]

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 4),
            MidB2S(b, 5, 4),
            MidB2S(b, 9, 2),
            MidB2S(b, 11, 2),
            MidB2S(b, 13, 2),
        )

@dataclass
class SEI_RUIKEI_INFO:
    """本年・累計成績情報"""
    SetYear: str            # 設定年
    HonSyokinTotal: str     # 本賞金合計
    FukaSyokin: str         # 付加賞金合計
    ChakuKaisu: list[str]   # 着回数

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 4),
            MidB2S(b, 5, 10),
            MidB2S(b, 15, 10),
            [MidB2S(b, 25 + 6 * i, 6) for i in range(6)],
        )

@dataclass
class SAIKIN_JYUSYO_INFO:
    """最近重賞勝利情報"""
    SaikinJyusyoid: RACE_ID     # <年月日場回日R>
    Hondai: str                 # 競走名本題
    Ryakusyo10: str             # 競走名略称10字
    Ryakusyo6: str              # 競走名略称6字
    Ryakusyo3: str              # 競走名略称3字
    GradeCD: str                # グレードコード
    SyussoTosu: str             # 出走頭数
    KettoNum: str               # 血統登録番号
    Bamei: str                  # 馬名

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            RACE_ID.SetDataB(MidB2B(b, 1, 16)),
            MidB2S(b, 17, 60),
            MidB2S(b, 77, 20),
            MidB2S(b, 97, 12),
            MidB2S(b, 109, 6),
            MidB2S(b, 115, 1),
            MidB2S(b, 116, 2),
            MidB2S(b, 118, 10),
            MidB2S(b, 128, 36),
        )

@dataclass
class HON_ZEN_RUIKEISEI_INFO:
    """本年・前年・累計成績情報"""
    SetYear: str                                # 設定年
    HonSyokinHeichi: str                        # 平地本賞金合計
    HonSyokinSyogai: str                        # 障害本賞金合計
    FukaSyokinHeichi: str                       # 平地付加賞金合計
    FukaSyokinSyogai: str                       # 障害付加賞金合計
    ChakuKaisuHeichi: CHAKUKAISU6_INFO          # 平地着回数
    ChakuKaisuSyogai: CHAKUKAISU6_INFO          # 障害着回数
    ChakuKaisuJyo: list[CHAKUKAISU6_INFO]       # 競馬場別着回数
    ChakuKaisuKyori: list[CHAKUKAISU6_INFO]     # 距離別着回数

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 4),
            MidB2S(b, 5, 10),
            MidB2S(b, 15, 10),
            MidB2S(b, 25, 10),
            MidB2S(b, 35, 10),
            CHAKUKAISU6_INFO.SetDataB(MidB2B(b, 45, 36)),
            CHAKUKAISU6_INFO.SetDataB(MidB2B(b, 81, 36)),
            [CHAKUKAISU6_INFO.SetDataB(MidB2B(b, 117 + 36 * i, 36)) for i in range(20)],
            [CHAKUKAISU6_INFO.SetDataB(MidB2B(b, 837 + 36 * i, 36)) for i in range(6)],
        )

@dataclass
class RACE_INFO:
    """レース情報"""
    YoubiCD: str        # 曜日コード
    TokuNum: str        # 特別競走番号
    Hondai: str         # 競走名本題
    Fukudai: str        # 競走名副題
    Kakko: str          # 競走名カッコ内
    HondaiEng: str      # 競走名本題欧字
    FukudaiEng: str     # 競走名副題欧字
    KakkoEng: str       # 競走名カッコ内欧字
    Ryakusyo10: str     # 競走名略称１０字
    Ryakusyo6: str      # 競走名略称６字
    Ryakusyo3: str      # 競走名略称３字
    Kubun: str          # 競走名区分
    Nkai: str           # 重賞回次[第N回]

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 1),
            MidB2S(b, 2, 4),
            MidB2S(b, 6, 60),
            MidB2S(b, 66, 60),
            MidB2S(b, 126, 60),
            MidB2S(b, 186, 120),
            MidB2S(b, 306, 120),
            MidB2S(b, 426, 120),
            MidB2S(b, 546, 20),
            MidB2S(b, 566, 12),
            MidB2S(b, 578, 6),
            MidB2S(b, 584, 1),
            MidB2S(b, 585, 3),
        )

@dataclass
class TENKO_BABA_INFO:
    """天候・馬場状態"""
    TenkoCD: str        # 天候コード
    SibaBabaCD: str     # 芝馬場状態コード
    DirtBabaCD: str     # ダート馬場状態コード

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 1),
            MidB2S(b, 2, 1),
            MidB2S(b, 3, 1),
        )

@dataclass
class CHAKUKAISU3_INFO:
    """着回数(サイズ3byte)"""
    ChakuKaisu: list[str]

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls([MidB2S(b, 1 + 3 * i, 3) for i in range(6)])

@dataclass
class CHAKUKAISU4_INFO:
    """着回数(サイズ4byte)"""
    ChakuKaisu: list[str]

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls([MidB2S(b, 1 + 4 * i, 4) for i in range(6)])

@dataclass
class CHAKUKAISU5_INFO:
    """着回数(サイズ5byte)"""
    ChakuKaisu: list[str]

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls([MidB2S(b, 1 + 5 * i, 5) for i in range(6)])

@dataclass
class CHAKUKAISU6_INFO:
    """着回数(サイズ6byte)"""
    ChakuKaisu: list[str]

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls([MidB2S(b, 1 + 6 * i, 6) for i in range(6)])

@dataclass
class RACE_JYOKEN:
    """競走条件コード"""
    SyubetuCD: str          # 競走種別コード
    KigoCD: str             # 競走記号コード
    JyuryoCD: str           # 重量種別コード
    JyokenCD: list[str]     # 競走条件コード

    # データセット
    @classmethod
    def SetDataB(cls, b):
        return cls(
            MidB2S(b, 1, 2),
            MidB2S(b, 3, 3),
            MidB2S(b, 6, 1),
            [MidB2S(b, 7 + 3 * i, 3) for i in range(5)],
        )
    
```
