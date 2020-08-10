
import sqlite3
'''
此檔案提供給老師重新創建 .db 檔案
'''

# 建立資料庫
connect = sqlite3.connect('Assignment_4-2-x.db')
cursor = connect.cursor()


# 建立資料表
cursor.execute("CREATE TABLE friends \
              (ID integer primary key, \
               Name varchar(10) UNIQUE, \
               Favorite_fruit text, Age integer)")
connect.commit()


# ----------------------------------------------------------
# 插入資料至資料表中
cursor.execute("INSERT INTO friends (Name, Favorite_fruit, Age) \
                VALUES ('Amy', 'apple', 12)")
cursor.execute("INSERT INTO friends (Name, Favorite_fruit, Age) \
                VALUES ('Jason', 'lemon', 14)")
cursor.execute("INSERT INTO friends (Name, Favorite_fruit, Age) \
                VALUES ('Hanna', 'pineapple', 9)")
cursor.execute("INSERT INTO friends (Name, Favorite_fruit, Age) \
                VALUES ('Coco', 'tomato', 8)")

connect.commit()

# ----------------------------------------------------------

# 印出存於資料表之資料
get_friends = cursor.execute("SELECT * FROM friends")
for friend in get_friends:
   print(friend)