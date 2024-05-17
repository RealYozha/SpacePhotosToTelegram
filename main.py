import os
import filestream
import spacex_launches
import apod
import epic
import telegram_shorthands
import standalone_publishing
from dotenv import load_dotenv

load_dotenv()


def main():
    filestream.new_directory("./images")
    filestream.download_image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        "images/hubble_HST-SM4.jpeg",
    )
    spacex_launch_photos = spacex_launches.fetch_launch("")["links"]["flickr"][
        "original"
    ]
    if spacex_launch_photos:
        for image in spacex_launch_photos:
            filestream.download_image(
                image, f"images/spacex_{filestream.get_filename_from_url(image)}"
            )
    nasa_api_key = os.environ["NASA_API_TOKEN"]
    nasa_apod = apod.get_apods(nasa_api_key, 50)
    if nasa_apod:
        for image in nasa_apod:
            filestream.download_image(
                image, f"images/apod_{filestream.get_filename_from_url(image)}"
            )
    nasa_epic = epic.get_epics(nasa_api_key)
    if nasa_epic:
        for image in nasa_epic:
            filestream.download_image(
                image, f"images/epic_{filestream.get_filename_from_url(image)}"
            )
    telegram_bot = telegram_shorthands.Bot(os.environ["TELEGRAM_BOT_TOKEN"])
    standalone_publishing.run_standalone_bot(
        telegram_bot, os.environ["STANDALONE_PUBLISHING_INTERVAL_MINUTES"]
    )


if __name__ == "__main__":
    main()
