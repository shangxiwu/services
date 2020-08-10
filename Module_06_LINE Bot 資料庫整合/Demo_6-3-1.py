import sqlite3

# 連結至資料庫 game.db
connect = sqlite3.connect('game.db')

# 建立cursor, 以利後續操作
cursor = connect.cursor()

# 建立資料表
cursor.execute("CREATE TABLE reservation \
               (id integer primary key, \
                game text, \
                user_id text)")
connect.commit()

# 填入遊戲
cursor.execute("INSERT INTO reservation (game) \
                VALUES ('小瓦隆')")
cursor.execute("INSERT INTO reservation (game) \
                VALUES ('雨聲')")
cursor.execute("INSERT INTO reservation (game) \
                VALUES ('龍捲風')")
connect.commit()


