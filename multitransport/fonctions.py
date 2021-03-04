import logging
import create_db as create_db

logging.basicConfig(level=logging.DEBUG)


def liste_stations(database):
    conn, cursor = create_db.connect()
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


def liste_trains(database, station):
    conn, cursor = create_db.connect()
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


def liste_next(database, station, destination, line):
    conn, cursor = create_db.connect()
    cursor.execute("""
    SELECT * FROM info_trafic
    WHERE Arrêt = ? AND Destination = ? AND Ligne = ?
    """, (station, destination, line))
    liste_passages = []
    for row in cursor:
        liste_passages.append(row)
    conn.commit()
    conn.close()
    return liste_passages
