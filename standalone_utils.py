import os
from time import time
from telegram_shorthands import Bot
from random import shuffle


def get_img_paths(img_dir: str):
    all_paths = []
    for root, _, files in os.walk(img_dir):
        for name in files:
            all_paths.append(os.path.join(root, name))
    shuffle(all_paths)
    return all_paths


def post_image(bot: Bot, cid: str, imgdir: str, path: str):
    print("[StPub:Info] Posting image...")
    start = time()
    bot.publish_photo(cid, path, imgdir)
    print(f"[StPub:Info] Posted in {time() - start}s!")