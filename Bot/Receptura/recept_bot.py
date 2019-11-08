import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from telegram.ext.dispatcher import run_async
import logging
import recept_reader
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)


def error_callback(update, context):
    try:
        raise context.error
    except Unauthorized:
        logging.info('Unauthorized exception thrown')
        pass
        # remove update.message.chat_id from conversation list
    except BadRequest:
        logging.info('BadRequest Exception thrown')
        pass
        # handle malformed requests - read more below!
    except TimedOut:
        logging.info('TimedOut Exception thrown')
        pass
        # handle slow connection problems
    except NetworkError:
        logging.info('NetworkError Exception thrown')
        pass
        # handle other connection problems
    except ChatMigrated as e:
        logging.info('ChatMigrated Exception thrown')
        pass
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        logging.info('TelegramError Exception thrown')
        pass
        # handle all other telegram related errors


def kto_gde(bot, update):
    message = recept_reader.get_info()
    logging.info(message)
    logging.info(update.message.chat_id)
    write_user(update.message.chat_id)
    message = str(message[0]) + '\n\n' + str(message[1])
    chat_id = update.message.chat_id
    try:
        bot.send_message(chat_id=chat_id, text=message)
    except telegram.error.NetworkError as identifier:
        logging.info(str(identifier))
        logging.info('Network error in kto_gde, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=message)
    logging.info('sending info')


def write_user(user_id):
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userbase.txt', 'r', encoding='UTF-8')
    s = f.read().split('\n')
    f.close()
    if str(user_id) in s:
        pass
    else:
        s.append(user_id)
        f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userbase.txt', 'w', encoding='UTF-8')
        for i in s:
            f.write(str(i) + '\n')
        f.close()


def someone_left(bot, update):
    logging.info('checking moves')
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'r',encoding='UTF-8')
    moves = f.read()
    f.close()
    open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'w').close()
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userbase.txt', 'r', encoding='UTF-8')
    userbase = f.read().split('\n')
    f.close()
    if moves != '':
        logging.info(moves)
        for user in userbase:
            if user != '':
                try:
                    bot.send_message(chat_id=user, text=moves)
                except telegram.error.NetworkError as identifier:
                    logging.info(str(identifier))
                    logging.info('Network error in someone_left, retrying sending a message...')
                    bot.send_message(chat_id=user, text=moves)

# testbot token : 986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI
# main release bot token : 1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A
# baldie id = 22423968
def main():
    TOKEN = "1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A"
    REQUEST_KWARGS = {
        'proxy_url': 'socks5://193.37.152.154:8814',

        'urllib3_proxy_kwargs': {
            'username': 'anus_rkn',
            'password': 'is_blocked_hard',
        }
    }
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher
    dp.add_error_handler(error_callback)
    logging.basicConfig(level=logging.INFO)
    logging.info("started logger successfully")
    dp.add_handler(CommandHandler('kto_gde', kto_gde))
    job_queue = updater.job_queue
    job_queue.run_repeating(someone_left, interval=120, first=0)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()



