import sqlite3
import urllib.request
import logging

logging.basicConfig(level=logging.DEBUG)

def remove_table(cursor):

    """This function remove table 'infoarret' if exist
    for remove before update

    cursor : Acts like a position indicator and will be use to
    retrieve data.

    """
    logging.debug('remove_table: la table est supprime')
    cursor.execute("""DROP TABLE IF EXISTS infoarret""")
    


def update_db():
    """This function, retrieve the csv from url and download this csv file

    """
    logging.debug('update_db: Mise a jour de la base de données')
    csv_url = 'https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'
    urllib.request.urlretrieve(csv_url, 'multitransport.csv')


def create_schema(cursor):
    """ This function create table 'infoarret' if not exist

    this table contains 11 columns and determinate the type.

    cursor : Acts like a position indicator and will be use to
    retrieve data.

    """
    logging.debug('create_schema: on cree les colonnes de la base')
    cursor.execute("""CREATE TABLE IF NOT EXISTS "infoarret" (
    "stop_name"	TEXT,
    "route_short_name"	TEXT,
    "trip_headsign"	TEXT,
    "delay_sec"	INTEGER
    );""")

def insert_csv_row(csv_row, cursor):

    """ This function insert values in table 'infoarret'

    cursor : Acts like a position indicator and will be use to
    retrieve data.

    csv_row : retrieve the lines on the csv file.

    """ 
    liste_row = csv_row.strip().split(";")
    new_row = [liste_row[3], liste_row[4], liste_row[5], liste_row[9]]
    # print(new_row)
    cursor.execute("""INSERT INTO infoarret VALUES (?,?,?,?) """,
                   new_row)


def load_csv(path, cursor):
    """ This function load and read the csv file, and insert row in db file.

    cursor : Acts like a position indicator and will be use to
    retrieve data.

    path : Source of the csv file.

    """
    logging.debug('load_csv: Charge la base de données')
    with open(path, "r") as f:
        # ignore the header
        f.readline()
        line = f.readline()
        # loop over the lines in the file
        while line:
            insert_csv_row(line, cursor)
            line = f.readline()


def test_requete(cursor):
    cursor.execute("""
    SELECT * FROM infoarret
    WHERE stop_name = ?
    """, ('MOSSON', ))
    for row in cursor:
        print(f'arret {row[0]} , ligne{row [1]}, trip_headsign {row[2]}, delay {row[3]}')

def main():

    """ This function, is the MAIN function :
    This function will check if the argument next or time has been entered by
    the user:

    If one of the two arguments was entered the program will continue and
    display the results to the user.
    If neither of the two arguments was entered by the user the program will
    display an error message and close.

    """
    logging.debug('Demarrage de la fonction main')
    conn = sqlite3.connect('multitransport.db')
    if not conn:  # si format ne convient pas, si la base est corrompue...etc
        logging.warning('impossible de se connecter à la base de données')
        return 1
    c = conn.cursor()
    remove_table(c)
    update_db()
    dl = 'multitransport.csv'
    print(dl)
    remove_table(c)
    create_schema(c)
    load_csv(dl, c)

    test_requete(c)

    conn.commit()
    conn.close()
    logging.info('Programme fini !!!!!')


if __name__ == '__main__':
    main()