import csv
import sys
from export_bdd import download


def readcsv(town):
    with open(download(town), newline='') as f:
        if town == 'Montpellier':
            return bdd_MPL(f)
        elif town == 'Rennes':
            return bdd_RNS(f)
        elif town == 'Lille':
            return bdd_LIL(f)
        elif town == 'Angers':
            return bdd_ANE(f)
        else:
            print(f'Pas de fichier CSV pour {town}')


def bdd_MPL(f):
    listerow = []
    reader = csv.DictReader(f, delimiter=';')
    try:
        for row in reader:
            readrow = [
                row['route_short_name'],
                row['stop_name'],
                row['trip_headsign'],
                row['delay_sec']
                ]
            listerow.append(readrow)
        return listerow
    except csv.Error as e:
        sys.exit(f'{e} problème avec le csv')


def bdd_RNS(f):
    listerow = []
    reader = csv.DictReader(f, delimiter=';')
    try:
        for row in reader:
            readrow = [
                row['Ligne (nom court)'],
                row["Point d'arrêt (nom)"],
                row['Destination'],
                row['Précision']
                ]
            listerow.append(readrow)
        return listerow
    except csv.Error as e:
        sys.exit(f'{e} problème avec le csv')


def bdd_LIL(f):
    listerow = []
    reader = csv.DictReader(f, delimiter=';')
    try:
        for row in reader:
            readrow = [
                row['codeLigne'],
                row['nomStation'],
                row['sensLigne'],
                row['heureEstimeeDepart']
                ]
            listerow.append(readrow)
        return listerow
    except csv.Error as e:
        sys.exit(f'{e} problème avec le csv')


def bdd_ANE(f):
    listerow = []
    reader = csv.DictReader(f, delimiter=';')
    try:
        for row in reader:
            readrow = [
                row['mnemoligne'],
                row['nomarret'],
                row['dest'],
                row['arrivee']
                ]
            listerow.append(readrow)
        return listerow
    except csv.Error as e:
        sys.exit(f'{e} problème avec le csv')
