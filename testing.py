from pyngrok import ngrok
from flask import Flask, request, abort

app = Flask(__name__)
http_tunnel = ngrok.connect(5000) #your port

@app.route("/callback", methods=['POST']) #replace def lambda_handler with this part instead
def callback():
    signature = request.headers['X-Line-Signature'] # get X-Line-Signature header value
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body) # get request body as text
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)
    return 'OK'
