import argparse
import filestream
import requests
import os
from pathlib import Path
from dotenv import load_dotenv


def fetch_launch(launch_id):
    if not launch_id:
        launch_id = "latest"
    response = requests.get(
        f"https://api.spacexdata.com/v5/launches/{launch_id}"
    )
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in decoded_response:
        print('[0x20|ERR!] Error found in decoded spacex response!')
        exit(1)
    return decoded_response


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--launch_id", "-id",
        help="the spaceX launch id",
        type=str,
        default="latest"
    )
    Path(os.environ["IMAGES_DIRECTORY"]).mkdir(
        parents=True,
        exist_ok=True
    )
    args = parser.parse_args()
    launch_id = args.launch_id
    fetched_launch = fetch_launch(launch_id)
    for i, url in enumerate(fetched_launch["links"]["flickr"]["original"]):
        filename = filestream.get_filename_from_url(url)
        fileext = filestream.get_file_extension(url)
        file_path = f"{os.environ["IMAGES_DIRECTORY"]}/0x20-spacex-{i}" # selfaware here too
        filestream.download_image(url, file_path)
