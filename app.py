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

@app.route("/", methods=['POST'])
def routing():
    body = request.get_data(as_text=True)
    receive_json = json.loads(body)
    print(body)
    cards = poker.getCards()[0:5]
    prize = poker.prizeJudge(cards)
    p=""
    if prize==poker.RSF:
        p="ロイヤルストレートフラッシュ"
    if prize==poker.SF:
        p="ストレートフラッシュ"
    if prize==poker.FC:
        p="フォーカード"
    if prize==poker.FH:
        p="フルハウス"
    if prize==poker.FL:
        p="フラッシュ"
    if prize==poker.ST:
        p="ストレート"
    if prize==poker.TC:
        p="スリーカード"
    if prize==poker.TP:
        p="ツーペア"
    if prize==poker.OP:
        p="ワンペア"
    if prize==poker.HC:
        p="豚"

    cards=poker.convertTupleToCards(cards)

    #route = receive_json['events'][0]['message']['text']



    # template_message = TemplateSendMessage(
    #     alt_text='button alt text', template=buttons_template)
  buttons_template = ButtonsTemplate(
             actions=[
                URITemplateAction(
                MessageTemplateAction(label='もう一回', text='もう一回')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)


    line_bot_api.reply_message(
        receive_json['events'][0]['replyToken'],
        [TextSendMessage(text=cards),
        TextSendMessage(text="あなたの役は"+p+"です"),template_message]

    )
# line_bot_api.reply_message(
    #     event.reply_token,
    return body


if __name__ == "__main__":
    app.run()
