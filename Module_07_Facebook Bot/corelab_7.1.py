import json
from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    # write your code here
    # set verification_code as "III_Assignment"
    # ...

# rcv msgs
@app.route('/callback', methods=['POST'])
def fb_receive_message():
    # write your code here
    # extract request, print text only
    # ...
                
    return 'OK'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    