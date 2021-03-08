import csv
from multitransport.download_csv import download


def listes_all_town():
    villes = ["Montpellier", "Rennes", "Lille", "Angers"]
    return villes


def liste_all_station(town):
    with open(download(town), newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        if town == "Montpellier":
            for row in reader:
                readrow = [row['stop_name']]
            return readrow
        elif town == "Rennes":
            for row in reader:
                readrow = [row["Point d'arrêt (nom)"]]
            return readrow
        elif town == "Lille":
            for row in reader:
                readrow = [row['nomStation']]
            return readrow
        elif town == "Angers":
            for row in reader:
                readrow = [row['nomarret']]
            return readrow
        else:
            print(f'Pas de fichier csv pour {town}')
