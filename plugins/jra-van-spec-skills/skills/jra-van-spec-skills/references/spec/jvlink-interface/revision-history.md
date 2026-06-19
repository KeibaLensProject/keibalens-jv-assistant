# JV-Link インターフェース仕様書 修正履歴

出典: `context/JV-Linkインターフェース仕様書_4.9.0.1(Win).pdf`

```
修正履歴
日付
版
項番
種類
内容
2024/08/07
4.9.0.1
修正
・JVRead/JVGets の中断・再開についての記述箇所をlastfiletimestamp の説
明の外に記述するよう修正
2023/8/8
4.9.0
修正
・JVOpen のoption パラメータとdataspec の指定不可に関する組合せ表
を修正
・JVOpen の読み出し終了ポイント時刻を指定することができないパラメータ
に関する記述を修正
2022/12/5
4.8.0.1
修正
・JVMVPlay/JVMVPlayWithTypeの【補足】のパトロール映像に関する
記述を修正
2022/6/21
4.8.0
修正
・JVSetUIProperties のダイアログを変更
修正
・JVOpen のoption とdataspec の指定誤りを修正
修正
・メソッド一覧のJVEventPay をJVEvtPay に変更
2022/4/5
4.7.1
修正
・メソッド一覧のJVSaveFlg をJVSaveFlag に変更
修正
・JVOpen メソッドの【パラメータ】に読み出し終了ポイント時刻指定に関する
説明を追加
修正
・JVFileDelete メソッドをJVFiledelete に変更
2022/2/22
4.7.0.1
修正
・スタートキット(CD/DVD-ROM)の提供終了に伴い、関連する記述を修正
3
修正
・【戻り値】の「-501」にスタートキット(CD/DVD-ROM)の提供終了を追記
2021/10/19
4.7.0
3
修正
・JVOpen/JVRTOpen の戻り値「-305」を追加
2021/5/13
4.6.0
修正
・JVOpen メソッドのfromtime パラメータ修正に伴い、パラメータ設定方法の
説明を修正
修正
・動画再生ブラウザの説明を修正
3
追加
・JVOpen/JVRTOpen の戻り値「-113」を追加
3
修正
・JVOpen/JVRTOpen の戻り値「-112」、「-114」の説明を修正
2017/1/24
4.5.1
修正
・JV-Linkマイナーバージョンアップのため版番号改訂
2016/7/26
4.5.0
修正
・JVMVCheckWithType、JVMVPlayWithType の【パラメータ】を追加
movietype“02”(マルチカメラ動画)、”03”(パトロール動画)を追加
追
修正
・JVSetUIProperties の【解説】のダイアログを変更
2016/4/19
4.4.2
-
修正
・開発環境更新に伴うJV-Linkマイナーバージョンアップのため版番号改訂
2015/10/20
4.4.1
-
修正
・開発環境更新に伴うJV-Linkマイナーバージョンアップのため版番号改訂
2014/6/10
4.4.0
修正
・JVMVPlay/JVMVPlayWithTypeのMP4形式動画の対応に伴い、動画
種別に関する記述を追記
・JVMVPlay/JVMVPlayWithType の【解説】の動画再生方式に
IE を追加
・JVMVPlay/JVMVPlayWithTypeの【補足】に映像形式変更に関する
記述を追記
修正
・JVSetUIProperties の【解説】のダイアログを変更
2013/9/25
4.3.2
修正
・JVMVPlay/JVMVPlayWithTYpe、JVMVOpen、JVMVRead の
【補足】に開発を行う際の説明を追記
2013/4/9
4.3.1
-
修正
・JV-Linkマイナーバージョンアップのため版番号改訂
2012/12/4
4.3.0
追加
・JVMVChcekWithTypeメソッドを追加
修正
・JVMVPlayWithTypeメソッドの【パラメータ】を追加
movietype“01”(パドック動画)を追加
修正
・メソッド追加に伴い、関連する他のメソッドの記述を修正
2012/2/21
4.2.0
1
修正
・JVSetUIPropertiesの【解説】の払戻ダイアログ表示に関する説明を
追記
修正
・JVSetUIPropertiesの払戻ダイアログ表示フラグのプロパティ名の
誤りを修正
2011/9/28
4.1.0
1
修正
・JVSetUIProperties のダイアログを変更
ダイアログ変更に伴い、「JRA-VANからのお知らせ」「払戻ダイアログ」の
表示に関する説明を修正
2011/6/21
4.0.0
1
追加
・JVOpen Option“2”の指定できないデータ種別ID にMING を追加
2010/10/12
3.5.0
1
追加
・m_payflag プロパティを追加
2
追加
・JVWatchEvent、JVWatchEventClose メソッドを追加
追加
・JVWatchEvent、JVWatchEventClose の戻り値を追加
2
修正
・JVRTOpen 第二引数の指定方法についてイベント発生時の引数の指定
も可能とする記述を追加
・JVSetUIProperties のダイアログを変更
・JVSetUIPropertiesの説明に払戻ダイアログに関するを追加
2009/12/8
3.4.0
修正
・JVCourseFile の【戻り値】に「-202」を追記
修正
・JVCourseFile2 の【戻り値】に「-202」を追記
2009/9/8
3.3.0
2
修正
・JVSetUIProperties のダイアログを変更
2009/6/23
3.2.1
2
修正
・JVCourseFileの【パラメータ】の説明を修正
コース説明の最大バイト数を修正
2009/3/17
3.2.0
2
修正
・JVOpen のOptionパラメータとdataspecパラメータの指定不可に関する
組合せ表に追記(今週データはCOMMが指定不可)
2
追加
・JVCourseFile2 メソッドを追加
追加
・JVCourseFile2 の戻り値を追加
2008/11/4
3.1.0.1
2
修正
・JVCourseFileの【パラメータ】の説明に追記
最新のコース図を取得する場合のパラメータについての説明を追記
コース説明の最大バイト数を追記
2008/9/24
3.1.0
2
追加
・JVCourseFile メソッドを追加
追加
・JVCourseFileの戻り値を追加
2008/6/17
3.0.0
-
修正
Windows Vista対応によりバージョン更新
2007/12/25
2.4.0
2
追加
・JVMVOpen、JVMVRead、JVMVPlayWithType メソッドを追加
追加
・JVMVOpen、JVMVRead の戻り値を追加
修正
・メソッド追加に伴い、関連する他のメソッドの記述を修正
2007/5/9
2.3.1
2
修正
・JVFukuFileの【パラメータ】の説明を修正
誤:作成した勝負服のビットマップファイルを出力するフォルダを指定
正:勝負服ファイルの出力ファイル名をフルパスで指定
・JVFukuFile、JVFukuの【解説】の説明を修正
2007/4/25
2.3.0
2
追加
・JVFukuFile、JVFuku メソッドを追加
追加
・JVFukuFile、JVFukuの戻り値を追加
2
修正
・JVOpen のlastfiletimestamp の説明の誤りを修正
2006/11/7
2.2.0
2
追加
・JVMVCheck、JVMVPlayメソッドを追加
2
修正
・JVSetSaveFlag の【戻り値】の説明を修正
誤:利用キーが正しくセットされた場合...
正:保存フラグが正しくセットされた場合...
2
修正
・JVSetSavePath の【戻り値】の説明を修正
誤:利用キーが正しくセットされた場合...
正:保存パスが正しくセットされた場合...
2
修正
・JVGets の解説を修正
VisualBasic.NET におけるメモリ解放に関する説明を削除
追加
・JVMVPlay の戻り値を追加
2004/11/2
2.1.1
2
修正
・JVRead の説明を修正
Buff パラメータの解放に関する説明を【補足】へ移動し仕様とする
2
修正
・JVGets の解説を修正
VisualBasic.NETに関する補足を追加
コーディング例のVisualBasic のバージョンを明確化(VB6)
2004/10/7
2.1.0
2
追加
・JVGets メソッドを追加
2
修正
・JVOpen/JVReadの構文を修正
2004/8/10
2.0.0
1
追加
・m_TotalReadFilesize の説明を修正
1024 で割った結果が0KB となる場合は、1KB を返すように変更
1
追加
・ParentHWnd プロパティを追加
3
追加
・JVRead の戻り値”-503”の説明を追加
2004/6/9
1.1.7
2
追加
・JVInitの解説に呼出タイミングに関する説明を追加
2004/4/2
1.1.5.1
2
追加
・JVOpen のdataspec の説明に既知の障害に関する記述を追加
(複数指定時に処理時間が長くなる)
2
追加
・JVOpen のlastfiletimestamp の説明に処理中断・再開に関する記述を
追加
2
追加
・JVRead のbuff の説明に既知の障害に関する記述を追加
(JVRead 内におけるデータ格納バッファの開放と確保)
2004/3/23
1.1.5
2
追加
・JVInitの説明に使用可能文字に関する記述を追加
2
追加
・JVOpen のoption パラメータにコード=4を追加
3
追加
・JVOpen/JVRTOpen の戻り値”-504”を追加
3
追加
・JVOpen/JVRTOpen の戻り値”-301”の説明を修正
2
追加
・Option パラメータとdataspec パラメータの指定不可に関する組合せ表を
修正(セットアップ時にTOKU の指定が可能)
・セットアップデータ取得時におけるdataspec=TOKUに関する補足を追加
1
修正
・m_TotalReadFilesize の説明を修正
戻り値である総データサイズがlong の最大値を超えたため、単位をKB に
変更
2004/3/2
1.1.4
2
修正
・JVSetUIProperties について説明を追加
3
修正
・JVOpen/JVRTOpen の戻り値”-1”を追加
3
修正
・JVStatusの戻り値”-502”の説明を修正
3
追加
・JVRead の戻り値”-402”, “-403”, “-502”を追加
3
追加
・JVSetServiceKey/JVSetSaveFlag/JVSetSavePath の戻り値”-101”を
追加
2
修正
・JVOpen のfromtime の説明の誤りを修正
・JVRead のパラメータの説明を補足
2003/9/3
1.1.2
β
3
修正
・JVOpen/JVRTOpen の戻り値”-112”の説明文修正
・JVOpen/JVRTOpen の戻り値”-113”の削除
2
追加
・JVSkip メソッドの追加
・m_CurrentFileTimestampプロパティの追加
2
修正
・JVRTOpen の第一引数の型の誤りを修正
誤:uint 型→正:string 型
・JVRTOpen の第二引数の指定方法についてレース単位の場合
に”YYYYMMDDJJRR”の指定も可能とする記述を追加
2003/8/8
1.1.1
β
1
追加
・m_JVLinkVersion,m_TotalReadFilesize,m_CurrentReadFilesize の
3つのプロパティを追加
2003/6/3
1.0.5
β
2
追加
・JVReadの戻り値”-1”について説明を追加
2003/5/16
1.0.4
β
3
追加
・コード表に各戻り値について対処方法の記述を追加
1
修正
・m_savepathプロパティのデフォルト値の誤りを修正し説明を追加
誤:「%InstallPath%\data」→正:「%InstallPath%」
・説明の中のメソッド名の誤りを修正誤:
「JVUISetProperties」→正:「JVSetUIProperties」
2003/5/2
1.0.3
β
2
修正
・JVOpenの引数の名前を実装された名前に合わせて修正
誤:「lasttime」→「lastfiletimestamp」
2
追加
・JVSetUIProperties実行時の保存パス指定の処理について説明を追加
・JVSetSavePath実行時の保存パス指定内容について説明を追加
3
追加
・JVOpen/JVRTOpenの戻り値として-1(該当データ無し)を追加
2003/4/28
1.0.2
β
2
修正
・JVSetUIProperties,JVSetServiceKey,JVSetSaveFlag,JVSetSa
vePathのエラー時の戻りコードを修正
・JVOpenのfromtimeパラメータの省略を不可に修正
2003/4/22
1.0.1
β
2
追加
・JVSetUIPropertiesのダイアログイメージ図を追加
・JVOpenのoptin=3 での呼び出し時に表示されるダイアログイメージ図と
その説明を追加
・JVOpenのoptionパラメータとdataspecパラメータの不正な組み合わせ
について記述を追加
・JVOpenのlasttime パラメータについての説明文を追加
3
修正
「3.コード表」の戻り値と意味を修正
3
追加
・JVOpen/JVRTOpenの戻り値として-303(利用キーが設定されてい
ない)を追加
・JVOpenの戻り値として-115(option パラメータが不正)を追加
・JVOpenの戻り値として-116(dataspec とoption の組み合わせが不
正)を追加
-
新規
初版作成
2003/4/1
1.0β
```
