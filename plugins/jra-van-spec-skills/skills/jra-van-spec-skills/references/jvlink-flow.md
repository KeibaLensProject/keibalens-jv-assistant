# JV-Link 呼び出しフロー

C# / Python などから JV-Link(COM)で JV-Data を取得する流れ。メソッドの正確な引数・戻り値は
`references/spec/jvlink-interface/methods/<連番>-<名称>.md`、戻り値コードは `references/spec/jvlink-interface/code-table.md` を参照。
COM ProgID は `JVDTLab.JVLink`（C# では JVDTLab COM 参照を追加し `new JVDTLabLib.JVLink()`、Python では `win32com.client.Dispatch("JVDTLab.JVLink")`）。

## JV-Link Ver.5.0.0 (64bit版 / 32bit版) の仕様と注意点

SDK Ver.5.0.0（2026年8月公開）より、従来の 32bit(x86) 版に加えて **64bit(x64) 版 JV-Link** が提供されている。

| 項目 | 仕様・注意点 |
|---|---|
| **API 互換性** | メソッド名・引数・戻り値・COM ProgID (`JVDTLab.JVLink`) は 32bit版・64bit版で共通（`JV-Linkインターフェース仕様書 4.9.0.1` から変更なし） |
| **接続先の決まり方** | **JV-Link を直接呼び出すプロセスの bit 数**で決まる（x64 プロセス→64bit版 JV-Link、x86 プロセス→32bit版 JV-Link）。Visual Studio で 64bit 版を使う場合はプラットフォームを `x64` に設定する（`references/spec/dev-guide.md` 3.4.2 参照）。64bit Python からも直接利用可能 |
| **同一端末での共存** | 32bit版と 64bit版の JV-Link（および検証ツール Ver.2.7.0）は同一 PC に共存インストール可能。32bit版と 64bit版の競馬ソフトは同時起動できるが、**JV-Link 設定画面 (`JVSetUIProperties`) は同時に起動できない** |
| **利用キー (重要)** | **32bit版と 64bit版にはそれぞれ異なる利用キーを登録する必要がある**。同一の利用キーを両方に設定した場合は `-301`（認証エラー）となる |
| **ソフトID (`sid`)** | `JVInit(sid)` に渡すソフトIDは **32bit版と 64bit版で共有**して使用する |
| **ポート番号** | 64bit版の追加に伴い、32bit版と 64bit版で同じポート番号を設定すると競合防止のためエラーとなる |
| **JV-Link 設定画面** | Ver.5.0.0 では JV-Link Agent が停止している場合でも設定画面を実行でき、設定画面から Agent の「起動」「停止」を実行できるボタンが追加された |
| **保存パス (`m_savepath`)** | `JVSetSavePath` / 設定画面で指定するのは `cache` と `data` が作られる親フォルダ。32bit版と 64bit版を併用する場合は、別々の Agent によるファイル競合を避けるため保存先フォルダを分けるのが安全 |

## 蓄積系(過去・差分データ): JVOpen

```
JVInit("SOFTID")                         // 起動時に1回。0=正常, 負=エラー
  ├ JVSetServiceKey(...)                 // 利用キー設定(任意。未設定ならレジストリ値)
  ├ JVSetSaveFlag(1) / JVSetSavePath(...)// ダウンロードファイルの保存設定(任意)
JVOpen(dataspec, fromtime, option,       // 取得要求。0=正常, 負=エラー
       out readcount, out downloadcount, out lastfiletimestamp)
  ├ (downloadcount>0 の間) JVStatus()    // ダウンロード進捗。== downloadcount で完了
  ├ JVRead(out buff, out size, out fname)// 1レコード読込。>0=バイト数, -1=ファイル切替, 0=EOF, 負=エラー
  │    └ レコード先頭2バイトで種別判定 → 該当構造体でパース(csharp-parsing.md)
  └ JVSkip()                             // 不要ファイルの読み飛ばし(任意)
JVClose()                                // 取り込み終了
```

### C# 擬似コード

```csharp
var jv = new JVDTLabLib.JVLink();

int rc = jv.JVInit("SOFTID");
if (rc != 0) throw new JvLinkException(rc);   // 負値は code-table.md を参照

int readCount, downloadCount;
string lastTimestamp;
rc = jv.JVOpen("RACE", "20240101000000", 1, out readCount, out downloadCount, out lastTimestamp);
if (rc != 0) throw new JvLinkException(rc);

// ダウンロード完了待ち(プログレス表示する場合のみ。0除算に注意)
while (downloadCount > 0 && jv.JVStatus() < downloadCount)
    Thread.Sleep(500);

while (true)
{
    string buff = new string('\0', 110000);   // 最大レコード長+改行+NULL を確保
    int size; string filename;
    int ret = jv.JVRead(out buff, out size, out filename);
    if (ret == 0) break;                       // EOF: 全ファイル読了
    if (ret == -1) continue;                    // ファイル切り替わり: 次のファイルへ
    if (ret < 0) throw new JvLinkException(ret);// エラー

    string spec = buff.Substring(0, 2);         // レコード種別ID
    Dispatch(spec, buff);                        // 種別ごとに構造体へパース
}

// 次回差分取得のため lastTimestamp を保存しておく(次回 JVOpen の fromtime に使う)
Save(lastTimestamp);
jv.JVClose();
```

- `fromtime` は `YYYYMMDDhhmmss`、または `開始-終了` の範囲指定。前回の `lastfiletimestamp` を渡すと差分取得・再開になる。
- `option` の意味と dataspec の組み合わせは [dataspec-option.md](./dataspec-option.md)。
- バイナリで読みたい場合は `JVRead` の代わりに `JVGets`(`references/spec/jvlink-interface/methods/10-JVGets.md`)。

### Python (`pywin32`) 擬似コード

公式サンプル `references/spec/sample-python/` (`Form1.py` / `Form2.py`) に準拠した呼び出し例。
64bit Python では 64bit 版 JV-Link、32bit Python では 32bit 版 JV-Link が使われる。

```python
import time
import win32com.client

jv = win32com.client.Dispatch("JVDTLab.JVLink")
rc = jv.JVInit("UNKNOWN")  # 本番は固有のソフトID
if rc != 0:
    raise RuntimeError(f"JVInit error: {rc}")

# pywin32 では出力引数も含めて渡し、(戻り値, read_count, download_count, lastfiletime) のタプルで返る
ret = jv.JVOpen("RACE", "20240101000000", 1, 0, 0, "")
open_code, read_count, download_count, lastfiletime = (
    (ret[0], int(ret[1] or 0), int(ret[2] or 0), str(ret[3] or ""))
    if isinstance(ret, (list, tuple)) else (ret, 0, 0, "")
)
if open_code < 0:  # -1=該当データなし, -2以下=エラー
    jv.JVClose()
    raise RuntimeError(f"JVOpen code: {open_code}")

while download_count > 0:
    status = jv.JVStatus()
    if status < 0:
        jv.JVClose()
        raise RuntimeError(f"JVStatus error: {status}")
    if status >= download_count:
        break
    time.sleep(0.3)

buffsize = 110000
while True:
    buff = bytearray(buffsize)
    buffname = bytearray()
    ret_code, memview, fname = jv.JVGets(buff, buffsize, buffname)
    ret_code = int(ret_code)
    if ret_code == 0:      # EOF
        break
    if ret_code == -1:     # ファイル切替
        continue
    if ret_code < 0:       # エラー
        raise RuntimeError(f"JVGets error: {ret_code}")

    raw: bytes = memview.tobytes()               # Shift_JIS(cp932) バイト列
    rec_id = raw[:2].decode("cp932", "ignore")   # 先頭2バイト = レコード種別ID
    # JVData_Struct.py の SetDataB(raw) または decode("cp932") で処理

jv.JVClose()
```

## 速報系(当日データ): JVRTOpen

```csharp
rc = jv.JVRTOpen("0B11", key);   // 例: 速報馬体重。key で対象レース等を指定
// 以降は JVRead/JVGets で読み込み、JVClose で終了(JVOpen と同様)
```

- `JVRTOpen` は option を取らない。`dataspec`(0Bxx)と `key`(対象レースキー等)で指定する。
- 速報専用レコード(WH/WE/AV/JC/TC/CC)はここで取得する(`JVOpen` では取れない)。
- 引数の詳細は `references/spec/jvlink-interface/methods/07-JVRTOpen.md`。

## イベント駆動(確定・変更通知): JVWatchEvent

```csharp
jv.JVWatchEvent();          // 通知開始。確定/変更の発生時にイベントが届く
// ... イベントハンドラ内で JVRTOpen → JVRead して該当データを取得 ...
jv.JVWatchEventClose();     // 通知終了
```

- イベント駆動の設計は C++ 版 `references/spec/dev-guide-event-cpp.md`、Python 版 `references/spec/dev-guide-event-python.md`、および `references/spec/jvlink-interface/methods/23-JVWatchEvent.md`。
- Python (`pywin32`) でイベントを受ける場合は、ワーカースレッドで `pythoncom.CoInitialize()` → `win32com.client.DispatchWithEvents("JVDTLab.JVLink", HandlerClass)` → `JVInit` → `JVWatchEvent` → `pythoncom.PumpWaitingMessages()` ループを回し、`OnJVEvtPay(self, bstr)` 等のハンドラ内で `JVRTOpen` → `JVGets` → `JVClose` を呼ぶ（詳細は `references/spec/dev-guide-event-python.md`）。

## 戻り値(エラー)コードの扱い

- 多くのメソッドは **0=正常、負値=エラー**(`JVStatus` は完了ファイル数、`JVRead` は >0=バイト数)。
- 負値の意味は `references/spec/jvlink-interface/code-table.md` のグループ別表で引く(例: -1=該当データなし、
  -2xx 系=サーバ/通信、-3xx 系=パラメータ不正 等)。メソッドごとに返りうるコードが異なるので、
  各メソッドの「戻り値」節も併せて確認する。
- ダウンロード完了前に `JVRead`/`JVGets` を呼ぶと予期しないエラーになり得る。`JVStatus` で完了を確認する。
- 中断時は `JVCancel`(`references/spec/jvlink-interface/methods/12-JVCancel.md`)でダウンロードスレッドを停止し、
  `JVClose` する。

## 関連ドキュメント

- メソッド一覧: `references/spec/jvlink-interface/methods/README.md`
- プロパティ(m_servicekey 等): `references/spec/jvlink-interface/properties.md`
- 呼び出しの実例(C++/MFC): `references/spec/sample-vc2019/README.md`(JVOpen→JVRead ループの実装箇所を明記)
- 呼び出しの実例(Python 3.14): `references/spec/sample-python/README.md`(JVOpen→JVGets ループの実装箇所を明記)
- イベント駆動ガイド: `references/spec/dev-guide-event-cpp.md`(C++) / `references/spec/dev-guide-event-python.md`(Python)
- 開発全般: `references/spec/dev-guide.md`(第4.2.3版・VS2026 / 64bit対応 / Python追加)
