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

# send text msg       
# reply as - user_id : message
def send_text_message(to, message):
    # write your code here
    # create text msg as JSON, send POST request
    # ...

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():   
    # write your code here
    # extract request, call send_text_message()
    # ...
                
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    