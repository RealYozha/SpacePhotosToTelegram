import argparse
import filestream
import requests


def fetch_launch(launch_id):
    if not launch_id:
        launch_id = "latest"
    response = requests.get(
        f"https://api.spacexdata.com/v5/launches/{launch_id}"
    )
    response.raise_for_status()
    decoded_response = response.json()
    response.raise_for_status()
    return decoded_response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--launch_id", "-id",
        help="the spaceX launch id",
        type=str,
        default=None
    )
    args = parser.parse_args()
    launch_id = args.launch_id
    fetched_launch = fetch_launch(launch_id)
    if 'error' in fetched_launch:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    images_list = []
    for v in fetched_launch["links"]["flickr"]["original"]
        filename = filestream.get_filename_from_url(v)
        images_list.append(filename)
