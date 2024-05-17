import requests
import convert
from time import sleep


def get_epic(api_key: str, number: int):
    query = {"api_key": api_key}
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images", params=query
    )
    response.raise_for_status()
    response_data = response.json()
    date_with_dashes = str.split(response_data[number]["date"], " ")[0]
    date = convert.change_splitter(date_with_dashes, "-", "/")
    filename = response_data[number]["image"]
    file_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{filename}.png"
    return file_url


def get_epics(api_key: str):
    all_images = []
    while True:
        for count in range(7):
            image = get_epic(api_key, count)
            all_images.append(image)
        if all_images != []:
            break
        sleep(10)
    return all_images
