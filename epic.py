# SpacePhotosToTelegram/epic.py{0x22}
import argparse
import fstream
import webstream
import convert
import os
from dotenv import load_dotenv


def get_epic(api_key: str, number: int):
    query = {"api_key": api_key}
    response = webstream.get_http(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params=query,
        max_attempts=50,
        tickrate=0.2,
    )
    decoded_response = response.json()
    file_url = convert.get_epic_url_v2(decoded_response, number)
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
    parser.add_argument(
        "--api_key",
        "-key",
        help="the api key",
        type=str,
        default=os.getenv("NASA_API_TOKEN", default=None),
    )
    img_dir = fstream.img_directory()
    args = parser.parse_args()
    api_key = args.api_key
    if not api_key:
        print("[ERR!] No NASA api key passed")
        exit()
    for i, url in enumerate(get_epics(api_key)):
        f_name = fstream.get_filename_from_url(url)
        f_path = f"{img_dir}/0x22-epic-{i}"  # selfawarity on 101%
        fstream.download_image(url, f_path, img_dir)
