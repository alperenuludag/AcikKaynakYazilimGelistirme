
import requests

URL = "https://rickandmortyapi.com/api/character/146"

result = requests.get(URL)

data= result.json()

print(data)

# output : {'id': 146, 'name': 'Glexo Slim Slom', 'status': 'Alive', 'species': 'Alien', 'type': '', 'gender': 'Male', 'origin': {'name': 'unknown', 'url': ''}, 'location': {'name': 'Nuptia 4', 'url': 'https://rickandmortyapi.com/api/location/13'}, 'image': 'https://rickandmortyapi.com/api/character/avatar/146.jpeg', 'episode': ['https://rickandmortyapi.com/api/episode/18'], 'url': 'https://rickandmortyapi.com/api/character/146', 'created': '2017-12-29T11:28:29.380Z'}

