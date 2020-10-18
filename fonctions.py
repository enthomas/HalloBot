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
    #utiliser dans Entrée
    if user_data["nbTotemsDétruits"] == 4 :
        user_data["position"] = 30
    else :
        user_data["position"] = 31
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def terminer(resultat, user_data):
    #sortieOK
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["fini"] = True
        user_data["nbDéplacements"] += 1
        user_data["fin"] = time.time()

def sceauPG(resultat, user_data):
    #fioles
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetGauche"] :
        user_data["poignetGauche"] = True
        user_data["nbTotemsDétruits"] += 1

def setSceaux(resultat, user_data):
    #sortiePasOK
    user_data["position"] = resultat
    user_data["poignetGauche"] = False
    user_data["poignetDroit"] = False
    user_data["chevilleGauche"] = False
    user_data["chevilleDroite"] = False
    user_data["nbTotemsDétruits"] = 0
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1

def sceauPD(resultat, user_data):
    #miroir
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetDroit"] :
        user_data["poignetDroit"] = True
        user_data["nbTotemsDétruits"] += 1

def sceauCG(resultat, user_data):
    #pentagramme
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleGauche"] :
        user_data["chevilleGauche"] = True
        user_data["nbTotemsDétruits"] += 1

def sceauCD(resultat, user_data):
    #chambre Dracula
    user_data["position"] = resultat
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleDroite"] :
        user_data["chevilleDroite"] = True
        user_data["nbTotemsDétruits"] += 1
def test_miroir(resulat, user_data):
    #salle de bain
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetDroit"] :
        user_data["position"] = resulat
    else :
        user_data["position"] = 32

def test_penta(resulat, user_data):
    #tableau
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleGauche"] :
        user_data["position"] = resulat
    else :
        user_data["position"] = 33

def test_fioles(resulat, user_data):
    #Laboratoire
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["poignetDroit"]:
        user_data["position"] = resulat
    else :
        user_data["position"] = 34

def test_Drac(resulat, user_data):
    #bibliothèque
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    if not user_data["chevilleDroite"]:
        user_data["position"] = resulat
    else :
        user_data["position"] = 35

def setSceauCG(resultat, user_data):
    #fioles
    if not user_data["fini"]:
        user_data["nbDéplacements"] += 1
    user_data["chevilleGauche"] = False
    user_data[nbTotemsDétruits] -= 1
    user_data["position"] = resulat

def setSceauPG(resultat, user_data):
#Salon1
if not user_data["fini"]:
    user_data["nbDéplacements"] += 1
user_data["poignetGauche"] = False
user_data[nbTotemsDétruits] -= 1
user_data["position"] = resulat

def setSceauPD(resultat, user_data):
#fioles
if not user_data["fini"]:
user_data["nbDéplacements"] += 1
user_data["poignetDroit"] = False
user_data[nbTotemsDétruits] -= 1
user_data["position"] = resulat

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
