import errno
import os
import sys
import tempfile
from argparse import ArgumentParser
import json
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, \
    PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
channel_secret = os.environ['LINE_CHANNEL_SECRET']
channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
app = Flask(__name__)
#ここらへんでルーティングする

@app.route("/")
def hello():
    return "hello world!"

@app.route("/", methods=['POST'])
def routing():
    body = request.get_data(as_text=True)
    receive_json = json.loads(body)
    print(body)
    route = receive_json['events'][0]['message']['text']




    line_bot_api.reply_message(
        receive_json['events'][0]['replyToken'],
        TemplateSendMessage(
            alt_text='Image carousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://images-fe.ssl-images-amazon.com/images/I/51bZA91ZWqL.jpg',
                        actions=[
                        PostbackTemplateAction(
                            label='ping with text', data='ping',
                            text='ping'),
                        MessageTemplateAction(label='Translate Rice', data='rice is pushed', text='米')
                    ]
                    ),
                    ImageCarouselColumn(
                        image_url='https://images-fe.ssl-images-amazon.com/images/I/51bZA91ZWqL.jpg',
                        action=MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://images-fe.ssl-images-amazon.com/images/I/51bZA91ZWqL.jpg',
                        action=URITemplateAction(
                            label='uri1',
                            uri='https://www.amazon.co.jp/gp/product/B00FR78X64'
                        )
                    )
                ]
            )
        )
    )
# line_bot_api.reply_message(
    #     event.reply_token,
    return body


if __name__ == "__main__":
    app.run()
