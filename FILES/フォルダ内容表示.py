import os
import tkinter as tk
from tkinter import filedialog, messagebox

def show_subfolders(folder_path):
    result = folder_path + "\n"
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            result += os.path.join(root, file) + "\n"
        for dir in dirs:
            result += os.path.join(root, dir) + "\n"
    return result

def select_folder():
    folder_path = filedialog.askdirectory(title="ディレクトリを選択してください")
    if folder_path:
        result = show_subfolders(folder_path)
        messagebox.showinfo("結果", result)

# Tkinter GUIの設定
root = tk.Tk()
root.title("ディレクトリの内容を表示")
root.geometry("300x150")

select_button = tk.Button(root, text="ディレクトリを選択", command=select_folder)
select_button.pack(expand=True)

root.mainloop()
