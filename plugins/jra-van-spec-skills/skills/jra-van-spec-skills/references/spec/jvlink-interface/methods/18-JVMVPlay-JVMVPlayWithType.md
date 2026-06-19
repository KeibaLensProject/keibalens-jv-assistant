# JVMVPlay / JVMVPlayWithType

*JRA レーシングビュアー映像再生要求*

### 構文

```
Long JVMVPlay( String 型key);
Long JVMVPlayWithType( String 型movietype , String 型key );
```

### パラメータ

**movietype**

再生を行う映像の種類を指定します。JVMVPlay はJVMVPlayWithType のmovietype に“00”を指定したものと同等です。

**key**

再生するレース映像を指定します。JVMVPlayWithType では、movietype の指定によりパラメータの設定内容が異なります。種類movietype指定するキー(key)説明レース映像“00”“YYYYMMDDJJKKHHRRTT”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号TT:動画種別パドック映像“01”“YYYYMMDDJJKKHHRR”または“YYYYMMDDJJRRTT”または“YYYYMMDDJJKKHHRR”または“YYYYMMDDJJRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号マルチカメラ映像“02”“YYYYMMDDJJKKHHRR”または“YYYYMMDDJJRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号パトロール映像“03”“YYYYMMDDJJKKHHRR”または“YYYYMMDDJJRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号または“YYYYMMDDJJRR”調教映像“11”または“YYYYMMDDNNNNNNNNNN”YYYY:調教実施年MM:調教実施月DD:調教実施日NNNNNNNNNN:血統登録番号“12”または“13”WMV 形式の動画の場合のみ、TTには以下のオプションが指定可能です。MP4 形式の動画の場合にTT を指定しても再生は可能ですが、画質は常に一定となります。(MP4 形式の場合、TT 以降はJV-Link では認識されません)TT=01高解像度版を優先して再生TT=02通常版を優先して再生指定なし高解像度版を優先して再生上記以外エラー

### 戻り値

映像再生要求が正しく終了した場合、0が返ります。エラーが発生した場合にはエラーの理由コードとしての負の数が返されます。(「3.コード表」参照)

### 解説

key で指定したレース映像の再生を行います。具体的には以下の処理を行います。・JRA レーシングビュアー連携機能が利用可能なソフトウェアであるかの認証を行います。・指定した映像が公開されている場合、映像の再生を行います。映像の再生はHTML5 Player (MP4 形式の場合)を利用して行います。再生するブラウザはJV-Link 設定画面の動画再生ブラウザにて設定した「Microsoft Edge」「Google Chrome」「IE」のいずれかになります。レース映像については、JVMVCheck メソッドもしくはJVMVCheckWithType メソッドを利用する事で、レース映像の公開状況を判別する事が可能となります。JVMVCheck もしくはJVMVCheckWithTypeと組み合わせてご利用下さい。パドック映像、マルチカメラ映像、パトロール映像については、JVMVCheckWithType メソッドを利用する事で、パドック動画、マルチカメラ動画、パトロール動画の公開状況を判別する事が可能となります。JVMVCheckWithType と組み合わせてご利用下さい。※1度公開されたパドック動画のレースが中止になった場合、該当のレースについて本メソッドを使用すると該当データ無し:-1が返ります。調教映像については、JVMVOpen で対象映像を指定し、JVMVRead で公開中の調教映像のkeyが取得可能です。取得したkey をJVMVPlayWithType に設定して下さい。また、movietype については”11”、”12”、”13”どれを指定しても再生される映像は同じです。※JVOpen/JVRTOpen/JVMVOpen 中は本メソッドを使用できません。オープン中の場合、先にJVClose を呼び出してから使用してください。

### 補足

当メソッドを利用するためには、JRA レーシングビュアー連携機能利用申請が必要になります。(未申請の場合、戻り値に-304 が返されます。)詳細についてはJRA-VANホームページのソフト作者サポートページを参照ください。※当メソッドを使用した開発を行う際には、JVInit メソッドにてソフトウェアID に"SA000000/SD000004"をセットしていただくことで当メソッドを利用可能となります。パトロール映像については、通常、各レース終了からおよそ40 分後に更新されます。マルチカメラ映像については、通常、レース終了後の翌月曜日の午後に更新されます。
