# JRA-VAN サンプルプログラム sample1 (Python 3.14 / pywin32)

出典: `context/sample1_Python3.14/` (SDK Ver.5.0.0 64bit版同梱)

SDK Ver.5.0.0 (64bit版) で追加された JRA-VAN 公式の Python (`tkinter` + `pywin32`) サンプルです。
64bit Python から 64bit 版 JV-Link (`JVDTLab.JVLink`) を呼び出す際の **COM 生成・タプル戻り値の受け取り・`JVGets` による `memoryview` 取得と `cp932` デコード** の公式実装例になります。

## JV-Link 呼び出しフロー (Python / 蓄積系)

```
win32com.client.Dispatch("JVDTLab.JVLink")  COM オブジェクト生成 (Form1.py)
JVInit("UNKNOWN")                           初期化 (Form1.py)
JVSetUIProperties()                         JV-Link 設定画面表示 (Form1.py)
JVOpen(dataspec, fromdate, option, 0, 0, "") 取得要求 → (rc, read_count, download_count, lastfiletime) (Form2.py)
  JVStatus()                                ダウンロード進捗ポーリング (Form2.py)
  JVGets(buff, buffsize, buffname)          1レコード読込 → (ret, memview, fname), memview.tobytes().decode("cp932") (Form2.py)
  JVCancel()                                ダウンロード/読込中止 (Form2.py)
JVClose()                                   取り込み終了 (Form2.py)
JVFiledelete(filename)                      ダウンロードファイル削除 (Form1.py)
```

## ファイル一覧

| ファイル | 役割 | 変換 |
|---|---|---|
| `Form1.py` | メイン画面。win32com.client.Dispatch("JVDTLab.JVLink") 生成・JVInit・JVSetUIProperties・JVFiledelete を呼ぶ | [Form1-py.md](./Form1-py.md) |
| `Form2.py` | データ取込みダイアログ。別スレッドで JVOpen → JVStatus → JVGets (cp932 デコード) / JVRead → JVCancel / JVClose を呼ぶ | [Form2-py.md](./Form2-py.md) |

## JV-Link メソッド使用箇所

| メソッド | 使用箇所(ファイル:行) |
|---|---|
| JVInit | `Form1.py:97`, `Form1.py:111` |
| JVSetUIProperties | `Form1.py:151` |
| JVOpen | `Form2.py:153` |
| JVStatus | `Form2.py:202` |
| JVRead | `Form2.py:231`, `Form2.py:257`, `Form2.py:259` |
| JVGets | `Form2.py:231`, `Form2.py:257`, `Form2.py:258`, `Form2.py:293` |
| JVCancel | `Form2.py:198`, `Form2.py:246`, `Form2.py:312`, `Form2.py:316` |
| JVClose | `Form2.py:319`, `Form2.py:323` |
| JVFiledelete | `Form1.py:154`, `Form1.py:166`, `Form1.py:171` |
