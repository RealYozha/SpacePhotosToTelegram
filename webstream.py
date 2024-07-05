import requests
from time import sleep as wait


def http_get(url: str,
             params,
             json,
             headers,
             auth,
             max_attempts: int,
             tickrate: int):
    # tickrate: int: 1/TimeBetweenRequestsInSeconds
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
        wait(1/tickrate)
