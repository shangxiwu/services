import sqlite3

# 連結至資料庫 history.db
connect = sqlite3.connect('history.db')

# 建立cursor, 以利後續操作
cursor = connect.cursor()

# 建立資料表
#cursor.execute("CREATE TABLE log \
#               (id integer primary key, \
 #               name varchar(20), \
 #               user_id text,\
 #               msg text)")
#connect.commit()



#cursor.execute("INSERT INTO log (id, name, user_id, msg) values (1,'Amy', 101, 12345)")
#connect.commit()

log_list = cursor.execute("select * from log")
for log in log_list:
    print(log)