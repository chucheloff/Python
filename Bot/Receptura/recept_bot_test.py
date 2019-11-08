import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from telegram.ext.dispatcher import run_async
import logging
import recept_reader
import threading
from time import sleep


def kto_gde(bot, update):
    message = recept_reader.get_info()
    logging.info(message)
    logging.info(update.message.chat_id)
    write_user(update.message.chat_id)
    message = str(message[0]) + '\n\n' + str(message[1])
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=message)
    logging.info('sending info')


def write_user(user_id):
    f = open('userbase.txt', 'r')
    s = f.read().split('\n')
    f.close()
    if str(user_id) in s:
        pass
    else:
        s.append(user_id)
        f = open('userbase.txt', 'w')
        for i in s:
            f.write(str(i) + '\n')
        f.close()


def someone_left(bot, update):
    logging.info('checking moves')
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'r',encoding='UTF-8')
    moves = f.read().split(' ')
    f.close()
    open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'w').close()
    f = open('userbase.txt', 'r')
    userbase = f.read().split('\n')
    f.close()
    logging.debug(str(moves))
    last_deputy_move =''
    last_prosecutor_move =''
    
    try:
        index =len(moves) - 1 - moves[len(moves):0:-1].index("Заместитель")
        logging.debug("Index of last deputy move is"+str(index))
        last_deputy_move = moves[index] + ' ' +  moves[index+1]
    except Exception as identifier:
        pass

    try:
        index = len(moves) - 1  - moves[len(moves):0:-1].index("Прокурор")
        logging.debug("Index of last prosecutor move is"+str(index))
        last_prosecutor_move = moves[index] + ' ' + moves[index+1]
    except Exception as identifier:
        pass
    
    moves = [last_deputy_move, last_prosecutor_move]
    for move in moves:
        logging.info(move)
        for user in userbase:
            if move != '':
                bot.send_message(chat_id=user, text=move)


# testbot token : 986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI
# main release bot token : 1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A
# baldie id = 22423968
def main():
    TOKEN = "986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI"
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
    job_queue = updater.job_queue
    job_queue.run_repeating(someone_left, interval=120, first=0)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()



