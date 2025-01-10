import webstream
import os
from shutil import rmtree
from pathlib import Path
from dotenv import load_dotenv
from urllib import parse as urlparse


def remake_directory(_dir: str):
    ndir = Path(_dir)
    if ndir.exists():
        rmtree(ndir)
    ndir.mkdir(parents=True, exist_ok=False)


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


def download_image(url: str, file_path_and_ext: str, img_dir: str):
    Path(img_dir).mkdir(
        parents=True, exist_ok=True
    )  # make images directory if not present
    response = webstream.get_http(
        url=url, params=None, json=None, max_attempts=50, tickrate=0.2
    )
    with open(f"{file_path_and_ext}", "wb") as file:
        file.write(response.content)
