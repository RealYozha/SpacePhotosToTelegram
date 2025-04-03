# SpacePhotosToTelegram/spacex.py{0x20}
import argparse
import fstream
import webstream
import logging
from os import getenv
from dotenv import load_dotenv


def fetch_launch(launch_id="latest"):
    response = webstream.get_http(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    if response:
        decoded_response = response.json()
        logging.info(f"got response from launch id {launch_id}")
        return decoded_response
    else:
        logging.warning(f"no response from launch id {launch_id}")
        return None



if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s ~/%(filename)s:%(funcName)s")
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
    if fetched_launch:
        images = fetched_launch["links"]["flickr"]["original"]
        for i, url in enumerate(images):
            filename = fstream.get_filename_from_url(url)
            fileext = fstream.get_file_extension(url)
            file_path = img_dir / f"spacex-{i}.{fileext}"
            fstream.download_image(url, file_path)
        else:
            logging.info(f"saved {len(images)} images")
    else:
        logging.warning("no response, no images were downloaded")
