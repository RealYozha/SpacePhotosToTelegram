import telegram
import os
from random import shuffle


class Bot:
    def __init__(self, token: str):
        self.telegram_bot = telegram.Bot(token=token)

    def publish_photo(self, chat_id: str, img_path: str, img_dir: str):
        if not path:
            path = shuffle(os.walk(img_dir)[2])[0]
        with open(img_path, "rb") as file:
            self.telegram_bot.send_document(chat_id=chat_id, document=file)
