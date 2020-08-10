import json
from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    verification_code = 'III_CODE12345'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    print('message_entries : ', message_entries)    # 了解事件架構
    for entry in message_entries:
        for message in entry['messaging']:
            if 'message' in message:
                sender_id = message['sender']['id']
                text = message['message']['text']
                print(sender_id, ' : ', text)       # 印出訊息
                
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    