import json
from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    verification_code = 'III_Assignment'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    print('message_entries : ', message_entries)
    # print text only
    for entry in message_entries:
        for message in entry['messaging']:
            if 'message' in message:
                text = message['message']['text']
                print(text)
                
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    