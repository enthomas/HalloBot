import time
from fonctions import *

intro = "Bonjour et bienvenu sur ce Bot d'Halloween 🎃 Le BDA te proposes une nouvelle fois une aventure forte en rebondissements !"
already_started = "Je vois que tu es déjà inscrit, utilises plutôt la commande /start_again si tu t'es trompé ☺️"
ask_data = "Avant de commencer on a besoin de savoir qui tu es (pour les cadeaux surtout 😉)"
recap_data = "On récapitule :"
incorrect_data = "Tu peux recommencer avec la commande /start_again s'il y a une erreur."
finish_start = "Tu peux utiliser /continuer pour continuer, /etat pour avoir un point sur ton état."
success_stop = "Ok on fait une pause. "
choix = "Que souhaites tu faire ?"
invalid_input = "Je n'ai pas compris, essaie encore."
suite = "Pour découvrir la suite clique sur /continuer"

empty_user = { "prénom" : "",
               "nom" : "",
               "promo" : "",
               "enregistrement" : 0,
               "fin" : 0,
               "position" : 0,
               "nbDéplacements" : 0,
               "nbTotemsDétruits" : 3,
               "poignetGauche" : False,
               "poignetDroit" : True,
               "chevilleGauche" : True,
               "chevilleDroite" : True,
               "fini" : False}

ask = [ "Quel est ton prénom ?",
        "Quel est ton nom ?",
        "Dans quelle promo es-tu ?",
        "Super merci ! J'arrête de t'embêter\nPour découvrir l'histoire utilise /continuer\nPour faire une pause à tout moment utilise /stop\nPour découvrir l'état de ton personnage utilise /etat"]
PRENOM, NOM, PROMO, FIN = range(4)

QCM, ENIGME = range(2)

promos = [ "1A", "2A", "3A"]

manoir = { 0 : { "nom" : "grenier",
                 "description" : "Tu te réveilles dans une pièce basse de plafond très poussiéreuse, on dirait un grenier. Des coffres et des malles sont entassés autour de toi, et un lucarne se détache du mur sombre. Tu remarques des traces de pas dans la poussière qui semblent se diriger vers ce qui ressemble à une trappe.",
                 "type" : "QCM",
                 "actions" : { "action1" : { "intitulé" : "Essayer d'ouvrir la trappe.",
                                             "descriptionAction" : "Malgré ta faible force physique tu parviens à ouvrir la trappe et tu découvres ce qui ressemble à un couloir en contre bas. Tu décides d'utiliser l'échelle pour descendre.\n\nCa y est tu es en bas. Mince l'échelle ! Elle vient de se replier, impossible de remonter. Tant pis continuons par là.",
                                             "résultat" : 1,
                                             "exécutable" : do_nothing},
                                "action2" : { "intitulé" : "Aller regarder par la lucarne.",
                                              "descriptionAction" : "Tu t'approches de la lucarne, il fait nuit. Il n'y a rien aux alentours à part des forêts à perte de vue. On dirait que tu te trouves dans grand manoir.\nTu essaies d'ouvrir la lucarne, et en forçant un peu tu y arrives ! On dirait qu'il y a un balcon juste en dessous, tu décides alors de te glisser hors du grenier et de sauter sur le balcon en contrebas.\nIl y a une porte fenêtre, elle s'ouvre ! Tu te faufiles donc à l'intérieur.",
                                              "résultat" : 2,
                                              "exécutable" : do_nothing},
                                "action3" : { "intitulé" : "Examiner les malles et les coffres.",
                                              "descriptionAction" : "Tu essaies d'ouvrir tout ce qu'il y a autour de toi. Un seul coffre s'ouvre, et à l'intérieur se trouve un vieux carnet poussiéreux. ",
                                              "résultat" : 3,
                                              "exécutable" : do_nothing}}},
            1 : { "nom" : "couloir",
                          "description" : "Tu es dans un long couloir. Dans côté une petite porte, de l'autre une très grande porte. Mais ? Ce serait la sortie ?!",
                          "type" : "QCM",
                          "actions" : { "action1" : { "intitulé" : "Ouvrir la petite porte.",
                                                      "descriptionAction" : "Elle n'est pas vérouillée, tu te glisse à l'intérieur de cette nouvelle pièce.",
                                                      "résultat" : 2,
                                                      "exécutable" : do_nothing},
                                        "action2" : { "intitulé" : "Utiliser la grande porte.",
                                                      "descriptionAction" : "Tu longes le couloir immense pour atteindre cette porte majestueuse. Tu la pousses et...",
                                                      "résultat" : 6,
                                                      "exécutable" : totemsFinis}}},
            2 : { "nom" : "chambre",
                          "description" : "Tu te trouves dans une chambre, un immense lit à baldaquins se trouve le long d'un des murs. Il y a une porte fenêtre qui semble mener sur un balcon. A l'opposer se trouve une autre porte.\nTu remarques une table de chevet à côté du lit. Etrange... on dirait que le tiroir bouge tout seul.",
                          "type" : "QCM",
                          "actions" : { "action1" : { "intitulé" : "Aller sur le balcon.",
                                                      "descriptionAction" : "Il fait froid dehors. Tu ne vois rien aux alentours à part une grande forêt, tu examines alors le batiment, on dirait un manoir, il a l'air immense.\nTu apprends peu de chose ici, tu décides de retourner à l'intérieur.",
                                                      "résultat" : 2,
                                                      "exécutable" : do_nothing},
                                        "action2" : { "intitulé" : "Utiliser l'autre porte.",
                                                      "descriptionAction" : "La porte n'est pas vérouillée, tu peux passer.",
                                                      "résultat" : 1,
                                                      "exécutable" : do_nothing},
                                        "action3" : { "intitulé" : "Examiner le tiroir de la table de chevet.",
                                                      "descriptionAction" : "A peine as-tu ouvert le tiroir qu'un flash lumineux t'éblouis...",
                                                      "résultat" : 5,
                                                      "exécutable" : do_nothing}}},
            3 : { "nom" : "coffre",
                  "description" : "En le feuilletant tu comprends que tu te trouves dans un manoir hanté et qu'il te faut t'échapper. L'auteur de ce journal s'est un jour retrouvé dans la même situation que toi et t'apprends que tu dois détruire 4 totems pour te défaire des sceaux sur tes chevilles et tes poignets.\nTu te demandes si lui a réussi à s'échapper...",
                  "type" : "QCM",
                  "actions" : { "action1" : { "intitulé" : "Essayer d'ouvrir la trappe.",
                                              "descriptionAction" : "Malgré ta faible force physique tu parviens à ouvrir la trappe et tu découvres ce qui ressemble à un couloir en contre bas. Tu décides d'utiliser l'échelle pour descendre.\n\nCa y est tu es en bas. Mince l'échelle ! Elle vient de se replier, impossible de remonter. Tant pis continuons par là.",
                                              "résultat" : 1,
                                              "exécutable" : do_nothing},
                                "action2" : { "intitulé" : "Aller regarder par la lucarne.",
                                              "descriptionAction" : "Tu t'approches de la lucarne, il fait nuit. Il n'y a rien aux alentours à part des forêts à perte de vue. On dirait que tu te trouves dans grand manoir.\nTu essaies d'ouvrir la lucarne, et en forçant un peu tu y arrives ! On dirait qu'il y a un balcon juste en dessous, tu décides alors de te glisser hors du grenier et de sauter sur le balcon en contrebas.\nIl y a une porte fenêtre, elle s'ouvre ! Tu te faufiles donc à l'intérieur.",
                                              "résultat" : 2,
                                              "exécutable" : do_nothing}}},
            4 : { "nom" : "sortieOK",
                  "description" : "Ca y est tu es dehors, plus de sceaux sataniques pour te retenir... Tu es libre !",
                  "type" : "QCM",
                  "actions" : { "action1" : { "intitulé" : "Voir la suite.",
                                              "descriptionAction" : "Bravo tu as terminé le jeu ! Merci d'avoir participer, on espère que ça t'a plu. Reste connecté, on annoncera les vainqueurs prochainement.\nA très vite à l'école !\n(tu peux continuer à explorer le manoir si tu veux, mais ton temps mui s'est arrété)",
                                              "résultat" : 0,
                                              "exécutable" : terminer}}},
            5 : { "nom" : "tiroir",
                  "description" : "Alors que ta vue s'adapte à cette nouvelle luminosité, tu distingues une créature d'un autre monde. Elle te dit alors d'une voix caverneuse :",
                  "type" : "énigme",
                  "question" : "\'Réponds donc à cette énigme\n(la réponse c'est reponse)\'",
                  "réponse" : "reponse",
                  "vrai" : { "descriptionRésultat" : "\'Bien joué tu as su répondre à mon énigme. Je vais donc te délivrer du sceaux sur ton poignet gauche.\'",
                             "résultat" : 2,
                             "exécutable" : sceauPG},
                  "faux" : { "descriptionRésultat" : "\'Mécréant ! Ne reviens pas me déranger à moins d'avoir la bonne réponse. Je te renvoie d'où tu viens !\'",
                             "résultat" : 0,
                             "exécutable" : do_nothing}},
            6 : { "nom" : "sortiepasOK",
                  "description" : "Tu te retouves dehors, et alors que tu allais t'élancer dans la nature, un démon apparait devant toi et s'exclame :",
                  "type" : "énigme",
                  "question" : "\'Je vois que tu essaies de t'enfuir. Ca ne se passera pas comme ça. Cependant je serais clément si tu réponds à cette énigme\n(la réponse c'est reponse)\'",
                  "réponse" : "reponse",
                  "vrai" : { "descriptionRésultat" : "\'Je vois que tu es plus malin que les autres... Je vais me contenter de te renvoyer d'où tu viens.\'",
                             "résultat" : 0,
                             "exécutable" : do_nothing},
                  "faux" : { "descriptionRésultat" : "\'Comme je m'y attendais tu es comme tous les autres... Je vais te renvoyer d'où tu viens en restaurant la puissance de mes sceaux.\'",
                             "résultat" : 0,
                             "exécutable" : setSceaux}}}
