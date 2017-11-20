from flask import Flask, request, abort
import json
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
channel_secret = os.environ['LINE_CHANNEL_SECRET']
channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/", methods=['POST'])
def hello_world():
    body = request.get_data(as_text=True)
    receive_json = json.loads(body)
    print(receive_json)
    response = receive_json['events'][0]['message']['text']
    line_bot_api.reply_message(receive_json['events'][0]['replyToken'], TextSendMessage(text = response))
    # line_bot_api.reply_message(
    #     event.reply_token,
    return body


if __name__ == "__main__":
    app.run()
