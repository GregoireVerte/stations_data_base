
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, ForeignKey

# Tworzenie silnika i połączenia z bazą danych
engine = create_engine('sqlite:///stations_data.db', echo=True)
meta = MetaData()

# Definicja tabeli 'stations' z 'station' jako primary_key
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

# Definicja tabeli 'measure' z 'id' jako primary_key oraz 'station' jako foreign_key
measure = Table(
    'measure', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('station', String, ForeignKey('stations.station')),
    Column('date', String),
    Column('precip', Float),
    Column('tobs', Float)
)

# Tworzenie tabel w bazie danych
meta.create_all(engine)

# Wczytywanie danych z plików CSV przy użyciu Pandas
stations_df = pd.read_csv('clean_stations.csv')
measure_df = pd.read_csv('clean_measure.csv')

# Zapisywanie danych do odpowiednich tabel w bazie danych
with engine.begin() as connection:
    # Używamy 'append' dla 'stations', zeby nie nadpisalo struktury tabeli (i zachowalo klucz glowny - primary key)
    stations_df.to_sql('stations', con=connection, if_exists='append', index=False)
    # Dajemy 'append' dla 'measure', żeby nie nadpisywać struktury tabeli a dodać kolumny
    measure_df.to_sql('measure', con=connection, if_exists='append', index=False)




print("Dane zostały załadowane do bazy danych w postaci tabel.")



