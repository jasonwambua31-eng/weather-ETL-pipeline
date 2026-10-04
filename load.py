import sqlite3
import pandas as pd
from transform import transform_weather_data
from extract import get_weather_data

def load_data_to_sqlite(df):
    #connecting to the SQLite database 
    conn = sqlite3.connect("weather_data.db")
    #load pandas DataFrame to sqlite database
    df.to_sql("weather", conn, if_exists="append", index=False)
    print("Data loaded into sqlite database successfully.")

    #verification: read the data back from the database
    print("\n Verifying the loaded data:")
    verify_query = "SELECT * FROM weather"
    saved_df = pd.read_sql(verify_query, conn)
    print(saved_df)

    #close the connection 
    conn.close()
#run the load process
if __name__ == "__main__":
    print("started the load process")

    #run the whole pipeline 
    raw_data = get_weather_data()

    if raw_data:
        cleaned_data = transform_weather_data(raw_data)
        load_data_to_sqlite(cleaned_data)
    else:
            print("No data to load into the database.")