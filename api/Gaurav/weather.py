import requests

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)
data = response.json()

current_weather = data["current_condition"][0]

temperature = current_weather["temp_C"]
condition = current_weather["weatherDesc"][0]["value"]

print("==============================")
print("      DEHRADUN WEATHER")
print("==============================")
print("City        : Dehradun")
print("Temperature :", temperature, "°C")
print("Condition   :", condition)
print("==============================")
