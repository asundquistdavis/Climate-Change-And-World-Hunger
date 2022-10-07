import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from config import user, password, port

def load_database(engine):

    temperatures_path = "../Resources/GlobalTemperatures.csv"
    amounts_path = "../Resources/FAO.csv"

    temperatures_df_1 = pd.read_csv(temperatures_path)
    temperatures_df_1.dropna()
    temperatures_df_1["year"] = pd.to_datetime(temperatures_df_1["dt"]).dt.year
    temperatures_df_2  = temperatures_df_1.groupby("year", as_index = False).mean()
    temperatures_df_2 = temperatures_df_2[(temperatures_df_2["year"] >= 1992) & (temperatures_df_2["year"] <= 2013)]
    temperatures_df_3 = temperatures_df_2[["year", "LandAverageTemperature", "LandAverageTemperatureUncertainty"]]
    temperatures_df_3 = temperatures_df_3.rename(columns = {"LandAverageTemperature": "temperature", "LandAverageTemperatureUncertainty": "uncertainty"})

    temperatures_df_3.to_sql(name='year', con=engine, if_exists='replace', index=False)

    # load food and feed amounts csv
    amounts_df_1 = pd.read_csv(amounts_path, encoding = "cp1252")
    # Organising resources into food groups
    # Grain
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2511, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2805, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2513, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2514, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2517, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2520, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2905, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2515, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2516, "Item Code"] = "Grain"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2518, "Item Code"] = "Grain"
    # Vegetable
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2531, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2537, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2549, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2605, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2907, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2911, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2918, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2532, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2533, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2534, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2546, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2547, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2555, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2556, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2558, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2570, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2602, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2641, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2775, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2570, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2557, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2559, "Item Code"] = "Vegetable"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2535, "Item Code"] = "Vegetable"
    # Protein
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2551, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2561, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2633, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2744, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2761, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2912, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2913, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2960, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2762, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2763, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2764, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2765, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2766, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2767, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2769, "Item Code"] = "Protein"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2949, "Item Code"] = "Protein"
    # Fruit
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2560, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2563, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2601, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2611, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2614, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2615, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2617, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2618, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2619, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2620, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2625, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2919, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2612, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2616, "Item Code"] = "Fruit"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2613, "Item Code"] = "Fruit"
    # Fats/Oils/Sweets
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2582, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2781, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2536, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2542, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2543, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2745, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2571, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2572, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2782, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2573, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2574, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2575, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2577, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2579, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2580, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2586, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2737, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2908, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2909, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2914, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2946, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2562, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2578, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2576, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2541, "Item Code"] = "Fats/Oils/Sweets"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2581, "Item Code"] = "Fats/Oils/Sweets"
    # Meats
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2731, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2732, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2734, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2735, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2736, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2943, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2945, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2733, "Item Code"] = "Meat"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2768, "Item Code"] = "Meat"
    # Dairy
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2740, "Item Code"] = "Dairy"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2743, "Item Code"] = "Dairy"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2848, "Item Code"] = "Dairy"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2948, "Item Code"] = "Dairy"
    # Others
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2640, "Item Code"] = "Others"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2645, "Item Code"] = "Others"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2680, "Item Code"] = "Others"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2922, "Item Code"] = "Others"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2923, "Item Code"] = "Others"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2928, "Item Code"] = "Others"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2961, "Item Code"] = "Others"
    amounts_df_1.loc[amounts_df_1["Item Code"] == 2642, "Item Code"] = "Others"

    amounts_df_2 = amounts_df_1.groupby(["Item Code","Area Abbreviation", "Element"], as_index= False).sum() 
    amounts_df_2 = amounts_df_2[["Item Code", "Area Abbreviation", "Element", "Y1992","Y1993","Y1994","Y1995","Y1996","Y1997","Y1998","Y1999","Y2000","Y2001","Y2002","Y2003","Y2004","Y2005","Y2006","Y2007","Y2008","Y2009","Y2010","Y2011","Y2012","Y2013"]]
    amounts_df_2 = amounts_df_2.rename(columns = {"Y1992" : "1992", "Y1993" : "1993", "Y1994" : "1994","Y1995" : "1995","Y1996" : "1996","Y1997" : "1997","Y1998" : "1998","Y1999" : "1999","Y2000" : "2000", "Y2001" : "2001", "Y2002" : "2002", "Y2003" : "2003", "Y2004" : "2004", "Y2005" : "2005","Y2006" : "2006", "Y2007" : "2007", "Y2008" : "2008", "Y2009" : "2009", "Y2010" : "2010", "Y2011" : "2011", "Y2012" : "2012", "Y2013" : "2013"})
    amounts_df_3 = (amounts_df_2.melt(id_vars=['Item Code', "Area Abbreviation", "Element"],var_name='Year', value_vars = ["1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013"]))
    amounts_df_3["Year"] = amounts_df_3["Year"].apply(pd.to_numeric)
    amounts_df_4 = amounts_df_3.rename(columns = {"Item Code": "category", "Area Abbreviation" : "country_code", "Element" : "type" , "Year" : "year", "value": "amount"})

    amounts_df_4.to_sql(name='amount', con=engine, if_exists='replace', index=False)

def add_orm_to_database(engine):

    Base = declarative_base()
    class Amount(Base):
        __tablename__ = 'amount'
        amount_id = Column(Integer, primary_key=True)
        amount = Column(Integer)
        country_code = Column(Integer)
        category = Column(String)
        type = Column(String)
        year = Column(Integer)

    class Year(Base):
        __tablename__ = 'year'
        year = Column(Integer, primary_key=True)
        temperature = Column(Float)
        temperature_unc = Column(Float)

    Base.metadata.create_all(engine)

def init_database(db, engine):
    
    create_database(engine.url)

    add_orm_to_database(engine)
    
    # load_database(engine)

db = 'test_db'

engine = create_engine(f'postgresql://{user}:{password}@localhost:{port}/{db}')
if not database_exists(engine.url):
    init_database(db, engine)