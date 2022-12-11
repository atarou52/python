import tkinter as tk
# tkinterはユーザインターフェイスを作成するためのツールキット

import tkinter.ttk as ttk
# ウィンドウの画面設定をするためのツール

import datetime as da

import calendar as ca

from tkinter import messagebox

import csv

import sqlite3
#SELECT文を受け取り１行の結果を返す関数
def select_db(sql):
    con = sqlite3.connect('diary.db')
    cur = con.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    con.close()
    return row

# SELECT文を受け取りすべての結果を返す関数
def select_all(sql):
    con = sqlite3.connect('diary.db')
    cur = con.cursor()
    cur.execute(sql)
    row = cur.fetchall()
    con.close()
    return row

# 日付文字列を作る関数
def make_text_1(y, m, d):
    return str(y) + '年' + str(m) + '月' + str(d) + '日'

def make_text_2(y, m, d):
    return str(y) + '_' + str(m) + '_' + str(d)

# 日付をクリックした際に呼び出す関数
def click(event):
    t = event.widget['text']
    n = str(yer[0]) + '_' + str(mon[0]) + '_' + str(t) 
    v_date = da.date(yer[0], mon[0], t) # クリックした日
    t_date = da.date(yer[1], mon[1], today) # 今日
    if v_date > t_date: #今日よりも後ならエラーメッセージ
        messagebox.showinfo('メッセージ', '未来は閲覧できません。')
        return
    elif v_date == t_date: # 今日ならウィジェットの表示を初期化
        title['text'] = make_text_1(yer[0], mon[0], t) + 'の日記'
        combo.current(0)
        sclH.set(0)
        var.set(0)
        text.delete('1.0', 'end')
        return
    #データがない日はエラーメッセージ
    elif event.widget['background'] != 'gray' :
        messagebox.showinfo('メッセージ', 'データがありません。')
        return
    
    row = select_db("SELECT * FROM daily WHERE date='" + n + "'")
    
    title['text'] = make_text_1(yer[0], mon[0], t) + 'の日記'
    combo.current(row[1])
    sclH.set(row[2])
    var.set(row[3])
    
    text.delete('1.0', 'end')
    text.insert('1.0', row[4])

#　保存ボタンをクリックした際に呼び出される関数
def save(t_day):
    d_1 = combo.current()
    d_2 = sclH.get()
    d_3 = var.get()

    with open('diary.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        # ウィジェットのデータをcsvファイルに書き込む
        writer.writerow([t_day, d_1, d_2, d_3])

    with open(t_day + '.txt', 'w') as f2:
        #テキストフィールドのデータをファイルに書き込む
        f2.write(text.get('1.0', 'end-1c'))

    messagebox.showinfo('メッセージ', 'データを保存しました。')

# データベースに、引数の日付があればTrue、なければFalseを返す関数
def check(y, m, d):
    if (y, m, d) == (yer[0], mon[0], today): #今日の場合はFalse
        return False
    n = make_text_2(y, m, d)
    if select_db("SELECT * FROM daily WHERE date = '"+ n + "'")is not None:
        return True
    return False

# 表示するカレンダーの生成
WEEK_COLUMN = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLOUR = ['red', 'black', 'black', 'black', 'black', 'black', 'blue']

def disp(arg):
    global yer
    global mon
    mon[0] += arg

# 年月表示箇所
    if mon[0] < 1:
        mon[0], yer[0] = 12, yer[0] - 1
    elif mon[0] > 12:
        mon[0], yer[0] = 1, yer[0] + 1
    label['text'] = str(yer[0]) + '年' + str(mon[0]) + '月'

    cal = ca.Calendar(firstweekday=6)
    cal = cal.monthdayscalendar(yer[0], mon[0])

    # print(cal)

    for widget in frame.winfo_children():
        widget.destroy()

    # 曜日出力箇所
    r = 0
    for i,x in enumerate(WEEK_COLUMN):
        label_day = tk.Label(frame,
        text = x,
        font =('', 10),
        width = 3,
        fg = WEEK_COLOUR[i])
        label_day.grid(row = r, column = i, pady = 1)
    
    # 日付の出力箇所
    r = 1
    for week in cal:
        for i, day in enumerate(week):
            #print(day)
            day = ' ' if day == 0 else day
            label_day = tk.Label(frame,
            text = day,
            font=('', 10),
            fg = WEEK_COLOUR[i],
            borderwidth = 1)
            if(yer[0], mon[0], today) == (yer[1], mon[1], day):
                label_day['relief'] = 'solid'
            label_day.bind('<Button-1>', click)
            label_day.grid(row = r, column = i, padx = 2, pady = 1)
        r = r + 1

#トップレベルウインドウの生成(リサイズ不可)
root = tk.Tk()
root.title('日記アプリ')
root.geometry('520x280')
root.resizable(0,0)

#カレンダー用のフレーム
c_frame = tk.Frame(root)
frame = tk.Frame(c_frame)

for n in range(3):
    c_frame.grid_columnconfigure(n, weight=1)

yer = [da.date.today().year] * 2
mon = [da.date.today().month] * 2
today = da.date.today().day

label = tk.Label(c_frame, font = ('', 10))
button_1 = tk.Button(c_frame,
    text = '<',
    font = ('', 10),
    command = lambda:disp(-1))

button_1.grid(row = 0, column = 0, pady = 10)
label.grid(row = 0, column = 1)
button_2 = tk.Button(c_frame,
    text = '>',
    font = ('', 10),
    command = lambda:disp(1))

button_2.grid( row = 0, column = 2)
frame.grid (row = 1, column = 0, columnspan = 3)

disp(0)

# ここから日記用のフレーム
d_frame = tk.Frame(root)

# タイトル保存ボタン
t_frame = tk.Frame(d_frame)
title = tk.Label(t_frame, text = make_text_1(yer[0], mon[0], today) + 'の日記' ,
font = ('', 12))

title.grid(row = 0, column = 0, padx = 20)

button = tk.Button(t_frame, text = '保存',
command = lambda:save(make_text_2(yer[0], mon[0], today)))

button.grid(row = 0, column = 1)

#タイトルと保存ボタンのフレームを日記フレームの１行目に配置
t_frame.grid(row = 0, column =  0, pady = 10)

#天気の選択
weather = select_all("SELECT type FROM weather")

# Label、Combobox,Scaleを配置するフレーム
w_frame = tk.Frame(d_frame)
label_1 = tk.Label(w_frame, text = '今日の天気 :  ', font = ('', 10))
label_1.grid(row = 0, column = 0, sticky = tk.W)
combo = ttk.Combobox(w_frame, state = 'readonly', values = weather)
combo.current(0)
combo.grid(row = 0, column = 1)

# 充実度
label_2 = tk.Label(w_frame, text = '今日の充実度  : ', font = ('', 10))
label_2.grid(row = 1, column = 0, sticky = tk.W)
sclH = tk.Scale(w_frame, orient = tk.HORIZONTAL, from_=1, length = 180)
sclH.grid(row = 1, column = 1)

# Label,Combobox,Scaleを配置するフレームを２行目に配置
w_frame.grid(row = 1, column = 0)

# 行動
r_frame = tk.Frame(d_frame)
action = select_all("SELECT type FROM action")

r_frame.grid_columnconfigure(0, weight=1)
r_frame.grid_columnconfigure(1, weight=1)
r_frame.grid_columnconfigure(2, weight=1)
r_frame.grid_columnconfigure(3, weight=1)
r_frame.grid_columnconfigure(4, weight=1)


var = tk.IntVar()
var.set(0)
for i, act in enumerate(action):
    radio = tk.Radiobutton(r_frame, text = act, variable = var, value = i)

    radio.grid (row=0, column = i)

# ラジオボタンのフレームを４行目に配置
r_frame.grid(row=3, column = 0)

# テキストフィールド
text = tk.Text(d_frame, width = 40, height = 10)

# テキストフィールドは直接日記用フレームに配置
text.grid(row = 4, column=0)
scroll_v = tk.Scrollbar(d_frame, orient = tk.VERTICAL, command = text.yview)

scroll_v.grid(row=4, column = 1, sticky = tk.N + tk.S)
text["yscrollcommand"] = scroll_v.set

# カレンダー用フレームをトップレベルウインドウに配置
c_frame.grid(row=0, column=0, padx=10)

# 日記用のフレームをトップレベルウインドウに配置
d_frame.grid(row=0, column=1)

root.mainloop()