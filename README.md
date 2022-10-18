# Overview
This project creates an interactive dashboard that looks at world temperatures and food supply across time.
# Contents
- Resources: Raw data downloaded as csvs and json file
    - FAO.csv
    - GlobalTemperatures.csv
    - countries.geojson
    - countries.csv
- Assets: Images used on the website
- database
    - etl:ipynb: used to develop etl process
    - database.py: sets up database when flask server is run
- static
    - js
        - choropleth.js:
        - charts.js
        - bar_chart.js
    - css
        - styles.css: styles index.html
- app.py: Flask server with two routes - index and data
- data.py: Calls PostgreSQL database for data (read only)
- templates
    - index.html
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
- [Countries GeoJSON](https://datahub.io/core/geo-countries#resource-countries) geojson (23527 KB)
- [Country Codes](https://www.iban.com/country-codes) csv scraped from a webpage (5 KB)
### Work Breakdown (in no particular order... yet)
- Dataset acquisition and SQL schema **As group on 10/03**
- ETL and database initiation **Nhan by 10/06**
- Read data from database programmatically **Andrew by 10/06**
- app.py Flask routes **Andrew**
- index layout + styling (styles.css) **Nhan**
- JS views
    - Leaflet with choropleth layer **Jon**
    - Pie chart **Loukya**
    - Plotly line plot **Loukya**
- readme and project documentation **Andrew by 10/16**
### Views
- **Country Temperature vs Food Availability Graph**: Shows total amount of food available for given country vs average annual global temperature.
- **Country Food Available by type Pie Chart**: Show the amounts of different food types available for the given country.
- **World food Availability Choropleth**: Leaflet world map with chloropleth layer that colors each country based on the amount of food available.
- **Top 10 Food Availability Bar chart**: Bar chart that shows the top 10 countries with most food available.
# Instructions
## Running The Flask Server
- Copy the repo from [here](https://github.com/asundquistdavis/Climate-Change-And-World-Hunger) and clone it onto your machine.
- Open [config_stater.py](/config_starter.py) and enter your postgres username, password and connection port. Ensure the database name does not conflict with an existing postgres database on your machine. After, rename congig_starter.py to config.py
- Create/activate a Python 3 environment that includes pandas, sqlalchemy, sqlalchemy-util, flask and json. A full list of dependencies can be viewed [here](/Assets/dependencies.txt).
- Run app.py using git bash/terminal.
- Note that the app.py automatically creates a postgreSQL database on your machine with all the necessary data.
## Acknowledgments
- https://leafletjs.com/examples/choropleth/
- https://colorbrewer2.org/
- Dom's Tutorial
- copious amounts of google and stack exchange