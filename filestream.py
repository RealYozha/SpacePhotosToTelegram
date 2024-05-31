import requests
from os import path
from urllib import parse
from time import sleep


def get_file_extension(file_link: str):
    splitted_url = parse.urlsplit(file_link)
    url_path = splitted_url[2]
    unquoted_path = parse.unquote_plus(url_path)
    extension = path.splitext(unquoted_path)[1]
    return extension


def get_filename_from_url(url: str):
    parsed_url = parse.urlsplit(url)
    filename = path.split(parsed_url.path)[1]
    return filename


def download_image(url: str, file_path_and_ext: str):
    response = None
    for attempt in range(100):
        response = requests.get(url)
        response.raise_for_status()
        decoded_response = response.json()
        if 'error' in decoded_response:
            raise requests.exceptions.HTTPError(decoded_response['error'])
        if response or attempt > 100:
            print(f"couldn't recieve any data from the requested server {url}")
            break
        sleep(5)
    with open(f"{file_path_and_ext}", "wb") as file:
        file.write(response.content)
