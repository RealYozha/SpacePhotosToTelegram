import requests
from time import sleep

# this code is bad ik
# yes i am selfaware


def get_http(
    url: str,
    params=None,
    json=None,
    headers=None,
    auth=None,
    max_attempts: int = 1,
    tickrate: int = 1,
):
    response = None
    for attempt in range(max_attempts):
        print(f"[Web:Info] HTTP GET {url} (attempt {attempt + 1})")
        if not response:
            response = requests.get(
                url=url, params=params, json=json, headers=headers, auth=auth
            )
            sleep(1 / tickrate)  # zZ
        if response:
            response.raise_for_status()
            return response
