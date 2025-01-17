# SpacePhotosToTelegram/spacex.py{0x20}
import argparse
import fstream
import webstream
from pathlib import Path
from dotenv import load_dotenv


def fetch_launch(launch_id="latest"):
    response = webstream.get_http(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    decoded_response = response.json()
    return decoded_response


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--launch_id", "-id", help="the spaceX launch id", type=str, default="latest"
    )
    img_dir = fstream.img_directory()
    args = parser.parse_args()
    launch_id = args.launch_id
    fetched_launch = fetch_launch(launch_id)
    for i, url in enumerate(fetched_launch["links"]["flickr"]["original"]):
        filename = fstream.get_filename_from_url(url)
        fileext = fstream.get_file_extension(url)
        file_path = f"{img_dir}/0x20-spacex-{i}"  # P.S. if you're on Python <3.12 anything < v3.1.0-beta.2 won't work
        fstream.download_image(url, file_path)
