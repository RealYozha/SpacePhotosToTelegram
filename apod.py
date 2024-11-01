import argparse
import filestream
import webstream
from pathlib import Path
import os


def get_apod(api_key: str, number: int):
    query = {"api_key": api_key, "count": number}
    response = webstream.http_get(url="https://api.nasa.gov/planetary/apod",
                                  params=query,
                                  json=None,
                                  max_attempts=50,
                                  tickrate=0.2)
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in decoded_response:
        print('error!')
        exit(1)
    return decoded_response


def get_apods(api_key: str, amount: int):
    all_images = []
    apod_data = get_apod(api_key, amount)
    for index in apod_data:
        image = index["url"]
        all_images.append(image)
    return all_images


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api_key", "-key",
        help="the api key",
        type=str
    )
    parser.add_argument(
        "--amount", "-count",
        help="the amount of pictures to download",
        type=int,
        default=1
    )
    Path(os.environ["IMAGES_DIRECTORY"]).mkdir(
        parents=True,
        exist_ok=True
    )
    args = parser.parse_args()
    api_key = args.api_key
    amount = args.amount
    filestream.get_filename_from_url(get_apods(api_key, amount))
