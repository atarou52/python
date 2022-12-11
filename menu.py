import sqlite3
import tkinter as tk
from tkinter import messagebox

# 保存メニューがクリックされると呼び出される関数
def save():
    messagebox.showinfo('メッセージ', '保存メニューです。')
    
# 削除メニューがクリックされると呼び出される関数
def delete():
    messagebox.showinfo('メッセージ', '削除メニューです。')
    
# 検索メニューがクリックされると呼び出される関数
def search():
    messagebox.showinfo('メッセージ', '検索メニューです。')
    
# トップレベルウインドウの生成
root = tk.Tk()
root.geometry('320x220')
root.title('メニューテスト')

# メニューバーを作成・セット
men = tk.Menu(root)
root.config(menu=men)
# 操作メニューを作成・セット
menu_command = tk.Menu(root)
men.add_cascade(label='操作', menu=menu_command)
# 操作メニューに、保存、削除、検索メニューを追加する
menu_command.add_command(label='保存', command=save)
menu_command.add_separator()
menu_command.add_command(label='削除', command=delete)
menu_command.add_separator()
menu_command.add_command(label='検索', command=search)

root.mainloop()