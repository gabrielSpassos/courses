import requests 

API_ENDPOINT_SWAPI = "https://swapi.co/api/planets/1"

response = requests.get(url = API_ENDPOINT_SWAPI)

print(response.json())
