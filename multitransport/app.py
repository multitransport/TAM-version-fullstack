import multitransport.fonctions as fc
import multitransport.create_db as create_db
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def entry_point():
    return render_template('./app.html')


@app.route('/hello_world')
def hello_world():
    """ This function says 'Hello, World'. """
    return 'Hello World'


@app.route('/<town>/stations')
def all_stations(town):
    """ This function searches for every train stops
    for a set town.
    Parameter : town (ex: Montpellier)
    Returns : json data
    Example : http://127.0.0.1:5000/Montpellier/stations
    [ "A. BROUSSONET", "A. L. JUSSIEU", "AGROPOLIS", ...,
    "ZI MARBRERIE", "ZONE ARTISANALE", "ZOO" ]
    """
    create_db.main(town)
    stations = fc.liste_stations(town)
    return jsonify(stations)


@app.route('/<town>/stations/<station>')
def next_trains(town, station):
    """ This function searches for the next trains to come
    at a set station no matter the line nor destination.
    Parameters : town, station (ex: Montpellier, BELEVEDERE)
    Returns : json data
    Example : http://127.0.0.1:5000/Montpellier/stations/BELVEDERE
    [ [ [ "10", "BELVEDERE", "AIGUELONGUE", "Montpellier" ],
    [ "20:06:10", "20:36:10", "19:50:13" ] ], ...
    [ [ "15", "BELVEDERE", "SABINES", "Montpellier" ],
    [ "20:21:47", "20:50:51" ] ] ]
    """
    create_db.main(town)
    trains = fc.liste_trains(station, town)
    return jsonify(trains)


@app.route('/<town>/next/')
# ?line=<line>&station=<station>&destination=<destination>')
def next_passages(town):
    """ This function searches for the next trains to come
    at a set station considering a specific line and destination.
    Parameters : town, station, destination (ex: Montpellier, COMEDIE, SABINES)
    Returns : json data
    Example :
    http://127.0.0.1:5000/Montpellier/next?line=2&station=COMEDIE&destination=SABINES
    [ [ "2", "COMEDIE", "SABINES", "19:46:09", "Montpellier" ],
    [ "2", "COMEDIE", "SABINES", "19:58:21", "Montpellier" ] ]
    """
    station = request.args.get('station')
    destination = request.args.get('destination')
    line = request.args.get('line')
    create_db.main(town)
    passage = fc.liste_next(station, destination, line, town)
    return jsonify(passage)


# if __name__ == '__main__':
#     app.run(debug=True)
