import requests

api_key = "YOUR_API_KEY"

url =  "https://wttr.in/Dehradun?format=j1"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

data = response.json()

print(data)
