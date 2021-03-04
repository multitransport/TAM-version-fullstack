from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import fonctions as fc
import create_db

@app.route('/')
def entry_point():
    return render_template('./app.html')


@app.route('/hello_world')
def hello_world():
    return 'Hello World'


@app.route('/<town>/stations')
def all_stations(town):
    create_db.main(town)
    stations = fc.liste_stations('multitrsp.db')
    return jsonify(stations)


@app.route('/<town>/stations/<station>')
def next_trains(town, station):
    create_db.main(town)
    trains = fc.liste_next_trains('multitrsp.db', station)
    return jsonify(trains)


if __name__ == '__main__':
    app.run(debug=True)
