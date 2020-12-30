import json
import requests
import os

#cette fonction renvoie la fusion de deux dictionnaires passé en arguments
def merge_dicts(dict1,dict2):
    dico = {}
    for x in dict1.keys():
        if(type(dict1[x]) is list):
            dico[x]= []
            dico[x].extend(dict1[x])
            dico[x].extend(dict2[x])

    return dico

#cette fonction prend en argument un dictionnaire et une chaine de caractère représentant le nom du fichier puis enregistre le fichier JSON
#Si le fichier existe déja elle fusionne les nouvelles données avec les anciennes
def saving_fichier_json(data: dict, filename: str = "fichier.json"):
    donnees = json.loads(json.dumps(data))
    if not (os.path.isfile("data/" + filename)):
        with open("data/" + filename, "w") as file:
            json.dump(donnees, file)
    else:
        with open("data/" + filename, "r") as file:
            fichier = json.load(file)
        fichier = merge_dicts(fichier, donnees) #on fusionne les anciennes données contenues dans le fichier et les nouvelles données
        with open("data/" + filename, "w") as file :
            json.dump(fichier,file)

#Cette fonction est la première étape pour accéder aux information de l'API elle permet avec les bonnes clés d'accès de récupérer le token
def load_api(client_id, client_secret, scope):
    url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=/partenaire"

    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope
    }

    headers = {  # Indique au serveur sous quelle forme on lui transmet les données
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.post(url, headers=headers, data=payload)
    return response

#Cette fonction prend en argument le token et renvoie les données à manipuler
def load_api_data(token):
    url = "https://api.emploi-store.fr/partenaire/offresdemploi/v2/offres/search"

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

#cette fonction lit les données contenu dans le fichier JSON
def read_json(filename) :
    with open("data/" + filename, "r") as file:
        data = json.load(file)
        file.close()
    return data