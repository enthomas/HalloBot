from data import *
from copy import deepcopy
from datetime import date
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import *
import time
from fonctions import *

def start(update, context):
    #initialise l'enregistrement de l'utilisateur
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if "users" in context.bot_data:
        if user_id not in context.bot_data["users"]:
            # logger.info("[/start] New user registering")
            context.bot_data["users"][user_id] = deepcopy(empty_user)
        else :
            context.bot.send_message(chat_id=chat_id, text=already_started)
            return ConversationHandler.END
    else:
        # logger.info("[/start] First user registered")
        context.bot_data["users"] = {user_id: deepcopy(empty_user)}
        context.bot_data["date"] = date.today().day
        context.bot_data["registration_open"] = True

    context.bot.send_message(chat_id=chat_id, text=intro)
    context.bot_data["users"][user_id]["nom"] = update.effective_user.name

    return update_id(update, context, first_time=True)
