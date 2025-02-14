
import pandas as pd
from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column, Float


engine = create_engine('sqlite:///stations_data.db', echo=True)
meta = MetaData()

# Definicja tabeli 'stations' - ta sama co przy tworzeniu bazy
stations = Table(
    'stations', meta,
    Column('station', String, primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)
)

# Łączenie się z bazą danych
with engine.connect() as conn:
    trans = conn.begin()  # Rozpoczynamy transakcję

    ins = stations.insert().values(
        station='UUUTESTING',
        latitude=0.0,
        longitude=0.0,
        elevation=0.0,
        name='NAMETEST',
        country='COUTEST',
        state='STATEST'
    )
    conn.execute(ins)

    conn.execute(stations.insert(), [
        {
            'station': 'UUUTESTING2',
            'latitude': 10.0,
            'longitude': 10.0,
            'elevation': 10.0,
            'name': 'NAMETEST2',
            'country': 'COUTEST2',
            'state': 'STATEST2'
        },
        {
            'station': 'UUUTESTING3',
            'latitude': 200.0,
            'longitude': 200.0,
            'elevation': 200.0,
            'name': 'NAMETEST3',
            'country': 'COUTEST3',
            'state': 'STATEST3'
        }
    ])

    trans.commit()  # Zatwierdzamy



print("Wstawiono dane do tabeli stations.")

