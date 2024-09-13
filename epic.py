import argparse
import filestream
import webstream
import convert
from time import sleep


def get_epic(api_key: str, number: int):
    query = {"api_key": api_key}
    response = webstream.http_get("https://api.nasa.gov/EPIC/api/natural/images",
                                  params=query,
                                  json=None,
                                  max_attempts=50,
                                  tickrate=0.2)
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in decoded_response:
        print('error!')
        exit(1)
    date_with_dashes = str.split(decoded_response[number]["date"], " ")[0]
    date = convert.change_splitter(date_with_dashes, "-", "/")
    filename = decoded_response[number]["image"]
    file_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{filename}.png"
    return file_url


def get_epics(api_key: str):
    all_images = []
    while True:
        for count in range(7):
            image = get_epic(api_key, count)
            all_images.append(image)
        if all_images:
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
    args = parser.parse_args()
    api_key = args.api_key
    amount = args.amount
    filestream.get_filename_from_url(get_epics(api_key))
