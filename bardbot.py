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

async def bingChat(qtn_text):
    async with SydneyClient() as sydney:
        res_str = await sydney.ask(qtn_text)
        return res_str
