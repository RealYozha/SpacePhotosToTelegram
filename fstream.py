import webstream
import os
import logging
from pathlib import Path
from urllib import parse as urlparse


def create_img_dir(img_dir: str = "./SpaceImages"):
    path_img_dir = Path(img_dir)
    path_img_dir.mkdir(parents=True, exist_ok=True)
    return path_img_dir


def get_file_extension(file_link: str):
    splitted_url = urlparse.urlsplit(file_link)
    url_path = splitted_url[2]
    unquoted_path = urlparse.unquote_plus(url_path)
    extension = os.path.splitext(unquoted_path)[1]
    return extension


def get_filename_from_url(url: str):
    parsed_url = urlparse.urlsplit(url)
    filename = os.path.split(parsed_url.path)[1]
    return filename


def download_image(url: str, file_path_and_ext: str, query: dict = None):
    create_img_dir()
    response = webstream.get_http(
        url=url, params=query, json=None, max_attempts=50, tickrate=0.2
    )
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s ~/%(filename)s:%(funcName)s")
    logging.debug(f"downloading {url} to {file_path_and_ext}")
    with open(f"{file_path_and_ext}", "wb") as file:
        file.write(response.content)
