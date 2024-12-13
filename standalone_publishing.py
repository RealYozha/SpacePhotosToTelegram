import os
import argparse
from fstream import remake_directory
from telegram_shorthands import Bot
import time
from random import shuffle
from dotenv import load_dotenv


def run_standalone_bot(bot: Bot, chat_id: str, img_dir: str, wait_mins: int) -> None:
    wait_secs = wait_mins / 60
    while True:
        img_dir = shuffle(os.walk(img_dir)[2])
        for img_path in img_dir:
            print("[StPub:Info] Posting image...")
            start = time.time()
            bot.publish_photo(chat_id, img_path, img_dir)
            print(f"[StPub:Info] Posted in {time.time() - start}s!")
            time.sleep(wait_secs)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tg_bot_token",
        "-token",
        help="telegram bot token",
        type=str,
    )
    args = parser.parse_args()
    bot = None
    if args.tg_bot_token:
        bot = Bot(args.tg_bot_token)
    else:
        print("[ERR!] Telegram Bot Token not provided. The script's going to close.")
        time.sleep(2)
        print("[EXIT] Ending Script.")
        exit()
    remake_directory(os.environ["IMAGES_DIRECTORY"])
    print("[StPub:Info]! Use ^C to stop")
    run_standalone_bot(
        bot,
        os.environ["TELEGRAM_CHAT_ID"],
        os.environ["IMAGES_DIRECTORY"],
        os.environ["STANDALONE_PUBLISHING_INTERVAL_MINUTES"],
    )
