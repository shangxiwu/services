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
        products_list = []
        for product, buyer in products.items():
            if buyer is None:
                products_list.append(product)
        product_text = '尚可預定商品：\n'
        for product in products_list:
            product_text = product_text + product + ' : ' + prices[product] + '\n'
        print(product_text)
    elif msg[0:2] == '想買':
        product_name = msg[2:]
        found = False
        for product, buyer in products.items():
            if product == product_name:
                found = True
                if buyer is None:
                    products[product_name] = current_user_id
                    print('已為您預訂：', product)
                else:
                    print('此商品已被預約！抱歉')
        if found == False:
            print('並沒有此款商品')
    elif msg == '想取消':
        for product, buyer in products.items():
            if buyer == current_user_id:
                products[product] = None
                print('已為您取消預訂')
    elif msg == '結束':
        break
    else:
        print('您好！請問需要什麼樣的服務？')
    print('------------------')
        
        