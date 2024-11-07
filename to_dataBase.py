import psycopg2
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')

df = pd.read_csv('char.csv')

df.to_sql(schema='public', name='characters', con=engine, if_exists='replace', index=False, dtype={'created': sqlalchemy.DATE})