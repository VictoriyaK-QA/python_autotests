import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKKEN = '3a51bc1e646b5b33c0ca4523b9b8df5b'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKKEN}
TRAINER_ID = '22874'

def test_status_code():
  response=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
  assert response.status_code == 200

def test_part_of_response():
  response_get=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
  assert response_get.json()["data"][0]["trainer_name"]== 'Фудзияма'