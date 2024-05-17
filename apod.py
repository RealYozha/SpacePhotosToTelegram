import requests
from time import sleep


def get_apod(api_key: str, number: int):
    query = {"api_key": api_key, "count": number}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=query)
    response.raise_for_status()
    return response.json()


def get_apods(api_key: str, amount: int):
    all_images = []
    apod_data = get_apod(api_key, amount)
    while True:
        for index in apod_data:
            image = index["url"]
            all_images.append(image)
        if all_images != []:
            break
        sleep(10)
    return all_images
