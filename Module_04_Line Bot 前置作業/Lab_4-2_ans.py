
import sqlite3

# 連結資料表
connect = sqlite3.connect('Lab_4-2.db')
cursor = connect.cursor()

# 建立資料表
cursor.execute("CREATE TABLE grades \
              (ID integer primary key, \
               Name varchar(10), \
               Chinese integer, \
               English integer, \
               Pass bit)")
connect.commit()

# ----------------------------------------------------------
# 插入資料至資料表中
cursor.execute("INSERT INTO grades (Name, Chinese, English, Pass) \
                VALUES ('Amy', 90, 85, 1)")
cursor.execute("INSERT INTO grades (Name, Chinese, English, Pass) \
                VALUES ('Jason', 59, 52, 0)")
cursor.execute("INSERT INTO grades (Name, Chinese, English, Pass) \
                VALUES ('King', 99, 99, 1)")

connect.commit()
print('插入多筆資料')

# ----------------------------------------------------------

# 印出目前資料表中資料
print('印出目前表中內容')
grades_list = cursor.execute("SELECT * FROM grades")
for grade in grades_list:
   print(grade)