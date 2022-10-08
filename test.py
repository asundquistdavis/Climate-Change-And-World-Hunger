from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

from database import database
from config import user, password, port
db = 'test_db'

engine = create_engine(f'postgresql://{user}:{password}@localhost:{port}/{db}')

def init_database():
    
    # create database
    create_database(engine.url)

    # define orm mapping

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

    database.load_database()

if not database_exists(engine.url):
    init_database()