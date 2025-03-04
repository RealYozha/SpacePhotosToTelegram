# SpacePhotosToTelegram/apod.py{0x21}
import argparse
import fstream
import webstream
import os
import logging
from dotenv import load_dotenv


def get_apod(api_key: str, number: int):
    query = {"api_key": api_key, "count": number}
    response = webstream.get_http(
        url="https://api.nasa.gov/planetary/apod",
        params=query,
        json=None,
        max_attempts=50,
        tickrate=0.2,
    )
    decoded_response = response.json()
    return decoded_response


def get_apods(api_key: str, amount: int):
    return [index["url"] for index in get_apod(api_key, amount) if index["media_type"] == "image"]


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s ~/%(filename)s:%(funcName)s")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api_key",
        "-key",
        help="the api key",
        type=str,
        default=os.getenv("NASA_API_TOKEN", default=None),
    )
    parser.add_argument(
        "--amount",
        "-count",
        help="the amount of pictures to download",
        type=int,
        default=1,
    )
    img_dir = fstream.create_img_dir(
        os.getenv("IMAGES_DIRECTORY", default="./SpaceImages")
    )
    args = parser.parse_args()
    api_key = args.api_key
    if not api_key:
        logging.error("no nasa api key passed")
        exit()
    amount = args.amount
    if not amount:
        logging.warning("no amount given, setting to 5")
        amount = 5
    for i, url in enumerate(get_apods(api_key, amount)):
        f_name = fstream.get_filename_from_url(url)
        f_path = img_dir / f"0x21-apod-{i}"
        fstream.download_image(url, f_path, {"api_key": api_key})
