# JVWatchEvent

*イベント通知開始*

イベント通知開始をおこなうことで、払戻確定、騎手変更、天候馬場状態変更、コース変更、出走取消・競走除外、発走時刻変更、馬体重発表が発表された際、イベントを受理することが可能になります。イベント通知開始およびイベントを受理するには特殊な宣言およびコード記述が必要となります。下記【イベント使用方法】に使用例を記述していますので参考にして下さい。

### 構文

```
Long JVWatchEvent();
```

### パラメータ

なし

### 戻り値

処理が正しく終了した場合はコード0 を返します。エラーが発生した場合にはエラーの理由コードとしての負の数が返されます。(「3.コード表」参照)

### 解説

確定・変更情報が発生した際、イベントを通知するスレッドを開始します。JVInit を行わずにJVWatchEventメソッドを呼び出すとエラーが返ります。【イベント】イベントを受理するためのメソッドは下記の通りになります。【イベント構文】Void  各イベントメソッド名(String 型bstr);受信可能な確定・変更イベントの種類は以下のようになります。種類イベントメソッド名説明払戻確定JVEvtPay払戻確定が発表された際イベントを受理します。騎手変更JVEvtJockeyChange騎手変更が発表された際イベントを受理します。天候馬場状態変更JVEvtWeather天候馬場状態変更が発表された際イベントを受理します。コース変更JVEvtCourseChangeコース変更が発表された際イベントを受理します。出走取消・競走除外JVEvtAvoid出走取消・競走除外が発表された際イベントを受理します。発走時刻変更JVEvtTimeChange発走時刻変更が発表された際イベントを受理します。馬体重発表JVEvtWeight馬体重が発表された際イベントを受理します。

### パラメータ

**bstr**

JVRTOpen に渡すためのパラメータが返されます。確定・変更イベントから返されるパラメータは以下のようになります。イベントメソッド名パラメータ説明JVEvtPay“YYYYMMDDJJRR”YYYY:開催年MM:開催月DD:開催日JJ:場コードRR:レース番号JVEvtWeightJVEvtJockeyChange“TTYYYYMMDDJJRRNNNNNNNNNNNNNN”TT:レコード種別IDYYYY:開催年MM:開催月DD:開催日JJ:場コードRR:レース番号NNNNNNNNNNNNNN:送信年月日JVEvtWeatherJVEvtCourseChangeJVEvtAvoidJVEvtTimeChange【イベント使用方法】※以下のコードはVisualBasic6 での使用例となります。‘WithEvents 付きでインターフェイスを宣言Friend WithEvents InterfaceJVLink As JVDTLabLib.JVLinkDim ReturnCode As Long‘JV-Link 返値InterfaceJVLink = New JVDTLabLib.JVLink‘オブジェクトインスタンスを作成ReturnCode = InterfaceJVLink.JVWatchEvent()‘イベント通知スレッド開始‘上記の手順を踏みJVWatchEvent メソッドを行うことにより、‘下記のようなイベント通知を受信するメソッドを使用することが出来るようになります。‘払戻確定イベントが発生した際の例を下記に記述します。Private Sub InterfaceJVLink _JVEvtPay(ByVal bstr As String)Handles InterfaceJVLink JVEvtPay‘払戻確定イベントが発生した際に行いたい処理をここに記述ReturnCode = frmMain.JVLink1.JVRTOpen("0B12", bstr)End Sub‘イベントが発生した際の処理を上記メソッドの中に記述してください。‘第一引数のbstr をkey としてJVRTOpen※1 に渡すことで対象リアルタイム系データを‘取得することが出来ます。※1:各イベントから返されるパラメータをkey にJVRTOpen を使用する場合イベント通知を受信するメソッドから返されるパラメータをkey としてJVRTOpen を使用する場合は、Dataspecを以下のように指定してください。種類Dataspec払戻確定0B12騎手変更0B16天候馬場状態変更0B16コース変更0B16出走取消・競走除外0B16発走時刻変更0B16馬体重発表0B11
