import os
import requests

MY_LAT = 51.402560 # Your latitude
MY_LONG = -3.484190 # Your longitude
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.getenv("OWM_API_KEY")
print(api_key)

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

print(data["weather"][0]["description"])
#print(os.getenv("PROJECT_DIR"))
