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
line_bot_api = LineBotApi('0AbwG/gL7jV1HInV5Utal90/ckOnbrdfWJCNYU5xkzyaFkL8R0nFOBjO+RCPJmvdgV3HAZBqgbH/L7rZNrOkX8h0DSkNFrbX8U5nrY+yDjKtDX3YgjVJDLq3itOWd9q2eqLyIX7zDvAqvC6u+0R8MwdB04t89/1O/w1cDnyilFU=')
# your linebot message API - Channel secret
handler = WebhookHandler('42a6bce6ba72c528632273839ec2799f')



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
connect = sqlite3.connect('history.db',check_same_thread=False)
cursor = connect.cursor()

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    
# connect to database

    # fetch log & save to text
    if msg == '想看歷史訊息':
        logs = cursor.execute("SELECT * FROM log")
        log_text = ''
        for log in logs:
            log_text = log_text + '\n' + str(log)
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = log_text))
    else:
        # save into database
        cursor.execute("INSERT INTO log (name, user_id, msg) \
                           VALUES (?, ?, ?)", (user_name, user_id, msg))
        connect.commit()
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = '已收到您的訊息！'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)