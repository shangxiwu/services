import sqlite3

# 連結資料庫
connect =                            # write your code here, connect to Assignment_4-2-3.db
cursor = connect.cursor()

def print_table():
    friends_list = cursor.execute("SELECT * FROM friends")
    for friend in friends_list:
       print(friend)
    print('---')

# 原始樣貌
print_table()

# 印出 age > 10 的資料
old_friends = cursor.execute(" ")    # write your code here
for friend in old_friends:
    print(friend)


