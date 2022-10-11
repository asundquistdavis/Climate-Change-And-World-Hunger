from flask import Flask, render_template, jsonify

from data import get_geojson, get_amounts, get_temperatures, orm

from database import database

app = Flask(__name__)

# index route which serves dashboard for websites
@app.route('/')
def index():
    return render_template('index.html')

# data route which serves data from database
@app.route('/api/v1.0/geojson')
def geojson():
    return jsonify(get_geojson())

@app.route('/api/v1.0/amounts')
def amounts():
    return jsonify(get_amounts())

@app.route('/api/v1.0/amounts/countries//<year>')
def amounts_countries(year):
    return jsonify(get_amounts(type='sum', sum_categories=False, country_code='list', year_=year))

@app.route('/api/v1.0/amounts/years/<country_code>/<type>')
def amounts_cats(country_code, type):
    return jsonify(get_amounts(type=type, sum_categories=False, country_code=country_code))

@app.route('/api/v1.0/temperatures')
def temperatures():
    return jsonify(get_temperatures())

if __name__ == '__main__':
    database
    app.run(debug=True)


