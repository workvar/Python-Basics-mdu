import requests

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)

if response.status_code == 200:
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
else:
    print("API request failed:", response.status_code)