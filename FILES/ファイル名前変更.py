import os
from tkinter import *
from tkinter import filedialog

def rename_files(directory, old_text, new_text):
    for filename in os.listdir(directory):
        if old_text in filename:
            new_filename = filename.replace(old_text, new_text)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, END)
    directory_entry.insert(END, directory)

def rename():
    directory = directory_entry.get()
    old_text = old_text_entry.get()
    new_text = new_text_entry.get()
    if directory and old_text and new_text:
        rename_files(directory, old_text, new_text)
        status_label.config(text="ファイルが正常にリネームされました！")
    else:
        status_label.config(text="すべてのフィールドに記入してください。")

# Create GUI
root = Tk()
root.title("ファイル名前変更")

directory_label = Label(root, text="ディレクトリ:")
directory_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

directory_entry = Entry(root, width=50)
directory_entry.grid(row=0, column=1, columnspan=2, pady=5)

browse_button = Button(root, text="参照", command=browse_directory)
browse_button.grid(row=0, column=3, pady=5)

old_text_label = Label(root, text="古いテキスト:")
old_text_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

old_text_entry = Entry(root, width=50)
old_text_entry.grid(row=1, column=1, columnspan=2, pady=5)

new_text_label = Label(root, text="新しいテキスト:")
new_text_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

new_text_entry = Entry(root, width=50)
new_text_entry.grid(row=2, column=1, columnspan=2, pady=5)

rename_button = Button(root, text="ファイルをリネーム", command=rename)
rename_button.grid(row=3, column=1, pady=10)

status_label = Label(root, text="")
status_label.grid(row=4, column=0, columnspan=4)

root.mainloop()
