import webstream
import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from urllib import parse


ENVKEY_IMAGES_DIRECTORY = os.environ["IMAGES_DIRECTORY"]


def remake_directory(dir: str):
    path = Path(dir)
    if path.exists():
        shutil.rmtree(dir)
    path.mkdir(parents=True, exist_ok=False)


def get_file_extension(file_link: str):
    splitted_url = parse.urlsplit(file_link)
    url_path = splitted_url[2]
    unquoted_path = parse.unquote_plus(url_path)
    extension = os.path.splitext(unquoted_path)[1]
    return extension


def get_filename_from_url(url: str):
    parsed_url = parse.urlsplit(url)
    filename = os.path.split(parsed_url.path)[1]
    return filename


def download_image(url: str, file_path_and_ext: str, dir: str=ENVKEY_IMAGES_DIRECTORY):
    Path(dir).mkdir(
        parents=True, exist_ok=True
    )  # make images directory if not present
    response = webstream.get_http(
        url=url, params=None, json=None, max_attempts=50, tickrate=0.2
    )
    with open(f"{file_path_and_ext}", "wb") as file:
        file.write(response.content)
