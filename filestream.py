import webstream
import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from urllib import parse


def remake_image_directory():
    path = Path(os.environ["IMAGES_DIRECTORY"])
    if path.exists():
        shutil.rmtree(os.environ["IMAGES_DIRECTORY"])
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


def download_image(url: str, file_path_and_ext: str):
    response = webstream.http_get(url=url,
                                  params=None,
                                  json=None,
                                  max_attempts=50,
                                  tickrate=0.2) # no! don't you dare use your own bad code!
    with open(f"{file_path_and_ext}", "wb") as file:
        file.write(response.content)
