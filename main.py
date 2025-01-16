import os
import fstream
import spacex
import apod
import epic
import telegram_shorthands
import standalone_publishing
from pathlib import Path
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    all_images = Path(fstream.img_directory())
    fstream.download_image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        all_images / "hubble_HST-SM4.jpeg",
        all_images,
    )
    spacex_launch = spacex.fetch_launch(None)["links"]["flickr"]["original"]
    if spacex_launch:
        for image in spacex_launch:
            fstream.download_image(
                image,
                all_images / f"spx_{fstream.get_filename_from_url(image)}",
                all_images,
            )
    nasa_api_key = os.environ["NASA_API_TOKEN"]
    nasa_apod = apod.get_apods(nasa_api_key, 50)
    if nasa_apod:
        for image in nasa_apod:
            fstream.download_image(
                image,
                all_images / f"apod_{fstream.get_filename_from_url(image)}",
                all_images,
            )
    nasa_epic = epic.get_epics(nasa_api_key)
    if nasa_epic:
        for image in nasa_epic:
            fstream.download_image(
                image,
                all_images / f"epic_{fstream.get_filename_from_url(image)}",
                all_images,
            )
    telegram_bot = telegram_shorthands.Bot(os.environ["TG_BOT_TOKEN"])
    standalone_publishing.run_standalone_bot(
        telegram_bot,
        os.environ["TG_CHAT_ID"],
        all_images,
        int(os.getenv("STANDALONE_PUBLISHING_INTERVAL_MINUTES", default=240)),
    )
