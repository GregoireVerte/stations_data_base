
from sqlalchemy import create_engine, MetaData, Table


engine = create_engine('sqlite:///stations_data.db', echo=True)

meta = MetaData()


stations = Table(
    'stations', meta,
    autoload_with=engine
)


with engine.connect() as conn:
    trans = conn.begin()
    
    update_query = stations.update().where(stations.c.longitude == 200).values(longitude=1500, elevation=900)
    conn.execute(update_query)
    
    trans.commit()

print("UPDATE w tabeli stations!")
