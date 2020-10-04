def user_id_str(user_data):
    #affichage
    try :
        return "{} {} ({}) {} ".format(user_data["prenom"],
                                       user_data["nom"],
                                       user_data["pseudo"],
                                       user_data["promo"])
    except :
        return user_data["nom"]
