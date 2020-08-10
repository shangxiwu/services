import sqlite3

# 連結資料庫
connect =                               # write your code here, connect to Assignment_4-2-1.db
cursor = connect.cursor()

def print_table():
    friends_list = cursor.execute("SELECT * FROM friends")
    for friend in friends_list:
       print(friend)
    print('---')

# 原始樣貌
print_table()

# 將 Amy 的 Favorite_fruit 改為 papaya
cursor.execute(" ")                     # write your code here
connect.commit()

# 印出資料
print_table()