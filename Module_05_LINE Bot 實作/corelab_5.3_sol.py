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
    MessageEvent, TextMessage, TextSendMessage, AudioMessage,
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
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
import os
os.chdir(os.path.abspath('.'))
import speech_recognition as sr

def transcribe(wav_path):
    '''
    Speech to Text by Google free API
    language: en-US, zh-TW
    '''
    
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio, language="zh-TW")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None
    
@handler.add(MessageEvent, message=AudioMessage)
def handle_audio(event):

    name_mp3 = 'recording.mp3'
    name_wav = 'recording.wav'
    message_content = line_bot_api.get_message_content(event.message.id)
    
    with open(name_mp3, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    
    os.system('ffmpeg -y -i ' + name_mp3 + ' ' + name_wav + ' -loglevel quiet')
    text = transcribe(name_wav)
    print('Transcribe:', text)
    
    
    '''
    作業
    必須將 ffmpeg.exe 和此程式碼置於相同路徑
    填寫 Channel access token 和 secret
    若接收到 '你好嗎' 的訊息，就回 '我很好，那你呢？'
    若接收到 '今天天氣如何' 的訊息，就回 '會下雨唷！要帶傘'
    '''
    if text == '你好嗎':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='我很好，那你呢？'))
    elif '今天天氣如何':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='會下雨唷！要帶傘'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
        
# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)