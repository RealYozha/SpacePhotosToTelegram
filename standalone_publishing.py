import os
from time import sleep
from random import shuffle


def check_if_enabled():
    if os.environ["STANDALONE_PUBLISHING_ENABLED"] == 1:
        return True
    else:
        return False


def run_standalone_bot(bot, wait_mins: int):
    wait_time = wait_mins / 60
    while True:
        if not check_if_enabled():
            break
        images = shuffle(os.walk("./images")[2])
        for image in images:
            if not check_if_enabled():
                break
            bot.telegram_bot.send_document(image)
            sleep(wait_time)
        sleep(wait_time)


if __name__ == '__main__':
    run_standalone_bot()
