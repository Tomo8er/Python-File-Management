import os
import tkinter as tk
from tkinter import filedialog, scrolledtext

def list_files_with_size(directory):
    result = ""
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            filesize = os.path.getsize(filepath)
            result += f"{filepath} - {filesize} bytes\n"
    return result

def show_file_sizes():
    directory = filedialog.askdirectory(title="ディレクトリを選択してください")
    if directory:
        file_sizes = list_files_with_size(directory)
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, file_sizes)

# Tkinter GUIの設定
root = tk.Tk()
root.title("ファイルサイズ表示")
root.geometry("400x300")

# ボタン
select_button = tk.Button(root, text="ディレクトリを選択", command=show_file_sizes)
select_button.pack(pady=10)

# テキストエリア
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=15)
text_area.pack(padx=10, pady=10)

root.mainloop()
