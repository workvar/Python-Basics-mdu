import requests
from tabulate import tabulate
url = "https://wttr.in/Dehradun?format=j1"
response = requests.get(url)

print("Status code:", response.status_code)

weather_data = response.json()
# print("Weather data:", weather_data)
# or print(response.json())

#  Current Weather
current_weather = weather_data["current_condition"][0]
temperature = current_weather["temp_C"]
condition = current_weather["weatherDesc"][0]["value"]

#  Nearest Area
nearest_area = weather_data["nearest_area"][0]

area = nearest_area["areaName"][0]["value"]
country = nearest_area["country"][0]["value"]
region= nearest_area["region"][0]["value"]

# Weather / Chance of rain
weather = weather_data["weather"][0]
hourly= weather["hourly"]

chance_of_rain = hourly[0]["chanceofrain"]

# Table
table=[
    ["current_condition","temp_c",temperature],
    ["current_condition","weatherDesc",condition],
    ["nearest_area","areaName",area],
    ["nearest_area","country",country],
    ["nearest_area","region",region],
    ["weather","chanceOfRain",chance_of_rain]
]

print("\n--- Dehradun Weather Data ---")
print(
    tabulate(table, headers=["Category", "Information", "Value"],
             tablefmt="grid")
)