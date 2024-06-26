import tkinter as tk
from tkinter import filedialog
import zipfile
import os

def zip_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        zip_filename = os.path.basename(folder_path) + ".zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))

        result_label.config(text="フォルダがZIPファイルに圧縮されました")

def zip_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        zip_filename = os.path.splitext(file_path)[0] + ".zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path))

        result_label.config(text="ファイルがZIPファイルに圧縮されました")

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("フォルダ/ファイルをZIP化する")

# ボタンを配置
folder_button = tk.Button(root, text="フォルダを選択してZIP化", command=zip_folder)
folder_button.pack(pady=10)

file_button = tk.Button(root, text="ファイルを選択してZIP化", command=zip_file)
file_button.pack(pady=10)

# 結果を表示するラベル
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
