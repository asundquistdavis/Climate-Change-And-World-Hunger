# *** use sqlalchemy to automap database ***

# load dependencies and get config properties for connection
from curses import ALL_MOUSE_EVENTS
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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

# *** define functions to query database ***

# get temps queries the 
def get_temps():
    data = {'status': 'success: temps'}
    return data

def get_foods():
    data = {'status': 'success: foods'}
    return data