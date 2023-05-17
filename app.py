import random
from flask import Flask, request, abort  
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import *
from crawler import get_patents
from datetime import date, timedelta
from message_builder import flex
import pickle

cache = {"path": "cache.pickle", "range": 0, "step": {}}
app = Flask(__name__)  
line_bot_api = LineBotApi('<api token>')  
handler = WebhookHandler('<channel secret>')

def get_recent(days: int):
    if cache["range"] < days:
        num = infos = None
        if cache["range"] == 0:
            num, infos = get_patents(date.today() - timedelta(days=days), date.today())
            infos = list(infos)
        else:
            num, infos = get_patents(date.today() - timedelta(days=days), date.today() - timedelta(days=days-7))
            infos = list(infos)
            with open(cache["path"], "rb") as f:
                old_num, old_infos = pickle.load(f)
            num += old_num
            old_infos.extend(infos)
            infos = old_infos
        with open(cache["path"], "wb") as f:
            pickle.dump((num, infos), f)
        cache["range"] = days
        cache["step"][days] = num
        return num, infos            
    else:
        with open(cache["path"], "rb") as f:
            _, infos = pickle.load(f)
            return cache["step"][days], infos[:cache["step"][days]] 


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def command(event):
    
    if event.message.text[0] == '/':
        cmd = event.message.text[1:]
        if cmd == "get":
            line_bot_api.reply_message(
                event.reply_token, 
                FlexSendMessage(alt_text="flex", contents= flex(7, get_recent(7)[1]))
            )    
        elif cmd == "update":
            num, infos = get_patents(date.today() - timedelta(days=7), date.today())
            infos = list(infos)
            with open(cache["path"], "wb") as f:
                pickle.dump((num, infos), f)
            cache["range"] = 7
            cache["step"] = {7: num}
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text="flex", contents= flex(7, infos))
            )    

@handler.add(PostbackEvent)
def postback(event):  
    try:
        action, days = (pair.split('=')[1] for pair in event.postback.data.split('&'))
        days = int(days) + 7
        print(action, days)
        if action == "show_early":
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text="flex", contents= flex(days, get_recent(days)[1]))
            )  
        elif action == "show_all":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text= "coming soon")
            )  
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= "error")
        )  


if __name__ == "__main__":
    app.run()
