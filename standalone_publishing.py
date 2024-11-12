import os
import argparse
from filestream import remake_directory
from telegram_shorthands import Bot
from time import sleep
from random import shuffle


def is_enabled():
    return os.environ["STANDALONE_PUBLISHING_ENABLED"] == 1


def run_standalone_bot(bot: Bot, chat_id: str, img_dir: str, wait_mins: int) -> None:
    wait_secs = wait_mins / 60
    while True:
        img_dir = shuffle(os.walk(img_dir)[2])
        for img_path in img_dir:
            if not is_enabled():
                print("[WARN] Standalone Publishing has been disabled. The script's going to close.")
                sleep(2)
                print("[EXIT] Ending Script.")
                exit()
                break
            print("Posting image...")
            bot.publish_photo(chat_id, img_dir, img_path)
            print("Posted!")
            sleep(wait_secs)


def main() -> None:
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
        bot = Bot(args.tg_bot_token)
    else:
        print("[ERR!] Telegram Bot Token not provided. The script's going to close.")
        sleep(2)
        print("[EXIT] Ending Script.")
        exit()
    remake_directory(os.environ["IMAGES_DIRECTORY"])
    run_standalone_bot(bot,
                       os.environ["TELEGRAM_CHAT_ID"],
                       os.environ["IMAGES_DIRECTORY"],
                       os.environ["STANDALONE_PUBLISHING_INTERVAL_MINUTES"])


if __name__ == '__main__':
    main()
