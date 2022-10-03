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
def get_amounts_by_years(type='both', all_item=True, country_code='all'):
    data = {}
    with Session(engine) as s:
        # sums all countries and, both types and all items 
        if country_code == 'all' and type == 'both' and all_items:
            years = data['years']
            years = {}
            for year in YEARS:
                ams = s.query(Amount).filter(Amount.year==year).all()
                years[year] = sum([am.amount for am in ams])
        elif country_code == 'all':
            for year in YEARS:
                ams = s.query(Amount).filter(Amount.year==year).filter(Amount.type==type).all()
                items = years[year]
                items = {}
                for am in ams:
                    items[am.item] = am.Amount
        else:
            for year in YEARS:
                ams = s.query(Amount).filter(Amount.year==year).filter(Amount.type==type).all()
                items = years[year]
                items = {}
                for am in ams:
                    items[am.item] = am.Amount


                s.query(Amount).filter(Amount.year==year).filter(Amount.country_code==country_code)
    return data

# get years queries the 
def get_temps():
    data = {'status': 'success: temps'}
    return data


def get_foods():
    data = {'status': 'success: foods'}
    return data

print(YEARS)