# Form1.py

出典: `context/sample1_Python3.14/Form1.py` (SDK Ver.5.0.0 64bit版同梱)

メイン画面。win32com.client.Dispatch("JVDTLab.JVLink") 生成・JVInit・JVSetUIProperties・JVFiledelete を呼ぶ

```python
# ========================================================================
#   JRA-VAN Data Lab. サンプルプログラム１(Form1.py)
# 
# 
#    作成: JRA-VAN ソフトウェア工房  2026年5月19日
# 
# ========================================================================
#    (C) Copyright JRA System Service Co.,Ltd. 2026 All rights reserved
# ========================================================================

# Tkinter（GUI）基本ライブラリ
import tkinter as tk

# 入力ダイアログとスクロール付きテキスト
from tkinter import simpledialog, scrolledtext

# COM（JVLinkを使うため）
import win32com.client

# 別ファイルのダイアログ（Form2）
from Form2 import JVLinkDialog


class MainForm:
    def __init__(self, root):
        # ルートウィンドウを保持
        self.root = root

        # ウィンドウタイトル
        self.root.title("Sample1 Main Form")

        # サイズ固定
        self.root.geometry("626x464")

        # リサイズ不可
        self.root.resizable(False, False)

        # -------------------------
        # JVLink COMオブジェクト生成
        # -------------------------
        try:
            # JRA-VANのCOMコンポーネントを取得
            self.jvlink = win32com.client.Dispatch("JVDTLab.JVLink")
        except Exception as e:
            # 取得失敗時（未インストールなど）
            print(e)
            self.jvlink = None

        # UI作成
        self.create_widgets()

        # JVLink初期化
        self.init_jvlink()

    def create_widgets(self):
        # -------------------------
        # ボタン配置
        # -------------------------

        # データ取込みボタン
        tk.Button(self.root, text="データ取込み",
                  command=self.open_dialog).place(x=16, y=16, width=88, height=32)

        # JVLink設定ボタン
        tk.Button(self.root, text="JVLink設定",
                  command=self.setting).place(x=112, y=16, width=88, height=32)

        # ファイル削除ボタン
        tk.Button(self.root, text="ファイル削除",
                  command=self.delete).place(x=208, y=16, width=88, height=32)

        # テキストクリアボタン
        tk.Button(self.root, text="テキストクリア",
                  command=self.clear).place(x=304, y=16, width=88, height=32)

        # -------------------------
        # ラベル（表示タイトル）
        # -------------------------

        tk.Label(self.root, text="出力").place(x=16, y=96)
        tk.Label(self.root, text="読込みファイルリスト").place(x=400, y=96)

        # -------------------------
        # 出力テキスト欄（左）
        # -------------------------
        # wrap=tk.NONE：折り返ししない
        self.txt_out = scrolledtext.ScrolledText(self.root, wrap=tk.NONE)
        self.txt_out.place(x=16, y=112, width=376, height=336)

        # -------------------------
        # ファイルリスト欄（右）
        # -------------------------
        self.txt_file = scrolledtext.ScrolledText(self.root, wrap=tk.NONE)
        self.txt_file.place(x=400, y=112, width=208, height=336)

    # ------------------------------------------------------------------------------------------------
    # JVLink初期化（JVInit）
    # ------------------------------------------------------------------------------------------------
    def init_jvlink(self):
        # JVLinkが取得できていない場合は何もしない
        if not self.jvlink:
            return

        # ソフトウェアID（固定値）
        sid = "UNKNOWN"

        # -------------------------
        # JVLink初期化
        # -------------------------
        # ※重要：JVInitは最初に1回必ず呼ぶ必要がある
        ret = self.jvlink.JVInit(sid)

        # -------------------------
        # 結果表示
        # -------------------------
        if ret != 0:    # エラー
            self.print_out(f"JVInitエラー:{ret}\n")
        else:           # 正常
            self.print_out(f"JVInit正常:{ret}\n")

    # -------------------------
    # データ取込みダイアログ起動
    # -------------------------
    def open_dialog(self):
        if not self.jvlink:
            return

        # Form2（ダイアログ）を起動
        JVLinkDialog(self, self.jvlink)

    # -------------------------
    # 出力欄に文字追加
    # -------------------------
    def print_out(self, msg):
        self.txt_out.insert(tk.END, msg)  # 末尾に追加
        self.txt_out.see(tk.END)          # 自動スクロール

    # -------------------------
    # ファイルリスト欄に追加
    # -------------------------
    def print_filelist(self, msg):
        self.txt_file.insert(tk.END, msg)   # 末尾に追加
        self.txt_file.see(tk.END)           # 自動スクロール

    # -------------------------
    # JVLink設定画面表示
    # -------------------------
    def setting(self):
        if self.jvlink:
            # JVLinkの設定UI表示
            self.jvlink.JVSetUIProperties()

    # -------------------------
    # ファイル削除処理（JVFiledelete）
    # -------------------------
    def delete(self):
        if not self.jvlink:
            self.print_out("JVLink未初期化\n")
            return
        
        # 入力ダイアログ
        filename = simpledialog.askstring("ファイル削除", "ファイル名を入力してください")
        
        if not filename:
            # 未入力 or キャンセル
            self.print_out(f"JVFiledelete:ファイル名未入力またはキャンセル\n")            
            return
        
        try:
            # JVLinkに削除命令
            ret = self.jvlink.JVFiledelete(filename)
            
            # エラー判定
            if ret != 0:    #エラー
                self.print_out(f"JVFiledeleteエラー:{ret}\n")
            else:           #正常
                self.print_out(f"JVFiledelete正常終了:{ret}\n")

        except Exception as e:
            # COM例外などを表示
            self.print_out(f"例外エラー:{e}\n")
                
    # -------------------------
    # テキストクリア
    # -------------------------
    def clear(self):
        # 出力欄クリア
        self.txt_out.delete("1.0", tk.END)

        # ファイルリストクリア
        self.txt_file.delete("1.0", tk.END)


# -------------------------
# アプリ起動処理
# -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MainForm(root)
    root.mainloop()
```
