#come collegare un server api a python
import requests
base_url = "https://pokeapi.co/api/v2/"

name = input("Seleziona un pokemon: ")
name = name.lower()

def get_pokemon_info(name):
  url = f"{base_url}/pokemon/{name}"
  response = requests.get(url)

  if response.status_code == 200:
    pokemon = response.json()
    return pokemon
  else:
    print(f"errore{response.status_code}")

pokemon_name = name
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
  print(f"Nome del pokemon: {pokemon_info['name']}")
  print(f"Id del pokemon: {pokemon_info['id']}")
  print(f"Altezza del pokemon: {pokemon_info['height']} cm.")
  print(f"Peso del pokemon: {pokemon_info['weight']} kg.")





  

