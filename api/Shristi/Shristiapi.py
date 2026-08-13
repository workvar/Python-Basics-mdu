import requests

url = "https://wttr.in/Dehradun?format=j1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current_condition"][0]

    temperature = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    condition = current["weatherDesc"][0]["value"]

    print("===== Dehradun Weather =====")
    print("Temperature :", temperature, "°C")
    print("Feels Like  :", feels_like, "°C")
    print("Humidity    :", humidity, "%")
    print("Condition   :", condition)

except requests.exceptions.RequestException as error:
    print("Unable to fetch weather data:", error)
except (KeyError, IndexError, ValueError):
    print("Unable to process the weather data.")