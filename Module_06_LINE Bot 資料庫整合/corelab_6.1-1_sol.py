import sqlite3

# 連結至資料庫 history.db
connect = sqlite3.connect('Assignment_6-1.db')

# 建立cursor, 以利後續操作
cursor = connect.cursor()

# 建立資料表
# save name, user_id, text
cursor.execute("CREATE TABLE log \
               (id integer primary key, \
                name varchar(20), \
                user_id text, \
                msg text)")
connect.commit()

