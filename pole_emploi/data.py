#
#
import json

#Cette fonction prend en argument un json et renvoie les lignes qui ont des informations sur la colonne 'salaires'
def extract_salary(data) :
    #renvoie la liste des offres qui ont renseigné le salaire sous forme de dictionnaire
    data["salaire"].fillna(0, inplace=True)
    return data.query('salaire != 0')

#Cette fonction prend en argument un paramètre json et renvoie les lignes qui ont des informations sur la colonne 'dureeTravailLibelle'
def extract_duree_travail(data):
    liste = []
    data["dureeTravailLibelle"].fillna(0,inplace=True) #On remplace les lignes non renseigné par 0

    return data.query("dureeTravailLibelle != 0")

