import pandas as pd
from extract import get_weather_data

def transform_weather_data(raw_data):
    city = raw_data.get("name")
    temperature_kelvin = raw_data['main']['temp']
    humidity = raw_data["main"]["humidity"]
    description = raw_data["weather"][0]["description"]
    timestamp = raw_data["dt"]

    #clean the data by converting temperature from Kelvin to Celsius
    temperature_celsius = temperature_kelvin - 273.15

    reliable_data = pd.to_datetime(timestamp, unit='s')

    #clean dictionary
    transformed_data = {
        "city": [city],
        "temperature_celsius": [round(temperature_celsius, 2)],
        "humidity": [humidity],
        "description": [description],
        "timestamp": [reliable_data]
    }

    df = pd.DataFrame(transformed_data)
    return df

#run the transformation
if __name__ == "__main__":
    raw_data = get_weather_data()

    if raw_data:
        transformed_df = transform_weather_data(raw_data)
        print("\nTransformed DataFrame:")
        print(transformed_df)
    else:
        print("No data to transform.")