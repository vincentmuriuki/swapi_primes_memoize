import os
import requests

def get_characters():
    url = "https://swapi.co/api/people/"
    r = requests.get(url)
    fav_chars = r.json()
    items = fav_chars['results']
    for item in items:
        print(item["name"], item["eye_color"], item["birth_year"])
    fav_list = []
    return items
