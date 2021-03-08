import csv
import sys
from multitransport.download_csv import download


def liste_all_town():
	villes = ["Montpellier", "Lille", "Angers", "Rennes"]
	return villes


def liste_all_station(town):
	with open(download(town), newline='', encoding='utf-8') as f:
		if town == 'Montpellier':
			reader = csv.DictReader(f, delimiter=';')
			for row in reader:
				readrow = [row['stop_name']]
			return readrow
		elif town == 'Rennes':
			reader = csv.DictReader(f, delimiter=';')
			for row in reader:
				readrow = [row["Point d'arrêt (nom)"]]
			return readrow
		elif town == 'Lille':
			reader = csv.DictReader(f, delimiter=';')
			for row in reader:
				readrow = [row['nomStation']]
			return readrow
		elif town == 'Angers':
			reader = csv.DictReader(f, delimiter=';')
			for row in reader:
				readrow = [row['nomarret']]
			return readrow
		else:
			print(f'Pas de fichier CSV pour {town}')
