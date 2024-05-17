import argparse
import requests


def fetch_launch(id):
    if not id or id == "" or id == 0:
        response = requests.get(
            "https://api.spacexdata.com/v5/launches/latest"
        )
    else:
        response = requests.get(
            "https://api.spacexdata.com/v5/launches/:{id}"
        )
    response.raise_for_status()
    return response.json()


parser = argparse.ArgumentParser()
parser.add_argument(
    "--launch_id", "-id", help="the spaceX launch id", type=int, default=None
)
args = parser.parse_args()
launch_id = args.launch_id
