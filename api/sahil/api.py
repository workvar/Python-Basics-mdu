import requests
from tabulate import tabulate

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)
data = response.json()

area_name = data['nearest_area'][0]['areaName'][0]['value']
state_name = data['nearest_area'][0]['region'][0]['value']

temp_c = data['current_condition'][0]['temp_C']
humidity = data['current_condition'][0]['humidity']
wind_speed = data['current_condition'][0]['windspeedKmph']


print(tabulate([[area_name, state_name, temp_c, humidity, wind_speed]], headers=["Area Name", "State Name", "Temperature (°C)", "Humidity (%)", "Wind Speed (Kmph)"], tablefmt="grid"))





'''
print("area_name:", area_name)
print("state_name:", state_name)
print("temp_c:", temp_c)
print("humidity:", humidity)
print("wind_speed:", wind_speed)
print()



k = data.keys()
print(k)
print()
cc= data['nearest_area'][0]
print(cc)
'''