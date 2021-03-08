import logging
import multitransport.create_db as create_db

logging.basicConfig(level=logging.DEBUG)


def liste_stations(town):
    """ This function checks all database entries associated
    with a set town and returns a list wich contains stations.
    Parameter : town (ex: Montpellier)
    """
    conn, cursor = create_db.connect()
    cursor.execute("""
    SELECT Arrêt FROM info_trafic WHERE Ville = ?
    """, (town,))
    stations = []
    for row in cursor:
        stations.append(row[0])
    conn.commit()
    conn.close()
    liste_stations = sorted(list(set(stations)))
    return liste_stations


def liste_trains(station, town):
    """ This function checks all database entries associated
    with a set station in a town and returns a list wich contains
    upcomming trains (whatever the line and destination).
    Parameter :
    - station (ex: COMEDIE)
    - town (ex: Montpellier)
    """
    conn, cursor = create_db.connect()
    cursor.execute("""
    SELECT * FROM info_trafic WHERE Arrêt = ? AND Ville = ?
    """, (station, town))
    liste_passages = []
    liste_row = []
    for row in cursor:
        listerow = [row[0], row[1], row[2], row[4]]
        liste_row.append(row[3])
        if listerow not in liste_passages:
            liste_passages.append(listerow)
    liste_temps = [liste_row[i:i+3] for i in range(0, len(liste_row), 3)]
    result = list(zip(liste_passages, liste_temps))
    conn.commit()
    conn.close()
    return result


def liste_next(station, destination, line, town):
    """ This function checks all database entries associated
    with a set station, destination and line in a town and
    returns a list containing upcomming trains.
    Parameter :
    - station (ex: COMEDIE)
    - destination (ex: SABINES)
    - line (ex: 2)
    - town (ex: Montpellier)
    """
    conn, cursor = create_db.connect()
    cursor.execute("""
    SELECT * FROM info_trafic
    WHERE Arrêt = ? AND Destination = ? AND Ligne = ? AND Ville = ?
    """, (station, destination, line, town))
    liste_passages = []
    for row in cursor:
        liste_passages.append(row)
    conn.commit()
    conn.close()
    return liste_passages
