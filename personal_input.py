import sqlite3
conn = sqlite3.connect('sample.db')

cur = conn.cursor()

#データの入力
cur.execute("""INSERT INTO personal VALUES
('001','Yamada Taro',173,62.5)""")
cur.execute("""INSERT INTO personal VALUES
('002','Tanaka Hanako',163,53.1)""")
cur.execute("""INSERT INTO personal VALUES
('003','Suzuki Saburo',180,75.8)""")

#コミットしてデータベースに反映される
conn.commit()

conn.close()