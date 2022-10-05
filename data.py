# *** use sqlalchemy to automap database ***

# load dependencies and get config properties for connection
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from config import user, password, port

# create postgres connection and automap tables to classes
engine = create_engine(f'postgresql://{user}:{password}@127.0.0.1:5432/whgw_db')
Base = automap_base()
Base.prepare(autoload_with=engine)

# declare class for each table in db
Amount = Base.classes.amount
# class Amount():
#   amount_id ~ int
#   amount ~ int
#   country_code ~ str
#   category ~ str
#   type ~ str
#   year ~ int, pk year.year

Year =Base.classes.year
# class Year():
#   year ~ int
#   temperature ~ float
#   tmeperature_unc ~ float

# load dependencies to query database and return json 
from sqlalchemy.orm import Session
from json import load

# define the years under scope
YEARS = [1961+x for x in range(53)]

# *** define functions to query database ***

# load geoJSON country data
def get_geojson():
    with open('Resources/countries.geojson', 'r') as data:
        return load(data)

# get food/feed amounts by year
def get_amounts(type='sum', sum_categories=True, country_code='all'):

    # years is a key in return object and itself is a dict (object) that will hold each year as its keys
    # data = {years: {year1: 'something', ...}}
    data = {}
    years = data['years']
    years = {}

    with Session(engine) as s:

        # option one: type='sum', sum_categories=True, country can be any or 'all'
        if type == 'sum' and sum_categories:
            
            # sub-otion one: sum countires
            if country_code=='all':

                # sum amounts for countries, types and categories for each year
                for year in YEARS:

                    ams = s.query(Amount).filter(Amount.year==year).all()
                    years[year] = sum([am.amount for am in ams])

                # reciept status
                data['status'] = f'success: amounts for both types, all categories and all countries by year'

            # sub-option two: specific country
            else:

                # sum amounts for countries, types and categories for each year
                for year in YEARS:

                    ams = s.query(Amount).filter(Amount.year==year).filter(Amount.country_code==country_code).all()
                    years[year] = sum([am.amount for am in ams])

                # reciept status
                data['status'] = f'success: amounts for both types, all categories and {country_code} by year'
        
        # option two: sum_categories=False, type can be either 'food' of 'feed' and countries can be any or 'all'
        elif not sum_categories:
            
            # sub-option one: sum all countries
            if country_code=='all':

                for year in YEARS:
                
                    # categories is the value of the year key in years and categories is a dict with each cat as keys and amounts as values
                    #  data = {years: {year1: {cat1: amount, ...}, ...}}
                    years[year] = {}
                    categories = years[year]
                    categories = {}

                    ams = s.query(Amount).filter(Amount.year==year).filter(Amount.type==type).all()

                    # sum all amounts of same category
                    keys = []
                    for am in ams:
                        category = am.category
                        if not (category in keys):
                            categories[category] = am.amount
                            keys.append(category)
                        else:
                            categories[category] += am.amount

                # reciept status
                data['status'] = f'success: all amounts for all {type} by category and year for all countries'

            # sub option two: specific country
            else:

                for year in YEARS:
                
                    # categories is the value of the year key in years and categories is a dict with each cat as keys and amounts as values
                    #  data = {years: {year1: {cat1: amount, ...}, ...}}
                    years[year] = {}
                    categories = years[year]
                    categories = {}

                    ams = s.query(Amount).filter(Amount.year==year).filter(Amount.type==type).filter(Amount.country_code==country_code).all()

                    # sum all amounts of same category
                    keys = []
                    for am in ams:
                        category = am.category
                        if not (category in keys):
                            categories[category] = am.amount
                            keys.append(category)
                        else:
                            categories[category] += am.amount

                # reciept status
                data['status'] = f'success: all amounts for all {type} and {country_code} by category and year'

        # if something else, report error
        else:
            data['status'] = 'error: parameters'

        return data

# get tempertures by year 
def get_temperatures(year='all'):

    data = {}

    with Session(engine) as s:

        # otpion one: 
        if year == 'all':

            years = data['years']
            years = {}

            for year in YEARS:

                ys = s.query(Year).filter(Year.year==year).all()
                years[year] = {}
                years[year]['tempurature'] = sum([y.temperature for y in ys])
                years[year]['uncertainty'] = sum([y.uncertainty for y in ys])
        
            # reciept status
            data['status'] = 'success: temps for all years'
    
        else:

            s.query(Year).filter(Year.year==year).all()
            data['temperature'] = sum([y.temperature for y in ys])
            data['uncertainty'] = sum([y.uncertainty for y in ys])

            # reciept status
            data['status'] = f'success: temps for {year}'
    
    return data
