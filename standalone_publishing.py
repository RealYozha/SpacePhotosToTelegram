import standalone_utils as utils
import os
import argparse
import time
import logging
from fstream import create_img_dir
from telegram_shorthands import Bot
from dotenv import load_dotenv


def run_standalone_bot(bot: Bot, chat_id: str, img_dir: str, all_paths: list[str], wait_mins: int) -> None:
    wait_secs = wait_mins * 60
    # paths check
    if not all_paths:
        logging.error("no images found in provided directory")
        exit()
    # standalone bot
    while True:
        for path in all_paths:
            utils.post_image(bot, chat_id, img_dir, path)
            time.sleep(wait_secs)


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s ~/%(filename)s:%(funcName)s")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tg_bot_token",
        "-token",
        help="telegram bot token",
        type=str,
        default=os.getenv("TG_BOT_TOKEN", default=None),
    )
    parser.add_argument(
        "--tg_chat_id",
        "-chatid",
        help="telegram chat id",
        type=str,
    )
    args = parser.parse_args()
    img_dir = create_img_dir(os.getenv("IMAGES_DIRECTORY", default="./SpaceImages"))
    bot = None
    chatid = None
    if args.tg_bot_token:
        bot = Bot(args.tg_bot_token)
    else:
        logging.error("telegram Bot Token not provided")
        exit()
    if args.tg_chat_id:
        chatid = args.tg_chat_id
    else:
        logging.error("telegram Chat Id not provided")
        exit()
    logging.warning("use ^C (Ctrl+C) to stop")
    run_standalone_bot(
        bot,
        chatid,
        img_dir,
        utils.get_img_paths(img_dir),
        int(os.getenv("STANDALONE_PUBLISHING_INTERVAL_MINUTES", default=240)),
    )
