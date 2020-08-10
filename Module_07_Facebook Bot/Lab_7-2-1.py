from flask import Flask, request

app = Flask(__name__)

# verify msg from facebook
@app.route('/callback', methods=["GET"])
def fb_webhook():
    # write your code here
    # set verification_code as "III_TEST12345"
    # ...


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
    
    