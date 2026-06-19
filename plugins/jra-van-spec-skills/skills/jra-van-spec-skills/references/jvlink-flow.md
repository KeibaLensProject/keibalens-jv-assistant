# JV-Link 呼び出しフロー

C# から JV-Link(COM)で JV-Data を取得する流れ。メソッドの正確な引数・戻り値は
`references/spec/jvlink-interface/methods/<連番>-<名称>.md`、戻り値コードは `references/spec/jvlink-interface/code-table.md` を参照。
COM 参照は JVDTLab(JV-Link)を追加し、`new JVDTLabLib.JVLink()` を生成して使う。

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

- イベント駆動の設計は `references/spec/dev-guide-event-cpp.md` と `references/spec/jvlink-interface/methods/23-JVWatchEvent.md`。

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
- 開発全般: `references/spec/dev-guide.md`
