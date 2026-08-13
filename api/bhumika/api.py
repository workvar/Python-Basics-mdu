import requests

url = "https://wttr.in/Dehradun?format=j1"

response = requests.get(url)
data = response.json()
print(data)
