import sqlite3

conn = sqlite3.connect('sample.db')

cur = conn.cursor()

# idが、'002'と等しい行抽出
for row in cur.execute("SELECT * FROM personal WHERE id = '002'"):
    print(row)
    print() # 改行

conn.close()