#ライブラリのインポート
import sqlite3

conn = sqlite3.connect('sample.db')

cur = conn.cursor()

for row in cur.execute("SELECT * FROM personal"):
    print(row)

conn.close()