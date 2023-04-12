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
    env = Env()
    env.read_env()
    nasa_api_key = env('nasa_api_key')
    fetch_nasa_epic_images(nasa_api_key)


if __name__ == '__main__':
    main()
