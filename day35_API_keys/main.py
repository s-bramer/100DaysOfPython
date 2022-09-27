import requests

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_key = "96a1e17cd654862d44b04f13936aab3c"

MY_LAT = 51.402560 # Your latitude
MY_LONG = -3.484190 # Your longitude

parameters = {
"lat": MY_LAT,
"lon": MY_LONG,
"appid": API_key,
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
print(response.json())