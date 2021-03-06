import multitransport.fonctions as fc
import multitransport.create_db as create_db
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def entry_point():
    return render_template('./app.html')


@app.route('/hello_world')
def hello_world():
    return 'Hello World'


@app.route('/<town>/stations')
def all_stations(town):
    create_db.main(town)
    stations = fc.liste_stations(town)
    return jsonify(stations)


@app.route('/<town>/stations/<station>')
def next_trains(town, station):
    create_db.main(town)
    trains = fc.liste_trains(station, town)
    return jsonify(trains)


@app.route('/<town>/next/')
# ?line=<line>&station=<station>&destination=<destination>')
def next_passages(town):
    station = request.args.get('station')
    destination = request.args.get('destination')
    line = request.args.get('line')
    create_db.main(town)
    passage = fc.liste_next(station, destination, line, town)
    return jsonify(passage)


# if __name__ == '__main__':
#     app.run(debug=True)
