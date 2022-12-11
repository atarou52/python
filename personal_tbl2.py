import sqlite3
conn = sqlite3.connect('sample.db')

cur = conn.cursor()

# personalテーブルがすでにある場合は削除
cur.execute("DROP TABLE IF EXISTS personal")
cur.execute("""CREATE TABLE personal(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    height INTEGER NOT NULL,
    weight REAL NOT NULL)""")

print('personalテーブルを作成しました。')




conn.close()