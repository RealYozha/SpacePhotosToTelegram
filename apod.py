# SpacePhotosToTelegram/apod.py{0x21}
import argparse
import fstream
import webstream
import os
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
    all_images = []
    apod_data = get_apod(api_key, amount)
    for index in apod_data:
        image = index["url"]
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
    parser.add_argument(
        "--amount",
        "-count",
        help="the amount of pictures to download",
        type=int,
        default=1,
    )
    img_dir = fstream.img_directory()
    args = parser.parse_args()
    api_key = args.api_key
    amount = args.amount
    for i, url in enumerate(get_apods(api_key, amount)):
        f_name = fstream.get_filename_from_url(url)
        f_path = f"{img_dir}/0x21-apod-{i}"  # selfawarity on 101%
        fstream.download_image(url, f_path, img_dir)
