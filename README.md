# Overview

# Proposal
### Group Number: 2
### Group Members
- Loukya Kilari
- Jon Kwiatkowski
- Andrew Sundquist
- Nhan Tran
### Topic and Overview
- We plan to create an interactive webpage that explores connections between world hunger and climate change. We will use a PostgreSQL database to store the cleaned (transformed) data. Our app.py will use Flask to serve data from the database to one route and serve index.html when the dashboard is visited. Our website will include (at least) 3 views: a world food availability Marker map, a country nutrition choropleth and a country temperature vs food availability graph (see below for more specifics).
### Datasets
- [Climate Change: Earth Surface Temperatures](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) csv (202 KB)
- [Who eats the food we grow?](https://www.kaggle.com/datasets/dorbicycle/world-foodfeed-production) csv (4,330 KB)
- [Countries GeoJSON](https://datahub.io/core/geo-countries#resource-countries) JSON (23527 KB)
### Work Breakdown (in no particular order... yet)
- Dataset acquisition and SQL schema **As group on 10/03**
- ETL and database initiation **Nhan by TBD**
- Read data from database programmatically **Andrew by TBD**
- app.py Flask routes **Andrew**
- data.py functions **Andrew**
- index layout + styling (styles.css) **TBD**
- JS views
    - Leaflet with choropleth layer **TBD**
    - Leaflet with markers layer **TBD**
    - Plotly line plot **TBD**
- readme and project documentation **Andrew by 10/16**
 
### Views
- **World Food Availability Marker Map**: Drop down option to select year, Leaflet world map with marker layer that displays food availability info for each country.
- **Country Nutrition Choropleth**: Leaflet world map with chloropleth layer that colors each country based on nutrition conditions that are determined by what types of food are available.
- **Country Temperature vs Food Availability Graph**: Drop down option to select specific country or total world and plotly line chart that graphs food availability vs global world temperature.
 
# Contents
- Resources: Raw data downloaded as csvs and json file
    - FAO.csv (may rename)
    - GlobalTemperatures.csv (may rename)
    - countries.geojson
- Assets: Any images to be used on the website
- database
    - etl.py: transforms raw data from Resources folder and loads into PostgreSQL database
- static
    - js
        - app.js: renders Plotly and Leaflet views for index.html
    - css
        - styles.css: styles index.html
- app.py: Flask server with two routes - index and data
- data.py: Calls PostgreSQL database for data (read only)
- templates
    - index.html: website that contains dashboard with views
