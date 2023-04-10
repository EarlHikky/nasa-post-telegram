import os
import requests
from pathlib import Path
from pprint import pprint
from urllib.parse import urlparse


def get_extension(url):
    return os.path.splitext(url)[-1]


def save_image(url, path, image_title):
    response = requests.get(url)
    extension = get_extension(url)
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f'{path}/{image_title}{extension}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(url)
    response.raise_for_status()
    launches = response.json()
    for launch in launches[-1::-1]:
        images = launch['links']['flickr']['original']
        if images:
            flight_number = launch['flight_number']
            path = f'./images/spacex/{flight_number}'
            Path(path).mkdir(parents=True, exist_ok=True)
            for index, image_url in enumerate(images, 1):
                image_title = f'spacex{index}'
                save_image(image_url, path, image_title)
            return


fetch_spacex_last_launch()
