import json
import requests

USE_MOCK_DATA = True
api_key = "dfda0e150b16b87cb5c9accae8d55138"
city = "Nairobi"


def get_weather_data():
    if USE_MOCK_DATA:
        print("Using mock data for weather information.")
        return {
            "name": "Nairobi",
            "main": {"temp": 288.15, "humidity": 82},
            "weather": [{"description": "scattered clouds"}],
            "dt": 1690000000,
        }

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    print(f"Fetching weather data from API: {url}")
    #geting response from the api
    response = requests.get(url)

# here we are checking if the response is successful
    if response.status_code == 200:
        return response.json()

    print(f"Error fetching data from API: {response.status_code}")
    return None

#getting the extaraction
if __name__ == "__main__":
    raw_data = get_weather_data()

    if raw_data:
        print("\n here is the the new data we got from the api:")
        print(json.dumps(raw_data, indent=4))
    else:
        print("Failed to extract the data from the API.")
    
    