# from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto     
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, InlineQueryHandler, CallbackQueryHandler, CallbackContext, Filters
import os 
from sys import exit

TOKEN: str = None
CHATID: int = None

# PATHS 
CURRENT_PATH: str = os.path.dirname(__file__)
TELEGRAM_CREDENTIALS_PATH: str = os.path.join(CURRENT_PATH, "memory", "auth", "telegram_credentials.json")




def startup() -> None: 
    global TOKEN 
    global CHATID
    
    if not os.path.exists(TELEGRAM_CREDENTIALS_PATH):
        create_telegram_credentials()


def create_telegram_credentials() -> None: 
    # this function creates the telegram_credentials.json and exits the scripts
    print("\tcreating create_telegram_scripts..")
    exit()
    
    
def status() -> None: 
    pass
    

if __name__ == "__main__": 
    startup() 
    
    updater = Updater(token = TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("status", status))