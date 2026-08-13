import requests

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)

data = response.json()

current = data["current_condition"][0]

print("Weather Information")
print("-------------------")
print("Temperature:", current["temp_C"], "°C")
print("Feels Like:", current["FeelsLikeC"], "°C")
print("Humidity:", current["humidity"], "%")
print("Wind Speed:", current["windspeedKmph"], "km/h")
print("Weather:", current["weatherDesc"][0]["value"])