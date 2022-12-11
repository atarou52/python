import sqlite3

# diary.dbの生成
con = sqlite3.connect('diary.db')
print('diary.dbを作成しました')

cur  = con.cursor()

# dailyテーブルの生成
cur.execute("""CREATE TABLE daily(date TEXT PRIMARY KEY,
            weather INTEGERk,
            adequacy INTEGER,
            action INTEGER,
            event TEXT)""")
print('daily テーブルを作成しました')

# dailyテーブルへデータを追加
sql = """INSERT INTO daily
       (date, weather, adequacy, action, event)
       VALUES
       ('2022_1_1', 2, 80, 4,'あけまして、おめでとう。')"""
cur.execute(sql)

sql = ("""INSERT INTO daily(date, weather, adequacy, action, event)
       VALUES
       ('2022_1_3', 1, 40, 4, '今日は7時に起きて、久々に町へ出かけた。')""")
cur.execute(sql)

sql = ("""INSERT INTO daily(date, weather, adequacy, action, event)
       VALUES
       ('2022_1_4', 3, 60, 1, 'やっぱり寝坊したけど、ズーム会議は１３時から。')""")
cur.execute(sql)

# dailyテーブルの表示
cur.execute("SELECT * FROM daily")
for row in cur:
    print(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]))
    
con.commit()
con.close()
