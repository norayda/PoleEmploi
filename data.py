#
#
import json
import requests


def saving_fichier_json(data: dict, filename: str = "fichier.json"):
    with open("pole_emploi/" + filename, "w") as file:
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
