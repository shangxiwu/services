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
line_bot_api = LineBotApi('2oZ7Dgf0U/fR6afMA+BciP0ip5rgYOSkm9Q/F56I/5jIjJH4DIt0HaFr1SE/Rmm1EBBsFvfRo5wPcaBYPuyTV0Y/mP/G7DfkdAjXqbPXMemawBQ5ZQ/75jY2h6iX3yNirk0GfG9XD9DLLd/Ll5swZAdB04t89/1O/w1cDnyilFU=')
# your linebot message API - Channel secret
handler = WebhookHandler('4bf0981e456e67ae214826d10301b421')

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
    
    # get msg details
    print('msg from [', user_name, '](', user_id, ') : ', msg)
    
    line_bot_api.reply_message(event.reply_token, 
                               [TextSendMessage(text = '回覆文字'),
                                StickerSendMessage(package_id='1',sticker_id='1'),
                                ImageSendMessage(original_content_url='https://www.iii.org.tw/assets/images/nav-all/logo.png', 
                                                 preview_image_url='https://www.iii.org.tw/assets/images/nav-all/logo.png'),
                                LocationSendMessage(
                                     title='Store Location',
                                     address='Taipei 101',
                                     latitude=25.033981,
                                     longitude=121.564506)
                                ])
    
    # push text_msg
    line_bot_api.push_message(user_id,
                              TextSendMessage(text = '您好^^'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)