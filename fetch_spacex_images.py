import argparse

import requests
from pathlib import Path

from nasa_api_utils import save_image


def fetch_spacex_launch(launch_id):
    """Allow download images in launch if exist"""
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()
    images = launch['links']['flickr']['original']
    if images:
        get_images(launch, images)


def find_spacex_launch_photo():
    """Allow to find and download images in previous launches"""
    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(url)
    response.raise_for_status()
    launches = response.json()
    for launch in launches[-1::-1]:
        images = launch['links']['flickr']['original']
        if images:
            get_images(launch, images)


def get_images(launch, images):
    flight_number = launch['flight_number']
    path = f'./images/spacex/{flight_number}'
    Path(path).mkdir(parents=True, exist_ok=True)
    for index, image_url in enumerate(images, 1):
        image_title = f'spacex{index}'
        save_image(image_url, path, image_title)


def main():
    parser = argparse.ArgumentParser(description='Получение фото запуска spacex')
    parser.add_argument("--launch_id", help="id запуска", default='latest')
    launch_id = parser.parse_args().launch_id
    fetch_spacex_launch(launch_id)


if __name__ == '__main__':
    main()
