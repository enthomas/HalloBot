import time

intro = "Bonjour et bienvenu sur ce Bot d'Halloween 🎃 Le BDA te proposes une nouvelle fois une aventure forte en rebondissements !"
already_started = "Je vois que tu es déjà inscrit, utilises plutôt la commande /start_again si tu t'es trompé ☺️"
ask_data = "Avant de commencer on a besoin de savoir qui tu es (pour les cadeaux surtout 😉)"recap_data = "On récapitule :"
incorrect_data = "Tu peux recommencer avec la commande /start_again s'il y a une erreur."

empty_user = { "prénom" : "",
               "nom" : "",
               "promo" : "",
               "enregistrement" : time.time(),
               "fin" : time.time(),
               "position" : 0,
               "nbDéplacements" : 0,
               "nbTotemsDétruits" : 0,
               "poignetGauche" : False,
               "poignetDroit" : False,
               "chevilleGauche" : False,
               "chevilleDroite" : False}

ask = [ "Quel est ton prénom ?",
        "Quel est ton nom ?",
        "Dans quelle promo es-tu ?",
        "Super merci ! J'arrête de t'embêter"]
PRENOM, NOM, PROMO, FIN = range(4)

promos = [ "1A", "2A", "3A"]
