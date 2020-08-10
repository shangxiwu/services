import sqlite3

# 連結至資料庫 game.db
connect = sqlite3.connect('Assignment_6-3.db')

# 建立cursor, 以利後續操作
cursor = connect.cursor()

# 建立資料表
# 模擬 Assignment_6-2 情境
# 儲存 商品名稱、價格與買家ID
cursor.execute("CREATE TABLE reservation \
               (id integer primary key, \
                product text, \
                price text, \
                user_id text)")
connect.commit()


# 填入商品
# 商品    |   價格(w)  |  預定買家(id)
#  ---         ---         ---
# 藍寶石        80           無
# 高級畫像      35           無
# 水晶燈        8            無
# 跑車         200           無
cursor.execute("INSERT INTO reservation (product, price) \
                VALUES ('藍寶石', '80w')")
cursor.execute("INSERT INTO reservation (product, price) \
                VALUES ('高級畫像', '32w')")
cursor.execute("INSERT INTO reservation (product, price) \
                VALUES ('水晶燈', '8w')")
cursor.execute("INSERT INTO reservation (product, price) \
                VALUES ('跑車', '200w')")
connect.commit()


