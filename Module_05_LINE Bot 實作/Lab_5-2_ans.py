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
    # get user info
    user_id = event.source.user_id
    
    # reply with text, sticker, img, location
    line_bot_api.reply_message(event.reply_token, 
                               [TextSendMessage(text = '完成 Lab5-2'),
                                StickerSendMessage(package_id='1',sticker_id='1'),
                                ImageSendMessage(original_content_url='https://www.iii.org.tw/assets/images/nav-all/logo.png', 
                                                 preview_image_url='https://www.iii.org.tw/assets/images/nav-all/logo.png'),
                                LocationSendMessage(
                                     title='Store Location',
                                     address='Taipei 101',
                                     latitude=25.033981,
                                     longitude=121.564506)
                                ])
    # push img
    line_bot_api.push_message(user_id,
                              ImageSendMessage(original_content_url='https://www.iii.org.tw/assets/images/nav-all/logo.png', 
                                                 preview_image_url='https://www.iii.org.tw/assets/images/nav-all/logo.png'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)