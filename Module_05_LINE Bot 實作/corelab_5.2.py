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
line_bot_api = LineBotApi(' ')
# your linebot message API - Channel secret
handler = WebhookHandler(' ')

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
    # get message
    msg = event.message.text
    
    # write your code here : 使用邏輯判斷式 if...elif..else 完成以下程式
    # 若收到訊息 '我要預約'，則回覆一則文字訊息：請問預約的時間為？人數？
    # ....
        # ....
    # 若收到訊息 '我要取消'，則回覆一則文字訊息：已為您取消
    # ....
        # ....
    # 其餘訊息一率回覆：您好，很高興為您服務！
    # ....
        # ....
    
    
# run app
if __name__ == "__main__":
    # write your code here to launch web server
    # ....