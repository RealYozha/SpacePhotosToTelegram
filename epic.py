# SpacePhotosToTelegram/epic.py{0x22}
import argparse
import fstream
import webstream
import convert
from pathlib import Path
import os
from time import sleep
from dotenv import load_dotenv


def get_epic_url(x, i: int):
    a = str.split(x[i]["date"]," ")[0]
    d = convert.change_splitter(a,"-","/")
    n = x[i]["image"]
    return f"https://api.nasa.gov/EPIC/archive/natural/{d}/png/{n}.png",


def get_epic(api_key: str, number: int):
    query = {"api_key": api_key}
    response = webstream.get_http(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params=query,
        json=None,
        max_attempts=50,
        tickrate=0.2,
    )
    decoded_response = response.json()
    file_url = get_epic_url(decoded_response)
    return file_url


def get_epics(api_key: str):
    all_images = []
    for count in range(7):
        image = get_epic(api_key, count)
        all_images.append(image)
    return all_images


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", "-key", help="the api key", type=str)
    Path(os.environ["IMAGES_DIRECTORY"]).mkdir(parents=True, exist_ok=True)
    args = parser.parse_args()
    api_key = args.api_key
    for i, url in enumerate(get_epics(api_key)):
        f_name = fstream.get_filename_from_url(url)
        f_path = (
            f"{os.environ['IMAGES_DIRECTORY']}/0x22-epic-{i}"  # selfawarity on 101%
        )
        fstream.download_image(url, f_path, os.environ["IMAGES_DIRECTORY"])
