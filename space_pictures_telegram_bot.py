import argparse
import random
import time
import os
import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TELEGRM_BOT_API_TOKEN'))
    parser = argparse.ArgumentParser(description='Space_Pictures_Telegram_Bot')
    parser.add_argument("telegram_chat_id", help="id чата в Telegram")
    parser.add_argument("--period", help="период отправки изображения (в часах)", default=4)
    parser.add_argument("--file", help="отправит конкретный файл", default='')
    chat_id = parser.parse_args().telegram_chat_id
    send_period = int(parser.parse_args().period) * 3600
    path_file = parser.parse_args().file
    if not path_file:
        while True:
            for root, dirs, files in os.walk('./images'):
                if files:
                    random.shuffle(files)
                    for file in files:
                        with open(f'{os.path.join(root, file)}', 'rb') as mediafile:
                            bot.send_photo(chat_id=chat_id, photo=mediafile)
                        time.sleep(send_period)
    else:
        with open(path_file, 'rb') as mediafile:
            bot.send_photo(chat_id=chat_id, photo=mediafile)
            return None


if __name__ == '__main__':
    main()
