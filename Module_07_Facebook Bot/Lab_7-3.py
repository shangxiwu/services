import json
import requests
from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    verification_code = 'III_TEST12345'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')


# input your access token
PAGE_ACCESS_TOKEN = ' '        

# send text msg
def send_text_message(to, message):
    # write your code here
    # ...

# semd img msg
def send_img_message(to, img_url):
    # write your code here
    # ... 

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():   
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    img_url = 'https://www.iii.org.tw/assets/images/nav-all/logo.png'
    # write your code here
    # ...
                
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    