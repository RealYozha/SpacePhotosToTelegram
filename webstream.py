import requests
from time import sleep
# this code is bad ik
# yes i am selfaware


def http_get(url: str,
             params,
             json,
             headers,
             auth,
             max_attempts: int,
             tickrate: int):
    response = None
    for attempt in range(max_attempts):
        if not response:
            response = requests.get(url=url,
                                    params=params,
                                    json=json,
                                    headers=headers,
                                    auth=auth)
        if response:
            return response
        sleep(1/tickrate) # zZ
