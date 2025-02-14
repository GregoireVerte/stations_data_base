
from sqlalchemy import create_engine, MetaData, Table


engine = create_engine('sqlite:///stations_data.db', echo=True)
meta = MetaData()


stations = Table(
    'stations', meta,
    autoload_with=engine
)


with engine.connect() as conn:
    trans = conn.begin()

    delete_query = stations.delete().where(stations.c.latitude == 0.0)
    conn.execute(delete_query)

    trans.commit()


print("Usunięcie wierszy z latitude = 0.0 z tabeli stations.")

