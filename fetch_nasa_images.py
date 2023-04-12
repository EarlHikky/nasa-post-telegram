import re
import requests
from pathlib import Path
from environs import Env

from nasa_api_utils import save_image


def fetch_nasa_images(nasa_api_key):
    """Allow to download random images from NASA API"""
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_api_key, 'count': 40}
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


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env('nasa_api_key')
    fetch_nasa_images(nasa_api_key)


if __name__ == '__main__':
    main()
