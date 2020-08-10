
import sqlite3

# 連結資料表
connect = sqlite3.connect('Lab_4-2.db')
cursor = connect.cursor()

# 建立資料表
cursor.execute(" ")     # write your code here
connect.commit()

# ----------------------------------------------------------
# 插入資料至資料表中
cursor.execute(" ")     # write your code here
cursor.execute(" ")     # write your code here
cursor.execute(" ")     # write your code here

connect.commit()
print('插入多筆資料')

# ----------------------------------------------------------

# 印出目前資料表中資料
print('印出目前表中內容')
grades_list = cursor.execute(" ")   # write your code here
for grade in grades_list:
   print(grade)