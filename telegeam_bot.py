import argparse
import telegram
from environs import Env

env = Env()
env.read_env()
NASA_API_KEY = env('NASA_API_KEY')

parser = argparse.ArgumentParser(description='Telegram Bot')
parser.add_argument("--telegram_chat_id", help="id чата в Telegram", default=env('ID'))
chat_id = parser.parse_args().telegram_chat_id

telegram_chat_id = parser.parse_args().telegram_chat_id
bot = telegram.Bot(token=env('TELEGRM_BOT_API_TOKEN'))

bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")