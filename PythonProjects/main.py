import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKKEN = '3a51bc1e646b5b33c0ca4523b9b8df5b'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKKEN}


body_create = {
    "name": "Матрёшка2222",
    "photo_id": 719
    }

body_rename ={
    "pokemon_id":"258946" ,
    "name": "Медуница",
    "photo_id": 719
}

body_pokeball ={
    "pokemon_id": "258946"

}

'''response_create=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)
print(response_create.status_code)'''

response_rename=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_rename)
print(response_rename.text)
print(response_rename.status_code)

response_pokeball =requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_pokeball.text)
print(response_pokeball.status_code)