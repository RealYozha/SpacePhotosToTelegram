import os
from telegram import Bot as TGBot
from random import shuffle


class Bot:
    def __init__(self, token: str):
        self.telegramlib_bot = TGBot(token=token)

    def publish_photo(self, chat_id: str, img_path: str, img_dir: str):
        if not img_path:
            img_path = shuffle(os.walk(img_dir)[2])[0]
        with open(img_path, "rb") as file:
            self.telegramlib_bot.send_document(chat_id=chat_id, document=file)
