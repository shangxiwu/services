# import flask related
from flask import Flask, request, abort
# import linebot related
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

# import for database
import sqlite3

# create flask server
app = Flask(__name__)
# your linebot message API - Channel access token (from LINE Developer)
line_bot_api = LineBotApi(' ')
# your linebot message API - Channel secret
handler = WebhookHandler(' ')

# connect to database
connect = sqlite3.connect('Assignment_6-3.db')
cursor = connect.cursor()

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    # implement reservation
    if msg == '想看商品種類':
        products = cursor.execute("SELECT * FROM reservation WHERE user_id IS NULL")
        product_text = '尚可預定商品：\n'
        for product in products:
            product_text = product_text + product[1] + ' : ' + product[2] + '\n'
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = product_text))
    elif msg[0:2] == '想買':
        product_name = msg[2:]
        products = cursor.execute("SELECT * FROM reservation")
        found = False
        for product in products:
            if product[1] == product_name:
                found = True
                if product[3] is None:
                    cursor.execute("UPDATE reservation \
                                   SET user_id = ? \
                                   WHERE product = ? ", (user_id, product_name))
                    connect.commit()
                    line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = '已為您預訂完成：' + product_name))
                else:
                    line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = '此商品已被預約！抱歉'))
        if found == False:
            line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = '並沒有此款商品'))
    elif msg == '想取消':
        products = cursor.execute("SELECT * FROM reservation where user_id = ?", (user_id,))
        canceled_product_name = []
        found = False
        for product in products:
            canceled_product_name.append(product[1])
        
        for product in canceled_product_name:
            cursor.execute("UPDATE reservation \
                           SET user_id = ? \
                           WHERE product = ? ", (None, product))
            connect.commit()
            found =  True
        if found == True:
            line_bot_api.reply_message(event.reply_token, 
                                       TextSendMessage(text = '已為您取消預約'))
    else:
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = '親愛的' + user_name + '您好！\n請問需要什麼樣的服務？'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)