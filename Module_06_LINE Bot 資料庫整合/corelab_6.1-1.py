import sqlite3

# 連結至資料庫 history.db
connect = sqlite3.connect('Assignment_6-1.db')

# 建立cursor, 以利後續操作
cursor = connect.cursor()

# 建立資料表
# save name, user_id, text
# write your code here
# ...

cursor.execute("create table game2 \
               id integrate primary key, \
                   product text, \
                   price text    ")
onnect.commit()

