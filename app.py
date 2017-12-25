import errno
import os
import sys
import tempfile
from argparse import ArgumentParser
import json
import poker
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
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
    cards=poker.getCards()[0:5]
    #route = receive_json['events'][0]['message']['text']


    buttons_template = ButtonsTemplate(
            title='Card itiran', text=str(cards), actions=[
                URITemplateAction(
                    label='Go to line.me', uri='https://line.me'),
                PostbackTemplateAction(label='ping', data='ping'),
                PostbackTemplateAction(
                    label='ping with text', data='ping',
                    text='ping'),
                MessageTemplateAction(label='Translate Rice', text='米')
            ])

    template_message = TemplateSendMessage(
        alt_text='button alt text', template=buttons_template)

    line_bot_api.reply_message(
        receive_json['events'][0]['replyToken'],
        template_message
    )
# line_bot_api.reply_message(
    #     event.reply_token,
    return body


if __name__ == "__main__":
    app.run()
