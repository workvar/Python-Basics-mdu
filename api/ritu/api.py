import requests

api_key = "YOUR_API_KEY"

url = "https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

data = response.json()

print(data)