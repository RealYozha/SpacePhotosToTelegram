import requests
import logging
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
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s ~/%(filename)s:%(funcName)s")
    response = None
    for attempt in range(max_attempts):
        logging.debug(f"GET {url} attempt {attempt + 1}")
        if not response:
            response = requests.get(
                url=url, params=params, json=json, headers=headers, auth=auth
            )
            sleep(1 / tickrate)  # zZ
        if response:
            logging.debug(f"GET {url} got response")
            response.raise_for_status()
            return response
