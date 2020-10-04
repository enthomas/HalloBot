import unicodedata
import time

def user_id_str(user_data):
    #affichage
    try :
        return "{} {} ({}) {} ".format(user_data["prenom"],
                                       user_data["nom"],
                                       user_data["pseudo"],
                                       user_data["promo"])
    except :
        return user_data["nom"]

def do_nothing(resultat, user_data):
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def totemsFinis(resultat, user_data):
    if user_data["nbTotemsDétruits"] == 4 :
        user_data["position"] = 4
    else :
        user_data["position"] = 6
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def terminer(resultat, user_data):
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["fini"] = True
        user_data["nbDéplacements"] += 1
        user_data["fin"] = time.time()

def sceauPG(resultat, user_data):
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetGauche"] :
        user_data["poignetGauche"] = True
        user_data["nbTotemsDétruits"] += 1

def setSceaux(resultat, user_data):
    user_data["position"] = resultat
    user_data["poignetGauche"] = False
    #user_data["poignetDroit"] = False
    #user_data["chevilleGauche"] = False
    #user_data["chevilleDroite"] = False
    user_data["nbTotemsDétruits"] = 0
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
