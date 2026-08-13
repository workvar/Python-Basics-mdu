import requests
from tabulate import tabulate

URL = "https://wttr.in/Dehradun?format=j1"

response = requests.get(URL)
response.raise_for_status()

data = response.json()

weather = data["current_condition"][0]

city = data["nearest_area"][0]["areaName"][0]["value"]
country = data["nearest_area"][0]["country"][0]["value"]

temperature = weather["temp_C"]
feels_like = weather["FeelsLikeC"]
condition = weather["weatherDesc"][0]["value"]
humidity = weather["humidity"]
wind_speed = weather["windspeedKmph"]
pressure = weather["pressure"]
visibility = weather["visibility"]


# Create table
table = [
    ["Location", f"{city}, {country}"],
    ["Temperature", f"{temperature} °C"],
    ["Feels Like", f"{feels_like} °C"],
    ["Condition", condition],
    ["Humidity", f"{humidity}%"],
    ["Wind Speed", f"{wind_speed} km/h"],
    ["Pressure", f"{pressure} hPa"],
    ["Visibility", f"{visibility} km"]
]


print("\n🌤️ DEHRADUN WEATHER\n")

print(
    tabulate(
        table,
        headers=["Weather", "Value"],
        tablefmt="grid"
    )
)