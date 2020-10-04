from telegram.ext import *
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import *
from fonctions import *

def continuer(update, context):
    user_id = update.effective_user.id
    position = context.bot_data["users"][user_id]["position"]
    update.message.reply_text(manoir[position]["description"])

    if manoir[position]["type"] == "QCM" :
        liste =[]
        for action in manoir[position]["actions"] :
            liste += [manoir[position]["actions"][action]["intitulé"]]
        keyboard = [[KeyboardButton(option)] for option in liste]
        update.message.reply_text(choix, reply_markup=ReplyKeyboardMarkup(keyboard))
        return QCM
    else :
        update.message.reply_text(manoir[position]["question"])
        return ENIGME

def qcm(update, context):
    user_id = update.effective_user.id
    user_input = update.message.text[:30].strip().replace("\n", " ")
    position = context.bot_data["users"][user_id]["position"]

    liste =[]
    for action in manoir[position]["actions"] :
        liste += [manoir[position]["actions"][action]["intitulé"]]
    if user_input not in [elt[:30] for elt in liste] :
        update.message.reply_text(invalid_input)
        return QCM

    for action in manoir[position]["actions"] :
        if user_input == manoir[position]["actions"][action]["intitulé"][:30] :
            update.message.reply_text(manoir[position]["actions"][action]["descriptionAction"], reply_markup=ReplyKeyboardRemove())
            manoir[position]["actions"][action]["exécutable"](manoir[position]["actions"][action]["résultat"], context.bot_data["users"][user_id])

    update.message.reply_text(suite)
    return ConversationHandler.END

def enigmes(update, context):
    user_id = update.effective_user.id
    user_input = remove_accents(update.message.text[:30].strip().replace("\n", " ").lower())
    position = context.bot_data["users"][user_id]["position"]

    if user_input == remove_accents(manoir[position]["réponse"].lower()) :
        res = "vrai"
    else :
        res = "faux"

    update.message.reply_text(manoir[position][res]["descriptionRésultat"], reply_markup=ReplyKeyboardRemove())
    manoir[position][res]["exécutable"](manoir[position][res]["résultat"], context.bot_data["users"][user_id])
    update.message.reply_text(suite)
    return ConversationHandler.END
