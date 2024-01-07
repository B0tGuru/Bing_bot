from os import environ
from Bard import Chatbot
import aiohttp
from sydney import SydneyClient


token = environ.get("BARD_TOKEN")
environ["BING_COOKIES"]=''
#environ.get("BARD_TOKEN")
def initBard(bard_token):
    token = bard_token
async def bardChat(bard_msg):
    chatbot = Chatbot(token)

    bot_reply = chatbot.ask(bard_msg)
    return bot_reply['content']

async def xbingChat(qtn_text):
    async with SydneyClient() as sydney:
        res_str = await sydney.ask(qtn_text)
        return res_str

async def bingChat(qtn_text):
    url_data = quote(qtn_text)
    req_str = f"https://api.freegpt4.ddns.net/?text={url_data}"
    print(req_str)
    req = requests.get(req_str)
    res_str = req.text
    print(f"response is: {res_str}")

    return res_str
