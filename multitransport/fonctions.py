import logging
import create_db as create_db

logging.basicConfig(level=logging.DEBUG)


def liste_stations():
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


def liste_trains(station):
    conn, cursor = create_db.connect()
    cursor.execute("""
    SELECT * FROM info_trafic
    WHERE Arrêt = ?
    """, (station, ))
    liste_passages = []
    liste_row = []
    for row in cursor:
        print(row)
        listerow = [row[0], row[1], row[2], row[4]]
        liste_row.append(row[3])
        if listerow not in liste_passages:
            liste_passages.append(listerow)
    liste_temps = [liste_row[i:i+3] for i in range(0,len(liste_row),3)]
    print(liste_temps)
    result = list(zip(liste_passages, liste_temps))
    print(result)
    conn.commit()
    conn.close()
    return result


def liste_next(station, destination, line):
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
