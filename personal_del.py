import sqlite3
conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#personalテーブルの削除
cur.execute("DROP TABLE personal")

conn.close