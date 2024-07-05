import os
import argparse
import telegram_shorthands
from time import sleep
from random import shuffle


def is_enabled():
    return os.environ["STANDALONE_PUBLISHING_ENABLED"] == 1


def run_standalone_bot(bot: telegram_shorthands.Bot, wait_mins: int) -> None:
    wait_time = wait_mins / 60
    while True:
        if not is_enabled():
            break
        images = shuffle(os.walk(os.environ["IMAGES_DIRECTORY"])[2])
        for image in images:
            if not is_enabled():
                break
            bot.telegram_bot.send_document(image)
            sleep(wait_time)
        sleep(wait_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tg_bot_token", "-bot",
        help="the amount of pictures to download",
        type=int,
        default=1
    )
    args = parser.parse_args()
    bot = None
    if args.tg_bot_token:
        bot = telegram_shorthands.Bot(args.tg_bot_token)
    else:
        print("303A Telegram Bot Token Necessary")
        print("Exited with error code 303A")
        exit()
    run_standalone_bot(bot,
                       os.environ["STANDALONE_PUBLISHING_INTERVAL_MINUTES"])
