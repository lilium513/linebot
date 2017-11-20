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
line_bot_api = LineBotApi('s6zOrp1BRjZmGqhcTkstw1welbN/UnxxAENoEIEk/n2KWsiPhVZdqmCuaTYbEQXCIxqrp8JK9OLCLNdONAfyGyBMiNtJInGD1SnJO1fHUazwlSTPHO6Hn2hGNgt6fxnLuwDOLhz1Sq1G0LRf5K2ogAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1ba028de2c5d4d8797a00fd5df0ab44f')
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/", methods=['POST'])
def hello_world():
    body = request.get_data(as_text=True)
    receive_json = json.loads(body)
    message = receive_json['events'][0]['message']['text']
    line_bot_api.reply_message(receive_json['events'][0]['replyToken'], TextSendMessage(text = response))
    # line_bot_api.reply_message(
    #     event.reply_token,
    return body


if __name__ == "__main__":
    app.run()
