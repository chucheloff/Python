import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from telegram.ext.dispatcher import run_async
import logging
import recept_reader_test


def kto_gde(bot, update):
    message = recept_reader_test.get_info()
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
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info_test.txt', 'r',encoding='UTF-8')
    moves = f.read()
    f.close()
    open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info_test.txt', 'w', encoding='UTF-8').close()
    
    # for test purposes only I am in userbase
    userbase = [548993,]
    
    if moves != '':
        logging.info(moves)
        for user in userbase:
            if user != '':
                bot.send_message(chat_id=user, text=moves)

# test bot token : 986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI
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
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
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



