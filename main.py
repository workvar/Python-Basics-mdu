import requests

numbers = [10, 15, 20, 25, 30]
total = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print("Even number:", numbers[i])
        total += numbers[i]
    else:
        print("Odd number:", numbers[i])

print("Total of even numbers:", total)

count = 0

while count < len(numbers):
    if numbers[count] > 20:
        print("Large:", numbers[count])
    count += 1

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

    print("\n===== Dehradun Weather =====")
    print("Temperature :", temperature, "°C")
    print("Feels Like  :", feels_like, "°C")
    print("Humidity    :", humidity, "%")
    print("Condition   :", condition)

except requests.RequestException as error:
    print("API request failed:", error)

except (KeyError, IndexError, ValueError) as error:
    print("Invalid API response:", error)

for num in numbers:
    print("Square:", num ** 2)