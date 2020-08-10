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
    MessageEvent, TextMessage, TextSendMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage
)

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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    # print msg details as log
    print('用戶名 : ', user_name)
    print('用戶ID : ', user_id)
    print('用戶訊息 : ', msg)

# run app
if __name__ == "__main__":
    # using port 11111, 
    # please resetting your webhook by restart ngrok, set it in LINE page
    app.run(host='127.0.0.1', port=12345)