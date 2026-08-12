import requests

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    weather_data = response.json()

    current_weather = weather_data["current_condition"][0]
    nearest_area = weather_data["nearest_area"][0]

    temperature = current_weather["temp_C"]
    condition = current_weather["weatherDesc"][0]["value"]

    area = nearest_area["areaName"][0]["value"]
    country = nearest_area["country"][0]["value"]
    region = nearest_area["region"][0]["value"]

    chance_of_rain = weather_data["weather"][0]["hourly"][0]["chanceofrain"]

    print("\n--- Weather Information ---")
    print("--------------------------------")
    print(f"Temperature    : {temperature} °C")
    print(f"Condition      : {condition}")
    print(f"Area           : {area}")
    print(f"Country        : {country}")
    print(f"Region         : {region}")
    print(f"Chance of Rain : {chance_of_rain}%")
    print("--------------------------------")

else:
    print("Unable to fetch weather data.")
    print("Server response:", response.text)