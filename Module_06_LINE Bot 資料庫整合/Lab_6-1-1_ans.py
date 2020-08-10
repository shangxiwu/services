import sqlite3

# 連結至資料庫 history.db
connect = sqlite3.connect('Lab_6-1.db')

# 建立cursor, 以利後續操作
cursor = connect.cursor()

# 建立資料表
cursor.execute("CREATE TABLE log \
               (id integer primary key, \
                name varchar(20), \
                msg text)")
connect.commit()

