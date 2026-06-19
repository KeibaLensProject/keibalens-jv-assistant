# C# で JV-Data をパースする

JV-Data の 1 レコードは「レコード種別ごとに長さが固定の Shift_JIS バイト列」。
レコードフォーマット表の **位置(1 始まり)** と **バイト長** が、そのままバイト切り出しのオフセットになる。
JRA-VAN 提供の C# 構造体サンプル(`references/spec/jvdata-struct/`)はこの切り出しを実装済みで、ほぼそのまま流用できる。

## 1. Shift_JIS エンコーディングの登録(.NET 5+ / .NET Core)

`Encoding.GetEncoding("Shift_JIS")` は .NET Framework では使えるが、.NET Core / .NET 5 以降では
コードページプロバイダの登録が必要。アプリ起動時に一度だけ実行する。

```csharp
using System.Text;

// Program.cs などの起動時に一度だけ
Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);
// 以降 Encoding.GetEncoding("Shift_JIS") / 932 が使える
```

NuGet `System.Text.Encoding.CodePages` が必要。

## 2. バイト切り出しヘルパ

サンプル(`references/spec/jvdata-struct/README.md`)の `MidB2S` / `MidB2B` がそのまま使える。
**位置は 1 始まり**で、内部で `-1` してから切り出すので、フォーマット表の「位置」をそのまま渡せる。

```csharp
// bSt = フォーマット表の「位置」(1 始まり), bLen = 「バイト」
public static string MidB2S(ref byte[] myByte, int bSt, int bLen)
    => Encoding.GetEncoding("Shift_JIS").GetString(myByte, bSt - 1, bLen);

public static byte[] MidB2B(ref byte[] myByte, int bSt, int bLen)
{
    byte[] cBt = new byte[bLen];
    Array.Copy(myByte, bSt - 1, cBt, 0, bLen);
    return cBt;
}
```

## 3. フォーマット表 → 切り出しコードの対応

`references/spec/jv-data-spec/record-formats/<ID>.md` の表(項番/位置/繰返/バイト)を、そのまま `MidB2S` 呼び出しに移す。

例: レース詳細(RA)の先頭付近
| 項番 | 項目名 | 位置 | バイト |
|---|---|---|---|
| 1 | レコード種別ID | 1 | 2 |
| 4 | 開催年 | 12 | 4 |
| 6 | 競馬場コード | 20 | 2 |
| 23 | グレードコード | 615 | 1 |

```csharp
RecordSpec = MidB2S(ref buf, 1, 2);    // "RA"
Year       = MidB2S(ref buf, 12, 4);   // yyyy
JyoCD      = MidB2S(ref buf, 20, 2);   // 競馬場コード(コード表 2001)
GradeCD    = MidB2S(ref buf, 615, 1);  // グレードコード(コード表 2003)
```

実際のサンプルでもこの通り実装されている(`references/spec/jvdata-struct/02-レース詳細.md`)。
サブ構造体は領域を切り出して渡す: `id.SetDataB(MidB2B(ref buf, 12, 16));`

## 4. 繰返し項目(繰返列がある項目)

フォーマット表の「繰返」列が 2 以上の項目は、`位置 + バイト長 * i` で i 番目を取り出す。

```csharp
// 本賞金が 7 回繰返し、各 8 バイト、開始位置 714 の場合
Honsyokin = new string[7];
for (int i = 0; i < 7; i++)
    Honsyokin[i] = MidB2S(ref buf, 714 + (8 * i), 8);
```

ネストした繰返し(例: コーナー通過順や馬毎の配列)も、外側→内側の順に同じ式を入れ子にする。

## 5. レコードの読み込みと種別判定

JV-Link から受け取った 1 行(Shift_JIS)を、**先頭 2 バイト = レコード種別ID** で判定して該当構造体に振り分ける。
未知のレコード種別IDは読み飛ばす(仕様追加で増えるため。`references/spec/jv-data-spec/data-types.md` 参照)。

```csharp
byte[] buf = Encoding.GetEncoding("Shift_JIS").GetBytes(line); // JVRead は Shift_JIS 文字列で返る
string recordSpec = MidB2S(ref buf, 1, 2);
switch (recordSpec)
{
    case "RA": var ra = new JV_RA_RACE(); ra.SetDataB(ref line); Handle(ra); break;
    case "SE": var se = new JV_SE_RACE_UMA(); se.SetDataB(ref line); Handle(se); break;
    // ... record-index.md の対応表に従って分岐 ...
    default:   /* 未知レコードはスキップ */ break;
}
```

> JVRead はレコード文字列とバイト数を返す。サンプルの `SetDataB(ref string)` は内部で `Str2Byte` して
> `MidB2S` で各項目を埋める実装になっている(`references/spec/jvdata-struct/02-レース詳細.md`)。

## 6. 数値・日付・初期値の扱い

- 取り出した文字列は固定長で、未設定時は **初期値**(`0`=半角"0" / `sp`=半角スペース / `Ｓ`=全角スペース)で埋まる。
  数値化する前に `Trim()` し、空なら 0 や null として扱う。
- 数値項目: `int.TryParse(MidB2S(...).Trim(), out var n)`。先頭ゼロ埋めはそのまま `int.Parse` で問題ない。
- 日付項目: `yyyymmdd` / 時刻 `hhmmss` 形式の固定長文字列。`DateTime.ParseExact(s, "yyyyMMdd", ...)` 等で変換。
- コード項目(競馬場・馬場状態など)は文字列のまま保持し、意味は `references/spec/jv-data-spec/code-tables/` で引く。

## 7. 実装の進め方(おすすめ)

1. 対象レコードを [record-index.md](./record-index.md) で特定し、`record-formats/` で項目を確認する。
2. `references/spec/jvdata-struct/` の該当構造体の `SetDataB` を出発点にする(切り出し位置が既に書かれている)。
3. **項目の位置/バイト数は必ず `record-formats/`(4.9.0.1)で照合する**。構造体サンプルは 2009 年版のため、
   その後拡張された項目(例: 2023 年の繁殖登録番号・生産者コード/名のサイズ拡張)は古いことがある。
4. 取得フロー(JVInit→JVOpen→JVRead→JVClose)は [jvlink-flow.md](./jvlink-flow.md) を参照。
