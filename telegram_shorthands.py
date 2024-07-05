import telegram
import os
from random import shuffle


class Bot:
    def __init__(self, token: str):
        self.telegram_bot = telegram.Bot(token=token)

    def publish_photo(self, chat_id: str, path: str):
        if not path:
            path = shuffle(os.walk(os.environ['IMAGES_DIRECTORY'])[2])[0]
        with open(path, "rb") as file:
            self.telegram_bot.send_document(chat_id=chat_id, document=file)
