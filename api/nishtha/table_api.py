import requests

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]
area = data["nearest_area"][0]
weather = data["weather"][0]

print("Weather Information")
print("-----------------------------------")
print("Temperature |", current["temp_C"], "°C")
print("Weather     |", current["weatherDesc"][0]["value"])
print("City        |", area["areaName"][0]["value"])
print("Country     |", area["country"][0]["value"])
print("Region      |", area["region"][0]["value"])
print("Chance Rain |", weather["hourly"][0]["chanceofrain"], "%")
print("-----------------------------------")