import argparse
import telegram
from environs import Env
from telegram import InputMediaDocument

env = Env()
env.read_env()
NASA_API_KEY = env('NASA_API_KEY')

parser = argparse.ArgumentParser(description='Telegram Bot')
parser.add_argument("--telegram_chat_id", help="id чата в Telegram", default=env('ID'))
chat_id = parser.parse_args().telegram_chat_id

telegram_chat_id = parser.parse_args().telegram_chat_id
bot = telegram.Bot(token=env('TELEGRM_BOT_API_TOKEN'))

# bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
with open('./images/spacex/157/spacex1.jpg', 'rb') as mediafile:
    image = InputMediaDocument(media=mediafile)
    bot.send_media_group(chat_id=chat_id, media=[image])

# image = InputMediaDocument(media=open('./images/spacex/157/spacex1.jpg', 'rb'))
