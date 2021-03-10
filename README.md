Développement d’une API d’analyse de données.

Groupe Adrian/ Damien / Emilie  (promo 2020 de la formation Développeur Cloud)

Le but du brief était d'exploiter l’opendata des horaires de transports pour développer une appli qui propose d’obtenir les horaires de transports en commun.
LIBRAIRIES utilisées :
- Flask
- Sqlite3
- Unnitest

## Partie BACK (dossier appelé multitranport):

LANCEMENT DE L'API :
Pour lancer l'API et mettre à disposition le serveur Flask, lancer le fichier "run.py" et se rendre à l'addresse suivante : http://127.0.0.1:5000/ 

FONCTIONNEMENT DE L'API :
3 routes principales: 
- http:/127.0.0.1:5000/<town>/stations : renvoie la liste les arrêts pour une ville données sous format json 
- http:/127.0.0.1:5000/<town>/stations/<station> : affiche la liste les prochains transports à une station donnée
- http:/127.0.0.1:5000/<town>/next?line=<line>&station=<station>&destination=<destination> : affiche la liste les prochains transports à une station, une ligne et une destination.

LANCER LES TESTS:
Une fois dans le dossier source, ecrire "python -m unittest" dans la console 

## Partie FRONT:


## Script Bash

