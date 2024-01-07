from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, InlineKeyboardButton, MenuButton, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ApplicationBuilder, MessageHandler, filters
import asyncio

import bardbot,json,os,sys
import logging
import logging.config

logger = logging.getLogger(__name__)

is_done = False
logs=list()

active_cmd = {}
tasks_made = {}


tele_token = ""

py_args = sys.argv
tapp = None


async def askToken(ask_txt,update):
    print(update)
    print("\n\n\n")
    button1 = InlineKeyboardButton(text='Get token', web_app=WebAppInfo(token_server))
    button2 = InlineKeyboardButton(text='write token',callback_data = "writetoken")
    keyboard = InlineKeyboardMarkup([[button1,button2]])
    await update.message.reply_text(ask_txt, reply_markup=keyboard)

async def processService(update,last_update,context):
    txt = update.message.text
    chatid = update.message.chat_id
    
    bard_reply = await bardbot.bingChat(txt)
    
    print(bard_reply)
    
    await context.bot.edit_message_text(chat_id=chatid,message_id = last_update.message_id,text=bard_reply)


async def authToken(update):
    print('authing user')

async def chatMan(update,context):
    print("chatter")
    cid = update.effective_user.id
    print(f"cid is {cid}")
    last_update = await update.message.reply_text(f'Digesting Message, Bambi Lindako......')
    print(f"\n\nuser id is: {cid}")
    print(f"\n\nlets go eyes: {cid}\n")
    
    await processService(update,last_update,context)
    is_done = True

async def chatManCmd(update,context):
    logs.append("processing message")
    
    await chatMan(update,context)



async def startCmd(update,context):
    cid = update.effective_user.id
    print("start started")
    await update.message.reply_text("You are free to use this service")


async def start(update, context):
    print("start update")
    cid = update.effective_user.id
    await startCmd(update,context)
    print("\n\nok off we go\n\n")


async def runCmd(update,context):
    cid = update.effective_user.id
    task_made = asyncio.create_task(start(update,context))
    await task_made


#async 
def main_polling():
    logging.error("initialising bot")
    logging.error("initialised bot")
    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(filters.TEXT,callback=chatManCmd)
    tapp.add_handler(start_handler)
    tapp.add_handler(msg_handler)
    tapp.run_polling()


if (len(py_args)>1):
    tele_token = py_args[1]
    tapp = ApplicationBuilder().token(tele_token).build()
    main_polling()
else:
    print("hello, please start the bot with your token from @botFather using this format python aibot.py [your_bot_token]")