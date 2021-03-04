import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

def liste_stations(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT Arrêt FROM info_trafic
    """)
    stations = []
    for row in cursor: 
        stations.append(row[0])
    conn.commit()
    conn.close()
    liste_stations = sorted(list(set(stations)))
    return liste_stations


def liste_next_trains(database, station):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM info_trafic
    WHERE Arrêt = ?
    """, (station, ))
    liste_passages = []
    for row in cursor: 
        liste_passages.append(row)
    conn.commit()
    conn.close()
    return liste_passages