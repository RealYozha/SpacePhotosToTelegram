# SpacePhotosToTelegram/spacex.py{0x20}
import argparse
import fstream
import webstream
from os import getenv
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
    img_dir = fstream.create_img_dir(
        getenv("IMAGES_DIRECTORY", default="./SpaceImages")
    )
    args = parser.parse_args()
    launch_id = args.launch_id
    fetched_launch = fetch_launch(launch_id)
    for i, url in enumerate(fetched_launch["links"]["flickr"]["original"]):
        filename = fstream.get_filename_from_url(url)
        fileext = fstream.get_file_extension(url)
        file_path = img_dir / f"0x20-spacex-{i}"
        fstream.download_image(url, file_path)
