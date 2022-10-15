from flask import Flask, render_template, jsonify

from data import get_geojson, get_amounts, get_temperatures, orm

from database import database

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# index route which serves dashboard for websites
@app.route('/')
def index():
    return render_template('index.html')

# api/v1.0 route which serves data from database
@app.route('/api/v1.0/geojson')
def geojson():
    return jsonify(get_geojson())

@app.route('/api/v1.0/amounts/<country>')
def amounts(country):
    return jsonify(get_amounts(country_code=country))

@app.route('/api/v1.0/amounts/countries/<year>')
def amounts_countries(year):
    return jsonify(get_amounts(type='sum', sum_categories=False, country_code='list', year_=year))

@app.route('/api/v1.0/amounts/years/<country_code>/<type>')
def amounts_cats(country_code, type):
    return jsonify(get_amounts(type=type, sum_categories=False, country_code=country_code))

@app.route('/api/v1.0/temperatures')
def temperatures():
    return jsonify(get_temperatures())

from data import get_line_chart, get_pie_chart, get_choropleth, get_bar_chart

# api/v2.0 routes which sercces 
@app.route('/api/v2.0/linechart/<country>')
def lineChart(country):
    # data = {year: [], temperature: [], amount: []}
    data = get_line_chart(country)
    return jsonify(data)

@app.route('/api/v2.0/piechart/<country>/<year>')
def pieChart(country, year):
    # data = {categories: [], amounts: {}}
    data = get_pie_chart(country, year)
    return jsonify(data)

@app.route('/api/v2.0/choropleth/<year>')
def choropleth(year):
    # data = {type: featureCollection, features: [{type: feature, properties: {ADMIN: string, ISO_A3: string, amount: #}, geometry: { -geojson geometry- }}}]}
    data = get_choropleth(year)
    return jsonify(data)

@app.route('/api/v2.0/barchart/<year>')
def barChart(year):
    # data = {country: [], amount: []}
    data = get_bar_chart(year)
    return jsonify(data)

if __name__ == '__main__':
    database
    app.run(debug=True)