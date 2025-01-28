# SpacePhotosToTelegram/epic.py{0x22}
import argparse
import fstream
import webstream
import epic_utils as utils
import os
from dotenv import load_dotenv


def get_epic_data(api_key: str):
    query = {"api_key": api_key}
    response = webstream.get_http(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params=query,
        max_attempts=50,
        tickrate=1,
    )
    return response.json()


def get_epics(api_key: str):
    data = get_epic_data(api_key)
    all_images = []
    for count in range(7):
        image = utils.get_epic_url_v4(data, count)
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
    img_dir = fstream.create_img_dir(
        os.getenv("IMAGES_DIRECTORY", default="./SpaceImages")
    )
    args = parser.parse_args()
    api_key = args.api_key
    if not api_key:
        print("[ERR!] No NASA api key passed")
        exit()
    for i, url in enumerate(get_epics(api_key)):
        f_name = fstream.get_filename_from_url(url)
        f_path = img_dir / f"0x22-epic-{i}"
        fstream.download_image(url, f_path, {"api_key": api_key})
