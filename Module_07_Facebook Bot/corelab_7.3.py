import json
import requests
from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    # write your code here
    # set verification_code as "III_Assignment"
    # ...


# input your access token
PAGE_ACCESS_TOKEN = ' '        

# semd img msg
def send_img_message(to, img_url):
    # write your code here
    # create img msg as JSON, send POST request
    # ...

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():   
    # target img
    img_url = 
    
    # write your code here
    # extract request, call send_img_message()
    # ...
    
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    