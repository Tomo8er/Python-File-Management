import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

def select_source_folder():
    source_folder = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_folder)

def select_destination_folder():
    destination_folder = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination_folder)

def backup_folder():
    source_folder = source_entry.get()
    destination_folder = destination_entry.get()

    if not source_folder:
        messagebox.showwarning("Warning", "ソースフォルダを選択してください。")
        return
    
    if not destination_folder:
        messagebox.showwarning("Warning", "バックアップ先フォルダを選択してください。")
        return

    try:
        destination_folder = os.path.join(destination_folder, os.path.basename(source_folder))
        shutil.copytree(source_folder, destination_folder)
        messagebox.showinfo("Success", "フォルダのバックアップが完了しました。")
    except Exception as e:
        messagebox.showerror("Error", f"エラーが発生しました: {e}")

app = tk.Tk()
app.title("フォルダバックアップ")

tk.Label(app, text="ソースフォルダ:").grid(row=0, column=0, padx=10, pady=5)
source_entry = tk.Entry(app, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=5)
source_button = tk.Button(app, text="選択", command=select_source_folder)
source_button.grid(row=0, column=2, padx=10, pady=5)

tk.Label(app, text="バックアップ先フォルダ:").grid(row=1, column=0, padx=10, pady=5)
destination_entry = tk.Entry(app, width=50)
destination_entry.grid(row=1, column=1, padx=10, pady=5)
destination_button = tk.Button(app, text="選択", command=select_destination_folder)
destination_button.grid(row=1, column=2, padx=10, pady=5)

backup_button = tk.Button(app, text="バックアップ開始", command=backup_folder)
backup_button.grid(row=2, columnspan=3, pady=10)

app.mainloop()
