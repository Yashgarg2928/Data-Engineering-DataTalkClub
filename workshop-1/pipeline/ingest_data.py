import pandas as pd 
from sqlalchemy import create_engine
from tqdm.auto import tqdm



dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}


parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]






def run():
    pg_user = 'root'
    pg_pass = "root"
    pg_host = 'localhost'
    pg_db = 'ny_taxi'
    pg_port = 5430

    year = 2021
    month = "01"
    chunksize = 100000
    target_table = "yellow_taxi_data"

    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    engine = create_engine(f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/ny_taxi")

    df_iter = pd.read_csv(
        prefix + f'yellow_tripdata_{year}-{month}.csv.gz',
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize
    )

    first = True
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.to_sql(
                con=engine, 
                name=target_table, 
                if_exists='replace'
                )
            first = False 
        
        df_chunk.to_sql(
            name='yellow_taxi_data',
            con=engine,
            if_exists='append'
        )



if __name__ == "__main__":
    run()