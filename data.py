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
Country = Base.classes.country
Item_Element = Base.classes.item_element
Amount = Base.classes.amount
Year =Base.classes.year

# *** load geoJSON country data ***

    

# *** define functions to query database ***

from sqlalchemy.orm import Session
from json import load

# 
def get_geosjon():
    with open('Resources/countries.geojson', 'r') as data:
        return load(data)

YEARS = [1961+x for x in range(53)]

# 
def get_amounts_by_years(type='both', sum_categories=True, country_code='all'):
    data = {}
    with Session(engine) as s:

        # option one: type='sum', sum_categories=True, country can be any or 'all'
        if type == 'sum' and sum_categories:
            # years = data['years']
            # years = {}
            # for year in YEARS:
            #     ams = s.query(Amount).filter(Amount.year==year).all()
            #     years[year] = sum([am.amount for am in ams])
            
            if country_code=='all':
                data['status'] = f'success: amounts for both types, all categories and all countries by year'

            # specific country
            else:
                data['status'] = f'success: amounts for both types, all categories and {country_code} by year'
        
        # option two: sum_categories=False, type can be either 'food' of 'feed' and countries can be any or 'all'
        elif not sum_categories:
            
            # sum all countries
            if country_code=='all':
                data['status'] = f'success: all amounts for all {type} by category and year for all countries'

            # specific country
            else:
                data['status'] = f'success: all amounts for all {type} and {country_code} by category and year'

        # if something else, report error
        else:
            data['status'] = 'error: parameters'


        return data

# get years queries the 
def get_temps():
    data = {'status': 'success: temps'}
    return data


def get_foods():
    data = {'status': 'success: foods'}
    return data

print(YEARS)