import pandas as pd
import requests as req
import psycopg2
import sqlalchemy
import os

pages = req.get('https://rickandmortyapi.com/api/character').json()['info']['pages']
frames = []

for i in range(1, pages+1):
    temp = pd.DataFrame(req.get(f'https://rickandmortyapi.com/api/character/?page={i}').json()['results'])
    tempOrigin = pd.DataFrame([origin['origin']['name'] for origin in req.get(f'https://rickandmortyapi.com/api/character/?page={i}').json()['results']])
    tempLocation = pd.DataFrame([location['location']['name'] for location in req.get(f'https://rickandmortyapi.com/api/character/?page={i}').json()['results']])
    temp.insert(len(temp.columns), "origin_name", tempOrigin)
    temp.insert(len(temp.columns), "location_name", tempLocation)
    temp = temp.drop('origin', axis=1).drop('location', axis=1).drop('episode', axis=1)
    frames.append(temp)
    print(str(round((len(frames)/pages)*100)) + '%')

df = pd.concat(frames)
df.to_csv('char.csv', index=False)

engine = sqlalchemy.create_engine(f'postgresql+psycopg2://postgres:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/postgres')

df = pd.read_csv('char.csv')

df.to_sql(schema='public', name='characters', con=engine, if_exists='replace', index=False, dtype={'created': sqlalchemy.DATE})

print("Загрузка в базу завершена")