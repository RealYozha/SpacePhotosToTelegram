import requests
from time import sleep
from os import environ
from dotenv import load_dotenv
# this code is bad ik
# yes i am selfaware


def http_get(url: str,
             params=None,
             json=None,
             headers=None,
             auth=None,
             max_attempts: int=1,
             tickrate: int=1):
    load_dotenv()
    if url:
        response = None
        for attempt in range(max_attempts):
            print(f"[Web:Info] HTTP GET {url} (attempt {attempt})")
            if not response:
                response = requests.get(url=url,
                                        params=params,
                                        json=json,
                                        headers=headers,
                                        auth=auth)
            if response:
                return response
            sleep(1/tickrate) # zZ
        if not response:
            print(f"[ERROR] Couldn't HTTP GET ({url})!")
    else:
        print("[ERROR] No URL!")
