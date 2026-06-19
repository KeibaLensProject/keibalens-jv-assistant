# JRA-VAN サンプルプログラム sample1 (C++ / MFC, VC2019)

出典: `context/sample1_VC2019/`

JRA-VAN 公式の C++ (MFC) サンプルです。**JV-Link の呼び出しフロー**(初期化→取得要求→進捗→読み込み→終了)を示しており、C# 実装時の処理順序・エラーハンドリングの参考になります。

## JV-Link 呼び出しフロー(蓄積系)

```
JVInit                  設定ダイアログ初期化時 (sample1Dlg1.cpp)
JVSetUIProperties       設定変更         (sample1Dlg1.cpp)
JVOpen                  データ取得要求    (sample1Dlg2.cpp)
  JVStatus              ダウンロード進捗  (sample1Dlg2.cpp)
  JVRead / JVGets       レコード読み込み  (sample1Dlg2.cpp)
  JVSkip                読みとばし
JVClose                 取り込み終了      (sample1Dlg2.cpp)
```

## ファイル一覧

| ファイル | 役割 | 変換 |
|---|---|---|
| `ReadMe.txt` | プロジェクト構成の概要(AppWizard 生成) | [ReadMe-txt.md](./ReadMe-txt.md) |
| `dlgDel.cpp` | 削除確認ダイアログ | [dlgDel-cpp.md](./dlgDel-cpp.md) |
| `dlgDel.h` | 削除確認ダイアログのヘッダ | [dlgDel-h.md](./dlgDel-h.md) |
| `jvlink.cpp` | JV-Link COM ラッパ実装(#import 生成) | [jvlink-cpp.md](./jvlink-cpp.md) |
| `jvlink.h` | JV-Link COM ラッパ宣言(IJVLink インターフェース) | [jvlink-h.md](./jvlink-h.md) |
| `resource.h` | リソース ID 定義 | [resource-h.md](./resource-h.md) |
| `sample1.cpp` | アプリケーションクラス CSample1App(エントリポイント) | [sample1-cpp.md](./sample1-cpp.md) |
| `sample1.h` | アプリケーションの中心インクルード | [sample1-h.md](./sample1-h.md) |
| `sample1.rc` | リソーススクリプト(ダイアログ/メニュー定義) | [sample1-rc.md](./sample1-rc.md) |
| `sample1Del.cpp` | ファイル削除処理。JVFiledelete を呼ぶ | [sample1Del-cpp.md](./sample1Del-cpp.md) |
| `sample1Del.h` | ファイル削除処理のヘッダ | [sample1Del-h.md](./sample1Del-h.md) |
| `sample1Dlg1.cpp` | 設定ダイアログ。JVInit / JVSetUIProperties を呼ぶ | [sample1Dlg1-cpp.md](./sample1Dlg1-cpp.md) |
| `sample1Dlg1.h` | 設定ダイアログのヘッダ | [sample1Dlg1-h.md](./sample1Dlg1-h.md) |
| `sample1Dlg2.cpp` | データ取得ダイアログ。JVOpen→JVStatus→JVRead→JVClose の中核 | [sample1Dlg2-cpp.md](./sample1Dlg2-cpp.md) |
| `sample1Dlg2.h` | データ取得ダイアログのヘッダ | [sample1Dlg2-h.md](./sample1Dlg2-h.md) |
| `sample1Dlg2.htm` |  | [sample1Dlg2-htm.md](./sample1Dlg2-htm.md) |
| `stdafx.cpp` | プリコンパイル済みヘッダ | [stdafx-cpp.md](./stdafx-cpp.md) |
| `stdafx.h` | 共通インクルード | [stdafx-h.md](./stdafx-h.md) |
| `res\html_sam.htm` |  | [res_html_sam-htm.md](./res_html_sam-htm.md) |

## JV-Link メソッド使用箇所

| メソッド | 使用箇所(ファイル:行) |
|---|---|
| JVInit | `jvlink.h:59`, `sample1Dlg1.cpp:152`, `sample1Dlg1.cpp:158`, `sample1Dlg2.cpp:92` |
| JVSetUIProperties | `jvlink.h:72`, `sample1Dlg1.cpp:266` |
| JVSetServiceKey | `jvlink.h:125` |
| JVSetSaveFlag | `jvlink.h:138` |
| JVSetSavePath | `jvlink.h:40` |
| JVOpen | `jvlink.h:78`, `sample1Dlg2.cpp:35`, `sample1Dlg2.cpp:37`, `sample1Dlg2.cpp:40`, `sample1Dlg2.cpp:111` |
| JVRTOpen | `jvlink.h:107` |
| JVStatus | `jvlink.h:85`, `sample1Dlg2.cpp:179` |
| JVRead | `jvlink.h:91`, `sample1Dlg2.cpp:236`, `sample1Dlg2.cpp:273`, `sample1Dlg2.cpp:274`, `sample1Dlg2.cpp:328` |
| JVGets | `jvlink.h:98`, `sample1Dlg2.cpp:240`, `sample1Dlg2.cpp:241`, `sample1Dlg2.cpp:276`, `sample1Dlg2.cpp:277` |
| JVSkip | `jvlink.h:170` |
| JVCancel | `jvlink.h:114`, `sample1Dlg2.cpp:382`, `sample1Dlg2.cpp:388`, `sample1Dlg2.cpp:389` |
| JVClose | `jvlink.h:66`, `sample1Dlg2.cpp:358` |
| JVFiledelete | `dlgDel.cpp:52`, `jvlink.h:118`, `sample1Del.cpp:67` |
| JVFukuFile | `jvlink.h:188` |
| JVFuku | `jvlink.h:195` |
| JVMVCheck | `jvlink.h:181` |
| JVMVPlay | `jvlink.h:174` |

## 変換対象外(バイナリ/プロジェクト/ビルド設定)

`res\sample1.ico`, `res\sample1.manifest`, `res\sample1.rc2`, `sample1.dsp`, `sample1.dsw`, `sample1.ncb`, `sample1.sln`, `sample1.vcxproj`, `sample1.vcxproj.filters`
