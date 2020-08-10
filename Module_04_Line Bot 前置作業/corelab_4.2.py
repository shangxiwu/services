import sqlite3

# 連結資料庫
connect = sqlite3.connect('Assignment_4-2-2.db')      # write your code here, connect to Assignment_4-2-2.db
cursor = connect.cursor()

def print_table():
    friends_list = cursor.execute("SELECT * FROM friends")
    for friend in friends_list:
       print(friend)
    print('---')

# 原始樣貌
print_table()

# 刪除 id 為 3 與 4 之資料
cursor.execute("DELETE FROM friends \
                WHERE id = 3 or id = 4")    # write your code here
connect.commit()
print_table()

# 加入 新資料
# Name : Zoe
# Favorite_fruit : banana
# Age : 13
cursor.execute("INSERT INTO friends (Name, Favorite_fruit, Age) \
                VALUES ('Zoe', 'banana', 13)")      # write your code here
connect.commit()
print_table()
