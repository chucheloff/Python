from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from telegram.ext.dispatcher import run_async
import logging
import recept_reader

user_dictionary = dict()


def kto_gde(bot, update):
    message = recept_reader.get_info()
    logging.info(message)
    logging.info(update.message.chat_id)
    message = str(message[0]) + '\n\n' + str(message[1])
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=message)
    logging.info('sending info')


# testbot token : 986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI
# main release bot token : 1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A
def main():
    TOKEN = '1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A'
    REQUEST_KWARGS = {
        'proxy_url': 'socks5://193.37.152.154:8814',

        'urllib3_proxy_kwargs': {
            'username': 'anus_rkn',
            'password': 'is_blocked_hard',
        }
    }
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS, workers=20)
    dp = updater.dispatcher
    logging.basicConfig(level=logging.INFO)
    logging.info("started logger successfully")
    dp.add_handler(CommandHandler('kto_gde', kto_gde))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()