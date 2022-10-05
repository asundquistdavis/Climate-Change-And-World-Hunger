from email.policy import default
from flask import Flask, render_template, request

from data import get_geojson, get_amounts, get_temperatures

app = Flask(__name__)

# index route which serves dashboard for websites
@app.route('/')
def index():
    return render_template('index.html')

# data route which serves data from database
@app.route('/api/v1.0/geaJSON')
def geojson():
    return get_geojson()

@app.route('/api/v1.0/amounts/sums')
def amounts_cats():
    type = request.args.get('type', default='food')
    return get_amounts(type='sum', sum_categories=True, country_code=country_code)

@app.route('/api/v1.0/amounts/categories')
def amounts_cats():
    type = request.args.get('type', default='food')
    return get_amounts(type=type, sum_categories=sum, country_code=country_code)

@app.route('/api/v1.0/temperatures')
def temps():
    pass

if __name__ == '__main__':
    app.run(debug=True)

