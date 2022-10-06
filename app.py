from email.policy import default
from flask import Flask, render_template, request

from data import get_geojson, get_amounts, get_temperatures

app = Flask(__name__)

# index route which serves dashboard for websites
@app.route('/')
def index():
    return render_template('index.html')

# data route which serves data from database
@app.route('/api/v1.0/geojson')
def geojson():
    return get_geojson()

@app.route('/api/v1.0/amounts')
def amounts():
    return get_amounts()

@app.route('/api/v1.0/amounts/<country_code>/<type>')
def amounts_cats(country_code, type):
    return get_amounts(type=type, sum_categories=False, country_code=country_code)

@app.route('/api/v1.0/temperatures')
def temperatures():
    return get_temperatures()

if __name__ == '__main__':
    app.run(debug=True)

