# import logging
import sqlite3
from multitransport.readcsv import readcsv


def connect():
    """ This function connects sqlite3 cursor"""
    conn = sqlite3.connect("multitrsp.db")
    c = conn.cursor()
    return conn, c


def clear_rows(cursor, town):
    """ This function deletes existing rows from database
    Parameters :
    - cursor : Acts like a position indicator and will be used to
    retrieve data.
    - town (ex: Montpellier)
    """
    cursor.execute("""
    DELETE FROM info_trafic
    WHERE Ville = ?""", (town,))


def insert_csv_row(csv_row, cursor):
    """ This function inserts a row in 'info_trafic' table.
    Parameters :
    - cursor : Acts like a position indicator and will be used to
    retrieve data.
    - csv_row : list of items comming form the csv row.
    """
    cursor.execute("""INSERT INTO info_trafic VALUES (?,?,?,?,?) """,
                   csv_row)


def load_csv(town, cursor):
    """ This function reads csv file, and inserts multiple rows
    into 'info_trafic' table.
    Parameters :
    - cursor : Acts like a position indicator and will be used to
    retrieve data.
    - town (ex: Montpellier)
    """
    lines = readcsv(town)
    for line in lines:
        insert_csv_row(line, cursor)


def remove_table(cursor):
    """This function removes 'info_trafic' table if exists.
    Parameters :
    - cursor : Acts like a position indicator and will be used to
    retrieve data.
    """
    cursor.execute("""DROP TABLE IF EXISTS info_trafic""")


def create_schema(cursor):
    """ This function creates 'info_trafic' table if not exists.
    Parameters:
    - cursor : Acts like a position indicator and will be used to
    retrieve data.
    """
    cursor.execute("""CREATE TABLE IF NOT EXISTS "info_trafic" (
    "Ligne"	TEXT,
    "Arrêt"	TEXT,
    "Destination"	TEXT,
    "Temps_attente"	INTEGER,
    "Ville"	TEXT
    );""")


def main(town):
    """ The MAIN function loads csv file for a set town and creates database .
    Parameters:
    - town (ex: Montpellier)
    """
    conn, c = connect()
    if not conn:
        print(
            "Error : could not connect to database {}".format("multitrsp.db")
            )
        return 1
    # print("Ville : Montpellier, Lille, Angers, Rennes")
    # town = input("Nom de la ville : ").capitalize()
    create_schema(c)
    clear_rows(c, town)
    load_csv(town, c)
    conn.commit()
    conn.close()
