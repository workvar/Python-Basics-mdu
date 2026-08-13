import requests

url = "https://wttr.in/Dehradun?format=j1"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    city = "Dehradun"
    current = data["current_condition"][0]

    temperature = current["temp_C"]
    condition = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]

    print("========== Weather Information ==========")
    print("City        :", city)
    print("Temperature :", temperature, "°C")
    print("Condition   :", condition)
    print("Humidity    :", humidity, "%")
    print("Wind Speed  :", wind_speed, "km/h")
    print("=========================================")

except requests.exceptions.RequestException as e:
    print("API Request Error:", e)

except (KeyError, IndexError, ValueError) as e:
    print("JSON Parsing Error:", e)