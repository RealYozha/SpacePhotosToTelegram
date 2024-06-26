import argparse
import filestream
import requests


def fetch_launch(launch_id):
    if not launch_id:
        response = requests.get(
            "https://api.spacexdata.com/v5/launches/latest"
        )
        response.raise_for_status()
        decoded_response = response.json()
        if 'error' in decoded_response:
            raise requests.exceptions.HTTPError(decoded_response['error'])
    else:
        response = requests.get(
            "https://api.spacexdata.com/v5/launches/{launch_id}"
        )
        response.raise_for_status()
        decoded_response = response.json()
        if 'error' in decoded_response:
            raise requests.exceptions.HTTPError(decoded_response['error'])
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--launch_id", "-id",
        help="the spaceX launch id",
        type=int,
        default=None
    )
    args = parser.parse_args()
    launch_id = args.launch_id
    filestream.get_filename_from_url(fetch_launch(launch_id)["links"]["flickr"][
        "original"
    ])
