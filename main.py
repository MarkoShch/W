from fastapi import  Query, HTTPException
import requests
import json
from typing import Union

from fastapi import FastAPI

app = FastAPI()

import psycopg2
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import Session, sessionmaker
from table import Weather
import requests
import json
@app.get("/WEATHER")
async def read_root(scity: str = Query()):

    api = '79011035a9af358337c2c8495c308c71'
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={scity}&appid={api}')
    json_data = weather.json()
    lat = json_data['coord']['lat']
    lon = json_data['coord']['lon']
    city = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric')
    json_city = city.json()
    temp_json = {
        "city": scity,
        "temperature": json_city['main']['temp'],
    }



    engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/postgres")
    session = Session(bind=engine)

    c3 = Weather(
        temp=temp_json['temperature'],
        city=temp_json['city'],

    )
    session.add_all([c3])
    session.commit()
    return temp_json



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}