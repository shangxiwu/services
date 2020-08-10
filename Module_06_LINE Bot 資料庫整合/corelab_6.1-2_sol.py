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
connect = sqlite3.connect('Assignment_6-1.db')
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
    
    # 當用戶輸入「秀xxx」，xxx為用戶姓名
    # 回覆 所有存於資料庫，來自 xxx 的訊息
    # 若 xxx 不存在於資料庫，則回覆「該用戶無任何訊息」
    if msg[0:1] == '秀':
        target_name = msg[1:]
        logs = cursor.execute("SELECT * FROM log WHERE name = ?", (target_name,))
        log_text = ''
        found = False
        for log in logs:
            log_text = log_text + '\n' + str(log)
            found = True
        if found == True:
            line_bot_api.reply_message(event.reply_token, 
                                       TextSendMessage(text = log_text))
        else:
            line_bot_api.reply_message(event.reply_token, 
                                       TextSendMessage(text = '該用戶無任何訊息'))
    else:
        # save into database
        # 儲存 user_name, uesr_id, msg
        cursor.execute("INSERT INTO log (name, user_id, msg) \
                           VALUES (?, ?, ?)", (user_name, user_id, msg))
        connect.commit()
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = '已收到您的訊息！'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)