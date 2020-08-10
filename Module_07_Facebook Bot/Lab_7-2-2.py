import json
from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    # write your code here
    # set verification_code as "III_TEST12345"
    # ...

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    print('message_entries : ', message_entries)
    # write your code here
    # print as :
    #   sender_id to recipient_id : msg
                
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    