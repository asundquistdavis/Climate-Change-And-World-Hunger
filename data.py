# load dependencies to query database and return json 
from sqlalchemy.orm import Session
from database.database import orm
from json import load

# define the years under scope
YEARS = [1992+x for x in range(22)]

# *** define functions to query database ***

# load geoJSON country data
def get_geojson():
    ams = get_amounts(type='sum', sum_categories=False, country_code='list', year_=1999)['countries']
    with open('Resources/countries.geojson', 'r') as geojson:
        gj = load(geojson)
        for feature in gj['features']:
            code = feature['properties']['ISO_A3']
            try:
                feature['properties']['amount'] = ams[code]
            except:
                feature['properties']['amount'] = 0
        return gj

# get food/feed amounts by year
def get_amounts(type='sum', sum_categories=True, country_code='sum', year_='all'):

    engine, Amount, Year, Country = orm()

    # years is a key in return object and itself is a dict (object) that will hold each year as its keys
    # data = {years: {year1: 'something', ...}}
    data = {}
    data['years'] = {}
    years = data['years']

    with Session(engine) as s:

        # option one: type='sum', sum_categories=False, country_code='list'
        if country_code=='list' and type=='sum':
            
            years['year'] = year_
            data['countries'] = {}
            countries = data['countries']

            ams = s.query(Amount).filter(Amount.year==year_).all()

            keys = []
            for am in ams:
                code = am.country_code
                if code in keys:
                    countries[code] += am.amount
                else:
                    countries[code] = am.amount
                
            
            # keys = []
            # for am, c in rs:
            #     if c.country_code in keys:
            #         countries[c.country_name] += am.amount
            #     else:
            #         countries[c.country_name] = am.amount

        # option two: type='sum', sum_categories=True, country can be any or 'sum'
        elif type == 'sum' and sum_categories:
            
            # sub-otion one: sum countires
            if country_code=='sum':

                # sum amounts for countries, types and categories for each year
                for year in YEARS:

                    ams = s.query(Amount).filter(Amount.year==year).all()
                    years[year] = sum([am.amount for am in ams])

                # reciept status
                data['status'] = f'success: amounts for both types, all categories and summed countries by year'

            # sub-option two: specific country
            else:

                # sum amounts for countries, types and categories for each year
                for year in YEARS:

                    ams = s.query(Amount).filter(Amount.year==year).filter(Amount.country_code==country_code).all()
                    years[year] = sum([am.amount for am in ams])

                # reciept status
                data['status'] = f'success: amounts for both types, all categories and {country_code} by year'
        
        # option three: sum_categories=False, type can be either 'food' of 'feed' and countries can be any or 'sum'
        elif not sum_categories:
            
            # sub-option one: sum countries
            if country_code=='sum':

                for year in YEARS:

                    # data = {years: {year1: {'categories'}, year2: {'categories'}...}
                    years[year] = {}
                    categories = years[year]

                    ams = s.query(Amount).filter(Amount.year==year).filter(Amount.type==type).all() 

                    keys = []
                    for am in ams:
                        
                        category = am.category
                        if category in keys:
                            categories[category] += am.amount
                        else:
                            categories[category] = am.amount
                            keys.append(category)
                
                # reciept status
                data['status'] = f'success: all amounts for all {type} by category and year summed countries'

            # sub option two: specific country
            else:

                for year in YEARS:

                    # data = {years: {year1: {'categories'}, year2: {'categories'}...}
                    years[year] = {}
                    categories = years[year]

                    ams = s.query(Amount).filter(Amount.year==year).filter(Amount.country_code==country_code).filter(Amount.type==type).all() 

                    keys = []
                    for am in ams:
                        
                        category = am.category
                        if category in keys:
                            categories[category] += am.amount
                        else:
                            categories[category] = am.amount
                            keys.append(category)

                # reciept status
                data['status'] = f'success: all amounts for all {type} in {country_code} by category and year'

        # if something else, report error
        else:
            data['status'] = 'error: parameters'

        return data

# get tempertures by year 
def get_temperatures(year='all'):

    engine, Amount, Year, Country = orm()

    data = {}

    with Session(engine) as s:

        # otpion one: 
        if year == 'all':

            data['years'] = {}
            years = data['years']

            for year in YEARS:

                ys = s.query(Year).filter(Year.year==year).all()
                years[year] = {}
                years[year]['temperature'] = sum([y.temperature for y in ys])
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
