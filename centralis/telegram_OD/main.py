from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto     
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, InlineQueryHandler, CallbackQueryHandler, CallbackContext, Filters

from ultralytics import YOLO

import sys
import os 
import time
import json 
import subprocess

# credentinals 
TOKEN: str = ''
CHATID: int = ''

# models 
OBJECT_DETECTION_MODELS: list = ["YOLOv8n", "YOLOv8s", "YOLOv8m", "YOLOv8l", "YOLOv8x"]

# PATHS 
CURRENT_PATH: str = os.path.dirname(__file__)
MEMORY_PATH: str = os.path.join(CURRENT_PATH, "memory")
AUTH_PATH: str = os.path.join(MEMORY_PATH, "auth")
TEMPORARY_PATH: str = os.path.join(MEMORY_PATH, "temporary")
TELEGRAM_CREDENTIALS_PATH: str = os.path.join(AUTH_PATH, "telegram_credentials.json")
TEMPORARY_IMAGE_PATH: str = os.path.join(TEMPORARY_PATH, "temporary.jpg")


def get_raspberry_pi_temperature() -> str:
    try:
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        result = result.stdout.strip()
    except:
        result = "[couldn't read temperature]"
    return result


def startup() -> None: 
    global TOKEN 
    global CHATID
    
    if not os.path.exists(TEMPORARY_PATH):
        os.makedirs(TEMPORARY_PATH)

    if not os.path.exists(TELEGRAM_CREDENTIALS_PATH):
        create_telegram_credentials()
        
    with open(TELEGRAM_CREDENTIALS_PATH, "r", encoding="utf-8") as json_file: 
        telegram_credentials: dict = json.load(json_file)
    
    TOKEN = telegram_credentials["TOKEN"]
    CHATID = telegram_credentials["CHATID"]
    
    if TOKEN == "" or CHATID == "": 
        print("\tPlease fill out telegram_credentials.json.")
        print("\tScript will be exited.")
        sys.exit()
    

def create_telegram_credentials() -> None: 
    # this function creates the telegram_credentials.json and exits the scripts
    print("\tcreating create_telegram_scripts...")
    
    if not os.path.exists(AUTH_PATH): 
        os.makedirs(AUTH_PATH)
    
    template: dict = {"TOKEN": "", "CHATID": ""}
    
    with open(TELEGRAM_CREDENTIALS_PATH, "w", encoding="utf-8") as json_file: 
        json.dump(obj=template, fp=json_file, indent=4)
    
    print("\ttelegram_credentials.json has been created. Please fill in the values to use this script!")
    print("\tScript will be exited.")
    sys.exit()
   
   
def object_detection(model_name: str, min_confidence: float = 0.25) -> None:
    # this function takes the temporary.jpg, does a object detection with the provided model and sends both the image and dictionary with all the objects detected. 
    DEVICE: str = "cpu"
    
    model = YOLO(f"{model_name.lower()}.pt")
    print(f"{model.model_name = }")
      
        
def status(update: Update, context: CallbackContext) -> None: 
    message: str = get_raspberry_pi_temperature()
    message: str = message + f"\n{sys.version = }\n{sys.platform = }"
    updater.bot.send_message(CHATID, text=message)
    
    
def opening_message() -> None: 
    message = "opening message"
    updater.bot.send_message(CHATID, text=message)
    
    
def receive_image(update: Update, context: CallbackContext) -> None: 
    # updater.bot.send_message(CHATID, text="you sent an image")
    update.message.reply_text("you sent an image")

    file_id = update.message.photo[-1].file_id
    file_info = context.bot.get_file(file_id)

    file_info.download(TEMPORARY_IMAGE_PATH)

    update.message.reply_text("image saved")

    choices = [[InlineKeyboardButton("Object Detection", callback_data="object_detection")]]
    
    updater.bot.send_message(CHATID, text="I receive and saved an Image. What do you want me to do?", reply_markup=InlineKeyboardMarkup(choices))


def receive_text(update: Update, context: CallbackContext) -> None: 
    update.message.reply_text("You sent a text")


def queryhandler(update: Update, context: CallbackContext) -> None: 
    query = update.callback_query.data.strip()
    if query == "object_detection":
        choices: list = []
        for model in OBJECT_DETECTION_MODELS: 
            choices.append([InlineKeyboardButton(model, callback_data=model)])
        updater.bot.send_message(CHATID, "I will analyze that image.", reply_markup=InlineKeyboardMarkup(choices))
    
    if query in OBJECT_DETECTION_MODELS: 
        updater.bot.send_message(CHATID, "You chose a model")
        object_detection(query)

if __name__ == "__main__": 
    print()
    startup() 
    
    print(f"{TOKEN = }\t{type(TOKEN)}")
    print(f"{CHATID = }\t{type(CHATID)}")
    
    updater = Updater(token = TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    opening_message()
    
    dispatcher.add_handler(CommandHandler("status", status))
    
    dispatcher.add_handler(MessageHandler(Filters.photo, receive_image))
    dispatcher.add_handler(MessageHandler(Filters.text, receive_text))

    dispatcher.add_handler(CallbackQueryHandler(queryhandler))
    
    updater.start_polling()
    updater.idle()