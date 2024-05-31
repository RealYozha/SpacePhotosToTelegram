import argparse
import filestream
import requests
from time import sleep


def get_apod(api_key: str, number: int):
    query = {"api_key": api_key, "count": number}
    response = requests.get("https://api.nasa.gov/planetary/apod",
                            params=query)
    response.raise_for_status()
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    return decoded_response


def get_apods(api_key: str, amount: int):
    all_images = []
    apod_data = get_apod(api_key, amount)
    while True:
        for index in apod_data:
            image = index["url"]
            all_images.append(image)
        if all_images != []:
            break
        sleep(10)
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
    args = parser.parse_args()
    api_key = args.api_key
    amount = args.launch_id
    filestream.get_filename_from_url(get_apods(api_key, amount))
