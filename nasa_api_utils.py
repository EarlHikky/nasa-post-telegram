import requests
from os.path import splitext
from urllib.parse import urlparse


def get_extension(url):
    _, extension = splitext(urlparse(url).path)
    return extension


def save_image(url, path, image_title, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    extension = get_extension(url)
    with open(f'{path}/{image_title}{extension}', 'wb') as file:
        file.write(response.content)

