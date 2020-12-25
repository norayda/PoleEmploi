#
#
import json
import requests
import os
import pandas as pd

def merge_dicts(dict1,dict2):
    dico = {}
    for x in dict1.keys():
        dico[x]= []
        dico[x].extend(dict1[x])
        dico[x].extend(dict2[x])

    return dico


def saving_fichier_json(data: dict, filename: str = "fichier.json"):
    donnees = json.loads(json.dumps(data))
    if not (os.path.isfile("data/" + filename)):
        with open("data/" + filename, "w") as file:
            json.dump(donnees, file)
            file.close()

    else :
        with open("data/" + filename, "r") as file:
            fichier = json.load(file)
            file.close()
        fichier = merge_dicts(fichier, donnees) #on fusionne les anciennes données contenues dans le fichier et les nouvelles données
        with open("data/" + filename, "w") as file :
            json.dump(fichier,file)
            file.close()


def saving_file_json (data,filename = "fichier.json"):
    with open(filename, "w") as file:
        json.dump(data, file)
        file.close()

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

def extract_salary(data) :
    #renvoie la liste des offres qui ont renseigné le salaire sous forme de dictionnaire
    data["salaire"].fillna(0, inplace=True)
    return data.query('salaire != 0') ##renvoie uniquement les ligne qui possèdent une information sur le salaire

def read_json(filename) :
    with open("data/" + filename, "r") as file:
        data = json.load(file)
        file.close()
    return data