# JV-Link プロパティ

出典: `context/JV-Linkインターフェース仕様書_4.9.0.1(Win).pdf`

JV-Link が公開するプロパティです。`m_savepath`/`m_servicekey` は設定値、`m_CurrentFileTimestamp` は再開用、`m_TotalReadFilesize` は進捗表示に使います。

| 型 | プロパティ | 説明 |
|---|---|---|
| Integer | m_saveflag | サーバーからダウンロードしたファイルを  m_savepath が示すパスに保存するかどうかのフラグを保持します。0:保存しない1:保存する |
| String | m_savepath | JV-Data を保存するディレクトリへのパスを保持します。JVInit 呼び出し時にレジストリから値がセットされます。JV-Link のインストール直後にはデフォルトで次の値がセットされています。%InstallPath%※%InstallPath%はJRA-VAN Data Lab. SDK がインストールされたパスJV-Data はこのパスの下に作成される”cache”と”data”フォルダに保存されます。値を変更する場合はJVSetSavePath またはJVSetUIProperties を使用します。 |
| String | m_servicekey | JRA-VAN DataLab.サービスを利用する権利を確認するための利用キー(17桁)を保持します。JVInit 呼び出し時にレジストリから値がセットされます。デフォルトでは値が設定されていないので認証出来ません。値を変更する場合はJVSetServiceKey またはJVSetUIProperties を使用します。 |
| String | m_JVLinkVersion | JV-Link のバージョンを4桁数字(例:0100)で保持します。値は変更できません。JV-Link を呼び出すソフトがJV-Linkの特定のバージョン以降でないと動作しないことがわかっている場合に、これをチェックすることで誤動作を防ぐために利用できます。 |
| Long | m_TotalReadFilesize | JVOpen 呼び出しから戻った時にこれから読み込むJV-Data の総データサイズを1024 で割った値がセットされています。(ただし、結果が0 の場合は、1 がセットされます。)値は変更できません。これはJVRead/JVGetsの戻り値に”0”が返るまでに読み取るデータの合計サイズなので、JVRead/JVGets  を使用した読み出し処理全体のプログレスバーの表示のために利用できますが、単位がKB なので注意が必要です。 |
| Long | m_CurrentReadFilesize | JVRead/JVGets で読み込んでいる現在のファイルのサイズがセットされています。値は変更できません。JVOpen 後の最初のJVRead/JVGets 呼び出しでセットされ、JVRead/JVGets の戻り値に”-1”が返されるまで同じ値を維持します。戻り値”-1”の次のJVRead/JVGets 呼び出しで次のファイルのサイズに変更されます。 |
| String | m_CurrentFileTimestamp | JVRead/JVGets で読み込んでいる現在のファイルのタイムスタンプがセットされます。JVOpen 後の最初のJVRead/JVGets 呼び出しでセットされ、JVRead/JVGets の戻り値に”-1”が返されるまで同じ値を維持します。戻り値”-1”の次のJVRead/JVGets 呼び出しで次のファイルのタイムスタンプに変更されます。 |
| Long | ParentHWnd | JV-Link が表示するメッセージダイアログのオーナーウィンドウを設定します。JVOpen/JVRTOpen の呼出前に設定を行って下さい。※:JV-Link Ver2.0.0 以降である必要がありますので、バージョンチェック後に設定を行って下さい。 |
| Integer | m_payflag | 払戻ダイアログを表示するかどうかのフラグを保持します。0:表示する1:表示しない |
