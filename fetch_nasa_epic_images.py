import requests
from pathlib import Path
from environs import Env

from nasa_api_utils import save_image


def fetch_nasa_epic_images(nasa_api_key):
    """Allow to download EPIC latest images from NASA API"""
    params = {'api_key': nasa_api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_response_data = response.json()
    limit_images = 9
    images = nasa_response_data[:limit_images]
    for image in images:
        year, month, day = image['date'].split()[0].split('-')
        image_title = image['image']
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_title}.png'
        path = f"./images/nasa_epic/{image['date'].split()[0]}"
        Path(path).mkdir(parents=True, exist_ok=True)
        save_image(epic_url, path, image_title, params)
    return None


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env('nasa_api_key')
    fetch_nasa_epic_images(nasa_api_key)


if __name__ == '__main__':
    main()
