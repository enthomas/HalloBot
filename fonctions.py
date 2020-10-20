import unicodedata
import time
from data import *

def user_id_str(user_data):
    #affichage
    try :
        return "{} {} {} ".format(user_data["prénom"],
                                       user_data["nom"],
                                       user_data["promo"])
    except :
        return user_data["nom"]

def user_recap(user_data) :
    #affichage recap
    try :
        return "{} {} ({})\n{} déplacements\nTrouve {}\nEn {} secondes".format(user_data["prénom"],
                                         user_data["nom"],
                                         user_data["promo"],
                                         user_data["nbDéplacements"],
                                         time.strftime("%A %d %B %Y %H:%M:%S", time.localtime(user_data["fin"])),
                                         int(user_data["fin"] - user_data["enregistrement"]))
    except :
        return user_data["nom"]

def game_recap(update, context):
    i = 1
    for id in context.bot_data["users"] :
        #if i!=3 and i!=17 and i!=20 and i!=33:
        str = "Prénom : {} \nNom : {} \nPromo : {} \n{} déplacements\nHeure d'enregistrement : {} \nHeure de réussite : {} \nTemps de process : {} secondes\n".format(
                                    context.bot_data["users"][id]["prénom"],
                                    context.bot_data["users"][id]["nom"],
                                    context.bot_data["users"][id]["promo"],
                                    context.bot_data["users"][id]["nbDéplacements"],
                                    time.strftime("%H:%M:%S", time.localtime(context.bot_data["users"][id]["enregistrement"])),
                                    time.strftime("%H:%M:%S", time.localtime(context.bot_data["users"][id]["fin"])),
                                    int(context.bot_data["users"][id]["fin"] - context.bot_data["users"][id]["enregistrement"])
                                    )
        #i +=1
        print(str)

def do_nothing(resultat, user_data, context, update):
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def totemsFinis(resultat, user_data, context, update):
    #utilisé dans Entrée
    if user_data["nbTotemsDétruits"] == 4 :
        user_data["position"] = 30
    else :
        user_data["position"] = 31
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def terminer(resultat, user_data, context, update):
    #sortieOK
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["fini"] = True
        user_data["nbDéplacements"] += 1
        user_data["fin"] = time.time()
        print(user_data["prénom"] + " a trouvé !\n" + user_recap(user_data))
        context.bot.send_message(chat_id=-430587684, text=user_data["prénom"] + " a trouvé !\n" + user_recap(user_data))

def sceauPG(resultat, user_data, context, update):
    #fioles
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetGauche"] :
        user_data["poignetGauche"] = True
        user_data["nbTotemsDétruits"] += 1

def setSceaux(resultat, user_data, context, update):
    #sortiePasOK
    user_data["position"] = resultat
    user_data["poignetGauche"] = False
    user_data["poignetDroit"] = False
    user_data["chevilleGauche"] = False
    user_data["chevilleDroite"] = False
    user_data["nbTotemsDétruits"] = 0
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def sceauPD(resultat, user_data, context, update):
    #miroir
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetDroit"] :
        user_data["poignetDroit"] = True
        user_data["nbTotemsDétruits"] += 1

def sceauCG(resultat, user_data, context, update):
    #pentagramme
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleGauche"] :
        user_data["chevilleGauche"] = True
        user_data["nbTotemsDétruits"] += 1

def sceauCD(resultat, user_data, context, update):
    #chambre Dracula
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleDroite"] :
        user_data["chevilleDroite"] = True
        user_data["nbTotemsDétruits"] += 1

def test_miroir(resultat, user_data, context, update):
    #salle de bain
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetDroit"] :
        user_data["position"] = resultat
    else :
        user_data["position"] = 32

def test_penta(resultat, user_data, context, update):
    #tableau
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleGauche"] :
        user_data["position"] = resultat
    else :
        user_data["position"] = 33

def test_fioles(resultat, user_data, context, update):
    #Laboratoire
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetGauche"]:
        user_data["position"] = resultat
    else :
        user_data["position"] = 34

def test_Drac(resultat, user_data, context, update):
    #bibliothèque
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleDroite"]:
        user_data["position"] = resultat
    else :
        user_data["position"] = 35

def setSceauCG(resultat, user_data, context, update):
    #fioles
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if user_data["chevilleGauche"] :
        user_data["chevilleGauche"] = False
        user_data["nbTotemsDétruits"] -= 1
    user_data["position"] = resultat

def setSceauPG(resultat, user_data, context, update):
    #Salon1
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if user_data["poignetGauche"] :
        user_data["poignetGauche"] = False
        user_data["nbTotemsDétruits"] -= 1
    user_data["position"] = resultat

def setSceauPD(resultat, user_data, context, update):
    #fioles
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if user_data["poignetDroit"] :
        user_data["poignetDroit"] = False
        user_data["nbTotemsDétruits"] -= 1
    user_data["position"] = resultat

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
