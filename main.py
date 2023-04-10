import requests
import re
import logging
from pathlib import Path
from os.path import splitext
from pprint import pprint
from urllib.parse import urlparse
from environs import Env


def get_extension(url):
    _, extension = splitext(urlparse(url).path)
    return extension


def save_image(url, path, image_title, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    extension = get_extension(url)
    with open(f'{path}/{image_title}{extension}', 'wb') as file:
        file.write(response.content)
    return None


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
            return None


def fetch_nasa_images(NASA_API_KEY):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': NASA_API_KEY, 'count': 10}
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
    return None


def fetch_nasa_epic_images(NASA_API_KEY):
    params = {'api_key': NASA_API_KEY}
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url, params=params)
    response.raise_for_status()
    response_json = response.json()
    images = response_json[:9] if not len(response_json) <= 9 else response_json
    for image in images:
        year, month, day = image['date'].split()[0].split('-')
        image_title = image['image']
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_title}.png'
        path = f"./images/nasa_epic/{image['date'].split()[0]}"
        Path(path).mkdir(parents=True, exist_ok=True)
        save_image(epic_url, path, image_title, params)
    return None


def main():
    logging.basicConfig(level=logging.DEBUG)
    env = Env()
    env.read_env()
    NASA_API_KEY = env('NASA_API_KEY')
    # fetch_spacex_last_launch()
    # fetch_nasa_images(NASA_API_KEY)
    fetch_nasa_epic_images(NASA_API_KEY)


if __name__ == '__main__':
    main()
