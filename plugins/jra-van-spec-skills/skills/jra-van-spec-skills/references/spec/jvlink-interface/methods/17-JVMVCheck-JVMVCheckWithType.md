# JVMVCheck / JVMVCheckWithType

*JRA レーシングビュアー映像公開チェック要求*

### 構文

```
Long JVMVCheck( String 型key );
Long JVMVCheckWithType( String 型movietype , String 型key );
```

### パラメータ

**movietype**

再生を行う映像の種類を指定します。JVMVCheck はJVMVCheckWithType のmovietype に“00”を指定したものと同等です。keyレース映像の公開状況をチェックするレースを指定します。パラメータは、以下のように指定します。種類movietype指定するキー(searchkey)説明レース映像“00”“YYYYMMDDJJRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号パドック映像“01”“YYYYMMDDJJRR”または“YYYYMMDDJJKKHHRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号マルチカメラ映像“02”“YYYYMMDDJJRR”または“YYYYMMDDJJKKHHRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号パトロール映像“03”“YYYYMMDDJJRR”または“YYYYMMDDJJKKHHRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードKK:回次HH:日次RR:レース番号または“YYYYMMDDJJKKHHRR”

### 戻り値

動画公開チェック要求が正しく終了した場合、公開状況を0または1で返ります。公開あり:1公開なし:0※:Movietype、:Key で指定したレースが存在しない場合は-1が返ります。エラーが発生した場合にはエラーの理由コードとしての負の数が返されます。(「3.コード表」参照)※JVOpen/JVRTOpen/JVMVOpen 中は本メソッドを使用できません。オープン中の場合、先にJVClose を呼び出してから使用してください。※1度公開されたパドック動画のレースが中止になった場合、該当レースについて本メソッドを使用すると公開なし:0が返ります。
