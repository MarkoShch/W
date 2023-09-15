import psycopg2
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base
from datetime import datetime

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/postgres")
engine.connect()
print(engine)

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    temp = Column(Integer)
    city = Column(String)


Base.metadata.create_all(engine)