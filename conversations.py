from telegram.ext import *
from telegram import ReplyKeyboardRemove
from data import *

def stop(update, context):
    update.message.reply_text(success_stop, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def etat(update, context):
    #envoie un récap de l'état du joueur
    user_id = update.effective_user.id

    nbTotems = context.bot_data["users"][user_id]["nbTotemsDétruits"]
    sceaux = ""
    if not context.bot_data["users"][user_id]["poignetGauche"] :
        sceaux += "du poignet gauche\n"
    if not context.bot_data["users"][user_id]["poignetDroit"] :
        sceaux += "du poignet droit\n"
    if not context.bot_data["users"][user_id]["chevilleGauche"] :
        sceaux += "de la cheville gauche\n"
    if not context.bot_data["users"][user_id]["chevilleDroite"] :
        sceaux += "de la cheville droite\n"

    str = "Tu as réussis à détruire {} totems.\nIl te reste des sceaux démoniques au niveau :\n{}".format(nbTotems, sceaux)
    if context.bot_data["users"][user_id]["fini"] :
        str = "Tu as déjà réussi à t'échapper une fois !\n" + str
    update.message.reply_text(str, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
