# import logging
import sqlite3
import time
from readcsv import readcsv


def connect():
    conn = sqlite3.connect("multitrsp.db")
    c = conn.cursor()
    return conn, c


def clear_rows(cursor, town):
    cursor.execute("""
    DELETE FROM info_trafic
    WHERE Ville = ?""", (town,))


def insert_csv_row(csv_row, cursor):
    cursor.execute("""INSERT INTO info_trafic VALUES (?,?,?,?,?) """,
                   csv_row)


def load_csv(town, cursor):
    lines = readcsv(town)
    for line in lines:
        insert_csv_row(line, cursor)


def remove_table(cursor):
    cursor.execute("""DROP TABLE IF EXISTS info_trafic""")


def create_schema(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS "info_trafic" (
    "Ligne"	TEXT,
    "Arrêt"	TEXT,
    "Destination"	TEXT,
    "Temps_attente"	INTEGER,
    "Ville"	TEXT
    );""")


def main(town):
    conn, c = connect()
    clear_rows(c, town)
    if not conn:
        print(
            "Error : could not connect to database {}".format("multitrsp.db")
            )
        return 1
    # print("Ville : Montpellier, Lille, Angers, Rennes")
    # town = input("Nom de la ville : ").capitalize()
    create_schema(c)
    load_csv(town, c)
    conn.commit()
    conn.close()
