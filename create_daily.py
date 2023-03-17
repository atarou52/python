import sqlite3

# diary.dbの生成
con = sqlite3.connect('diary.db')

cur  = con.cursor()

# 既にdiary.dbがある場合は削除
cur.execute("DROP TABLE IF EXISTS diary")

# dailyテーブルの生成
cur.execute("""CREATE TABLE diary(date TEXT PRIMARY KEY,
            weather INTEGERk,
            adequacy INTEGER,
            action INTEGER,
            event TEXT)""")
print('diary テーブルを作成しました')

# dailyテーブルへデータを追加
sql = """INSERT INTO diary
       (date, weather, adequacy, action, event)
       VALUES
       ('2023_3_1', 2, 80, 4,'あけまして、おめでとう。')"""
cur.execute(sql)

sql = ("""INSERT INTO diary(date, weather, adequacy, action, event)
       VALUES
       ('2023_3_2', 1, 40, 4, '今日は7時に起きて、久々に町へ出かけた。')""")
cur.execute(sql)

sql = ("""INSERT INTO diary(date, weather, adequacy, action, event)
       VALUES
       ('2023_3_3', 3, 60, 1, 'やっぱり寝坊したけど、ズーム会議は１３時から。')""")
cur.execute(sql)

# dailyテーブルの表示
cur.execute("SELECT * FROM diary")
for row in cur:
    print(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]))
    
con.commit()
con.close()
