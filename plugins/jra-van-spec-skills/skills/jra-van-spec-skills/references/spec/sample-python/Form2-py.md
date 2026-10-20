# Form2.py

出典: `context/sample1_Python3.14/Form2.py` (SDK Ver.5.0.0 64bit版同梱)

データ取込みダイアログ。別スレッドで JVOpen → JVStatus → JVGets (cp932 デコード) / JVRead → JVCancel / JVClose を呼ぶ

```python
# ========================================================================
#   JRA-VAN Data Lab. サンプルプログラム１(Form2.py)
# 
# 
#    作成: JRA-VAN ソフトウェア工房  2026年5月19日
# 
# ========================================================================
#    (C) Copyright JRA System Service Co.,Ltd. 2026 All rights reserved
# ========================================================================

# Tkinter GUIライブラリ
import tkinter as tk

# ttk（Progressbarなど拡張Widget）
from tkinter import ttk

# スレッド（非同期処理）
import threading

# スリープ（ポーリング用）
import time


class JVLinkDialog:
    def __init__(self, owner, jvlink):
        # 親フォーム（MainForm）
        self.owner = owner

        # JVLink COMオブジェクト
        self.jvlink = jvlink

        # -------------------------
        # 状態管理変数
        # -------------------------

        # キャンセルフラグ（中止ボタン用）
        self.cancel_flag = False

        # 読込み対象ファイル数（JVOpenで取得）
        self.read_count = 0

        # ダウンロード対象ファイル数（JVOpenで取得）
        self.download_count = 0

        # -------------------------
        # ウィンドウ作成
        # -------------------------
        self.win = tk.Toplevel()

        # タイトル
        self.win.title("Sample1 JVLink Dialog")

        # サイズ固定
        self.win.geometry("506x198")

        # リサイズ不可
        self.win.resizable(False, False)

        # UI構築
        self.create_widgets()

    # -------------------------------
    # UI設定
    # -------------------------------
    def create_widgets(self):
        # ファイル識別子ラベル
        tk.Label(self.win, text="ファイル識別子").place(x=16, y=16)

        # 入力欄（DataSpec）
        self.txt_dataspec = tk.Entry(self.win, width=30)
        self.txt_dataspec.place(x=16, y=32)

        # FROM日付ラベル
        tk.Label(self.win, text="データ提供日FROM").place(x=248, y=16)

        # FROM日付入力
        self.txt_fromdate = tk.Entry(self.win, width=15)
        self.txt_fromdate.place(x=248, y=32)

        # -------------------------
        # ラジオボタン（取得データ種別）
        # -------------------------

        # IntVarで選択状態管理
        self.option = tk.IntVar(value=1)

        # グループボックス
        frame = tk.LabelFrame(self.win, text="取得データ")
        frame.place(x=16, y=56, width=352, height=48)

        # 通常データ
        tk.Radiobutton(frame, text="通常データ",
                       variable=self.option, value=1).place(x=8, y=4)

        # 今週開催データ
        tk.Radiobutton(frame, text="今週開催データ",
                       variable=self.option, value=2).place(x=100, y=4)

        # セットアップデータ
        tk.Radiobutton(frame, text="セットアップデータ",
                       variable=self.option, value=3).place(x=220, y=4)

        # -------------------------
        # ボタン
        # -------------------------

        # データ取込み開始
        tk.Button(self.win, text="データ取込み開始",
                  command=self.start).place(x=392, y=16, width=104, height=32)

        # データ取込み中止
        tk.Button(self.win, text="データ取込み中止",
                  command=self.cancel).place(x=392, y=56, width=104, height=32)

        # -------------------------
        # プログレスバー
        # -------------------------

        tk.Label(self.win, text="ダウンロード").place(x=16, y=112)

        # ダウンロード進捗
        self.pb_download = ttk.Progressbar(self.win, length=352)
        self.pb_download.place(x=16, y=128)

        tk.Label(self.win, text="読込み").place(x=16, y=152)

        # 読込み進捗
        self.pb_read = ttk.Progressbar(self.win, length=352)
        self.pb_read.place(x=16, y=168)

    # -------------------------------
    # 開始ボタン押下
    # -------------------------------
    def start(self):
        # 別スレッドで実行（GUIフリーズ防止）
        threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        try:
            self.cancel_flag = False

            # 入力値取得
            dataspec = self.txt_dataspec.get()
            fromdate = self.txt_fromdate.get()
            option = self.option.get()

            # 開始ログ
            self.owner.print_out("JVOpen開始\n")

            # -------------------------
            # JVOpen実行
            # -------------------------
            ret = self.jvlink.JVOpen(dataspec, fromdate, option,0,0,"")

            # 戻り値がタプルの場合（環境差対応）
            if isinstance(ret, (list, tuple)):
                open_code = ret[0]
                self.read_count = int(ret[1] or 0)
                self.download_count = int(ret[2] or 0)
                self.lastfiletime = str(ret[3] or "")
            else:
                open_code = ret

            # -------------------------
            # 結果判定
            # -------------------------
            if open_code == 0:      #正常
                self.owner.print_out(
                    f"JVOpen正常 Read={self.read_count} Download={self.download_count}\n"
                )
            elif open_code == -1:   #該当データなし
                self.owner.print_out(f"該当データなし:{open_code}\n")
            else:                   #エラー
                self.owner.print_out(f"JVOpenエラー:{open_code}\n")
                return

            # -------------------------
            # ダウンロード0件の場合
            # -------------------------
            if self.download_count == 0:
                self.pb_download["maximum"] = 1
                self.pb_download["value"] = 1

                self.win.title("ダウンロード完了")

                self.read_data()
                self.close()
                return

            # -------------------------
            # ダウンロード進捗管理
            # -------------------------
            self.pb_download["maximum"] = self.download_count

            while True:
                if self.cancel_flag:
                    # UI更新はafter必須
                    self.win.after(0, lambda: self.win.title("JVCancel:キャンセルされました"))
                    return

                # 現在ダウンロード数取得
                status = self.jvlink.JVStatus()

                if status < 0:
                    self.owner.print_out(f"JVStatusエラー:{status}\n")
                    return

                # 進捗バー更新（afterでメインスレッド実行）
                self.win.after(0, lambda s=status: self.pb_download.configure(value=s))

                # タイトル更新
                self.win.after(0, lambda s=status:self.win.title(f"ダウンロード中... ({s}/{self.download_count})"))

                # 完了判定
                if status >= self.download_count:
                    break

                time.sleep(0.3)

            # 完了表示
            self.win.after(0, lambda:self.win.title(f"ダウンロード完了 ({self.download_count}/{self.download_count})"))

            # 読込み処理へ
            self.read_data()
            self.close()

        except Exception as e:
            print(e)

    # -------------------------------
    # ファイル読込（JVGets or JVRead）
    # -------------------------------
    def read_data(self):
        try:
            # 読込済みカウント
            readed = 0

            # 最大件数セット
            self.pb_read["maximum"] = self.read_count

            # タイトル初期化
            self.win.after(0, lambda: self.win.title(f"読込み中...(0/{self.read_count})"))

            while True:
                if self.cancel_flag:
                    self.win.after(0, lambda: self.win.title("JVCancel:キャンセルされました"))
                    return

                buffsize = 110000

                # バッファ
                buff = bytearray(buffsize)

                # ファイル名格納用
                buffname = bytearray()

                # JVデータ取得（JVGets or JVRead）
                ret, memview, fname = self.jvlink.JVGets(buff, buffsize, buffname)
                # ret, buff, size, fname = self.jvlink.JVRead(buff, buffsize, buffname)

                ret = int(ret)

                if ret > 0:
                # 使用するメソッドによって下記の処理をコメントアウトしてください。

                #------------JVGetsを使用する場合--------------
                    # バイトデータ取得
                    raw: bytes = memview.tobytes()                    
                    # データ本体（cp932でデコード）
                    text = raw.decode("cp932", errors="replace")
                    self.owner.print_out(text)
                #---------------------------------------------

                #------------JVReadを使用する場合---------------
                    # self.owner.print_out(buff)
                #---------------------------------------------

                elif ret == -1:
                    # ファイル切替
                    readed += 1

                    # プログレス更新
                    self.win.after(0, lambda r=readed: self.pb_read.configure(value=r))

                    # タイトル更新
                    self.win.after(0, lambda r=readed:self.win.title(f"読込み中... ({r}/{self.read_count})"))

                    # ファイル名出力
                    self.owner.print_filelist(fname + "\n")

                elif ret == 0:
                    # EOF（読込終了）
                    self.owner.print_out("JVGets EndOfFile\n")

                    self.win.after(0, lambda:self.win.title(f"読込み完了 ({readed}/{self.read_count})"))
                    break

                else:
                    # エラー
                    self.owner.print_out(f"JVGetsエラー:{ret}\n")
                    break

        except Exception as e:
            print(e)

    # -------------------------------
    # キャンセル処理
    # -------------------------------
    def cancel(self):
        self.cancel_flag = True
        try:
            self.jvlink.JVCancel()
        except:
            pass

        self.owner.print_out("JVCancel:キャンセルされました\n")

    # -------------------------------
    # JVClose（終了処理）
    # -------------------------------
    def close(self):
        try:
            ret = self.jvlink.JVClose()
            self.owner.print_out(f"JVClose正常終了:{ret}\n")
        except:
            pass
```
