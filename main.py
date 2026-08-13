numbers = [10, 15, 20, 25, 30]
total = 0

for i in range(0, len(numbers)):
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
    count = count + 2

for num in numbers:
    print("Square:", num ** 2)


import requests

API_URL = "https://wttr.in/Dehradun?format=j1"

response = requests.get(API_URL, timeout=10)
response.raise_for_status()

data = response.json()

current = data["current_condition"][0]
location = data["nearest_area"][0]

city = location["areaName"][0]["value"]
temperature = current["temp_C"]
condition = current["weatherDesc"][0]["value"]

print("\n--- Dehradun Weather ---")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Condition:", condition)