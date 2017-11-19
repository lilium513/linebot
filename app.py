from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
# line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
# handler = WebhookHandler('YOUR_CHANNEL_SECRET')
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/", methods=['POST'])
def hello_world():
    return "hello world!"


if __name__ == "__main__":
    app.run()
