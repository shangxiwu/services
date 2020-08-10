import sqlite3

# 連結至資料庫 mydatabase.db
connect = sqlite3.connect('mydatabase.db')

# 建立cursor, 以利後續操作
cursor = connect.cursor()


# 建立資料表
#cursor.execute("CREATE TABLE users \
#               (id integer primary key, \
#                name varchar(20) UNIQUE, \
#                email text NOT NULL, age integer)")
#connect.commit()


# ----------------------------------------------------------
# 插入資料至資料表中
#cursor.execute("INSERT INTO users (name, email, age) \
#                 VALUES ('John', 'yoyo@123.com', 30)")
#cursor.execute("INSERT INTO users (name, email, age) \
#                 VALUES ('Allen', 'hello@123.com', 25)")
#cursor.execute("INSERT INTO users (name, email, age) \
#                 VALUES ('Amy', 'girl@123.com', 20)")
#connect.commit()
#print('插入多筆資料')

# ----------------------------------------------------------

# 搜尋存於資料表中之資料
#print('印出目前表中內容')
#get_users = cursor.execute("SELECT * FROM users")
#for user in get_users:
#    print(user)

# ----------------------------------------------------------

# 更新特定使用者的 email, age
#cursor.execute("UPDATE users \
#               SET email = 'nono@456.com', age = 28 \
#               WHERE id = 3")
#connect.commit()
#print('更新 id 為 3 的使用者資訊')
#
#print('印出更新使用者後之表中內容')
#get_users = cursor.execute("SELECT * FROM users")
#for user in get_users:
#    print(user)

# ----------------------------------------------------------

# 刪除特定筆資料
#cursor.execute("DELETE FROM users WHERE id = 3")
#connect.commit()
#print('刪除 id 為 3 的使用者')
#
#print('印出刪除使用者後之表中內容')
#get_users = cursor.execute("SELECT * FROM users")
#for user in get_users:
#    print(user)

