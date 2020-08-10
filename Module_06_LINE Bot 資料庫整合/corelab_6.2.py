'''
# 請實作拍賣系統：
用戶可以透過系統訂購出售之商品

## 模擬情境：
輸入：想看商品種類
    - 獲取尚未被預訂之商品名稱及價格
輸入：想買xxx
    - xxx 為商品名
    - 若該商品存在於清單中：
        - 若該商品尚未被預約：
            - 將此商品設定為屬於目前用戶
        - 若該商品已被預約：
            - 告知此商品已被預定
    - 若該商品不存在於清單中：
        - 告知用戶此商品不存在
輸入：想取消
    - 搜尋該用戶是否有預定之商品
        - 若有：
            - 取消所有該用戶預定之所有商品
            - 告知已取消
輸入：結束
    - 結束程式

## 資料格式：
 商品    |   價格(w)  |  預定買家(id)
 ---         ---         ---
藍寶石        80           無
高級畫像      35           無
水晶燈        8            無
跑車         200           無

'''

# create dictionary to store buyer info
products = {'藍寶石' : None, 
         '高級畫像' : None,
         '水晶燈' : None,
         '跑車' : None}

# create dictionary to store prices
prices = {'藍寶石' : '80w', 
         '高級畫像' : '35w',
         '水晶燈' : '8w',
         '跑車' : '200w'}

# run for 100 times
for i in range(1, 100):
    
    msg = input('輸入訊息：')
    current_user_id = '123abc'
    
    # implement reservation
    if msg == '想看商品種類':
        # write your code here
        # ...
    elif msg[0:2] == '想買':
        product_name = msg[2:]
        found = False
        # write your code here
        # ...
    elif msg == '想取消':
        # write your code here
        # ...
    elif msg == '結束':
        break
    else:
        print('您好！請問需要什麼樣的服務？')
    print('------------------')
        
        