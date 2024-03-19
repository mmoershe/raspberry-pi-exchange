from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto     
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, InlineQueryHandler, CallbackQueryHandler, CallbackContext, Filters

import os
import json 
from sys import exit

TOKEN: str = ''
CHATID: int = ''

# PATHS 
CURRENT_PATH: str = os.path.dirname(__file__)
TELEGRAM_CREDENTIALS_PATH: str = os.path.join(CURRENT_PATH, "memory", "auth", "telegram_credentials.json")


def startup() -> None: 
    global TOKEN 
    global CHATID
    
    if not os.path.exists(TELEGRAM_CREDENTIALS_PATH):
        create_telegram_credentials()
        
    with open(TELEGRAM_CREDENTIALS_PATH, "r", encoding="utf-8") as json_file: 
        telegram_credentials: dict = json.load(json_file)
    
    TOKEN = telegram_credentials["TOKEN"]
    CHATID = telegram_credentials["CHATID"]
    
    if TOKEN == "" or CHATID == "": 
        print("\tPlease fill out telegram_credentials.json.")
        print("\tScript will be exited.")
        exit()
    

def create_telegram_credentials() -> None: 
    # this function creates the telegram_credentials.json and exits the scripts
    print("\tcreating create_telegram_scripts...")
    
    template: dict = {"TOKEN": "", "CHATID": ""}
    
    with open(TELEGRAM_CREDENTIALS_PATH, "w", encoding="utf-8") as json_file: 
        json.dump(obj=template, fp=json_file, indent=4)
    
    print("\ttelegram_credentials.json has been created. Please fill in the values to use this script!")
    print("\tScript will be exited.")
    exit()
    
    
def status(update: Update, context: CallbackContext) -> None: 
    message = "test message"
    updater.bot.send_message(CHATID, text=message)
    
    
def opening_message() -> None: 
    message = "opening message"
    updater.bot.send_message(CHATID, text=message)
    
    
def receive_image(update: Update, context: CallbackContext) -> None: 
    # updater.bot.send_message(CHATID, text="you sent an image")
    update.message.reply_text("you sent an image")


if __name__ == "__main__": 
    print()
    startup() 
    
    print(f"{TOKEN = }")
    print(f"{CHATID = }")
    
    updater = Updater(token = TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    opening_message()
    
    dispatcher.add_handler(CommandHandler("status", status))
    
    dispatcher.add_handler(MessageHandler(Filters.photo, receive_image))
    
    updater.start_polling()
    updater.idle()