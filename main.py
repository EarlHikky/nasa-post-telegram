import requests
import re
from pathlib import Path
from os.path import splitext
from os.path import split as splittitle
from pprint import pprint
from urllib.parse import urlparse
from environs import Env


def get_extension(url):
    _, extension = splitext(urlparse(url).path)
    return extension


def save_image(url, path, image_title):
    response = requests.get(url)
    extension = get_extension(url)
    with open(f'{path}/{image_title}{extension}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/'
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


def fetch_nasa_images():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': env('NASA_API_KEY'), 'count': 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for image in images:
        if image['media_type'] == 'image':
            url = image['hdurl'] if image['hdurl'] else image['url']
            path = './images/nasa'
            Path(path).mkdir(parents=True, exist_ok=True)
            image_title = re.sub(r'\W', '', image['title'])
            save_image(url, path, image_title)


env = Env()
env.read_env()

fetch_spacex_last_launch()
fetch_nasa_images()
