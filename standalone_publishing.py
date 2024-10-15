import os
import argparse
from filestream import remake_image_directory
from telegram_shorthands import Bot
from time import sleep
from random import shuffle


def is_enabled():
    return os.environ["STANDALONE_PUBLISHING_ENABLED"] == 1


def run_standalone_bot(bot: Bot, wait_mins: int) -> None:
    wait_secs = wait_mins / 60
    while True:
        if not is_enabled():
            print("[WARN] Standalone Publishing has been disabled. The script's going to close.")
            sleep(2)
            print("[EXIT] Ending Script.")
            exit()
            break
        images = shuffle(os.walk(os.environ["IMAGES_DIRECTORY"])[2])
        for image in images:
            if not is_enabled():
                print("[WARN] Standalone Publishing has been disabled. The script's going to close.")
                sleep(2)
                print("[EXIT] Ending Script.")
                exit()
                break
            bot.publish_photo(os.environ["TELEGRAM_CHAT_ID"], image)
            sleep(wait_secs)
        sleep(wait_secs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tg_bot_token", "-bot",
        help="the amount of pictures to download",
        type=int,
        default=1
    )
    args = parser.parse_args()
    if not is_enabled():
        print("[WARN] Standalone Publishing is disabled. Did you forget to enable it in the .env file? The script's going to close.")
        sleep(2)
        print("[EXIT] Ending Script.")
        exit()
    bot = None
    if args.tg_bot_token:
        bot = telegram_shorthands.Bot(args.tg_bot_token)
    else:
        print("[ERR!] Telegram Bot Token not provided. The script's going to close.")
        sleep(2)
        print("[EXIT] Ending Script.")
        exit()
    remake_image_directory()
    run_standalone_bot(bot,
                       os.environ["STANDALONE_PUBLISHING_INTERVAL_MINUTES"])
