import json
import requests
from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    verification_code = 'III_Assignment'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')


# input your access token
PAGE_ACCESS_TOKEN = ' '        

# semd img msg
def send_img_message(to, img_url):
    post_message_url = 'https://graph.facebook.com/v6.0/me/messages?access_token=' + PAGE_ACCESS_TOKEN
    response_message = json.dumps({
                                  "recipient":{
                                    "id": to
                                  },
                                  "message":{
                                    "attachment":{
                                      "type":"image", 
                                      "payload":{
                                        "url": img_url, 
                                        "is_reusable": 'true'
                                      }
                                    }
                                  }
                                })
    requests.post(post_message_url, headers={'Content-Type': 'application/json'}, data=response_message)    

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():   
    # target img
    img_url = 'https://www.iii.org.tw/assets/images/nav-all/logo.png'
    
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            if 'message' in message:
                sender_id = message['sender']['id']
                # send img
                send_img_message(sender_id, img_url)
                
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    