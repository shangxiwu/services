
# create games dictionary
games =         # write your code here

# run for 100 times
for i in range(1, 100):
    
    msg = input('輸入訊息：')
    current_user_id = '123abc'
    
    # implement reservation
    if msg == '想看遊戲種類':
        game_list = []
        # write your code here
        # ...
    elif msg[0:3] == '想預約':
        game_name = msg[3:]
        found = False
        # write your code here
        # ...
    elif msg == '想取消預約':
        # write your code here
        # ...
    elif msg == '結束':
        break
    else:
        print('您好！請問需要什麼樣的服務？')
    print('------------------')
        
        