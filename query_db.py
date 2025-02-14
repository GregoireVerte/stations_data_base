
import pandas as pd
from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column, text

## Tworzymy silnik połączenia z istniejącą bazą danych ##
#engine = create_engine('sqlite:///stations_data.db', echo=True)
engine = create_engine('sqlite:///stations_data.db')

meta = MetaData()

meta.reflect(bind=engine)

# Odczytujemy definicje tabel ze schematu bazy danych
stations = Table('stations', meta, autoload_with=engine)
measure = Table('measure', meta, autoload_with=engine)

# Połączenie z bazą danych
with engine.connect() as conn:
    print("Pierwsze 4 rekordy z tabeli 'stations':")
    result = conn.execute(text("SELECT * FROM stations LIMIT 4")).fetchall()
    for row in result:
        print(row)

    print("\n")


    print("Rekordy z tabeli 'measure' gdzie tobs > 84:")
    s = measure.select().where(measure.c.tobs > 84)
    result = conn.execute(s)

    for row in result:
        print(row)
