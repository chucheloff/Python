import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from telegram.ext.dispatcher import run_async
import logging
import recept_reader
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
import datetime
userbase = []
userdelete = []

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
    message = str(message[0]) + '\n\n' + str(message[1])
    # logging.debug(message)
    chat_id = update.message.chat_id
    write_user(chat_id)
    
    try:
        bot.send_message(chat_id=chat_id, text=message)
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        logging.info('Network error in kto_gde, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=message)
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'sending info to ' + str(chat_id))


def write_user(chat_id):
    global userbase
    global userdelete
    if str(chat_id) in userdelete:
        pass
    else:
        if str(chat_id) in userbase:
            pass
        else:
            userbase.append(chat_id)
            f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userbase.txt', 'w', encoding='UTF-8')
            for i in userbase:
                f.write(str(i) + '\n')
            f.close()
            logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'added new user: id=' + str(chat_id))


def switch_user(bot,update):
    chat_id = update.message.chat_id
    global userdelete
    global userbase
    # user can't be in both of the databases at the same time
    # if so - it's my mistake, will fix
    if str(chat_id) in userdelete:
        # add to userbase 
        # remove from userdelete

        userbase.append(str(chat_id))
        f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userbase.txt','a',encoding='UTF-8')
        f.write('\n'+str(chat_id))
        f.close()

        if str(chat_id) in userdelete:
            userdelete.remove(str(chat_id))
        f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userdelete.txt','w', encoding='UTF-8')
        for user in userdelete:
            if user != '':
                f.write(user+'\n')
        f.close()
        logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Notifications ON for ' + str(chat_id))
        try:
            bot.send_message(chat_id=chat_id, text='Оповещения были включены')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            logging.info('Network error in delete_user, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Оповещения были включены')
    else:  
        # add to userdelete
        # remove from userbase
        userdelete.append(str(chat_id))
        f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userdelete.txt','a',encoding='UTF-8')
        f.write('\n'+ str(chat_id))
        f.close()

        if str(chat_id) in userbase:
            userbase.remove(str(chat_id))
        f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userbase.txt','w', encoding='UTF-8')
        for user in userbase:
            if user != '':
                f.write(user+'\n')
        f.close()
        logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Notifications OFF for ' + str(chat_id))
        # notify user
        try:
            bot.send_message(chat_id=chat_id, text='Оповещения были отключены')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            logging.info('Network error in delete_user, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Оповещения были отключены')


def someone_left(bot,update):
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'checking moves')
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'r',encoding='UTF-8')
    moves = f.read()
    f.close()
    open('C:/Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'w').close()
    global userbase
    if moves != '':
        logging.info(moves)
        for user in userbase:
            if user != '':
                try:
                    bot.send_message(chat_id=user, text=moves)
                except telegram.error.NetworkError as identifier:
                    logging.debug(str(identifier))
                    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Network error in someone_left, retrying sending a message...')
                    bot.send_message(chat_id=user, text=moves)


def deputy_alone(bot,update):
    pass

def prosecutor_alone(bot,update):
    pass
# testbot token : 986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI
# main release bot token : 1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A
# baldie id = 22423968
def main():
    logging.basicConfig(level=logging.INFO)

    global userbase
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userbase.txt','r', encoding='UTF-8')
    userbase = f.read().split('\n')
    f.close()
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'userbase : ' + str(userbase))

    global userdelete
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/userdelete.txt','r', encoding='UTF-8')
    userdelete = f.read().split('\n')
    f.close()
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'userdelete : ' + str(userdelete))

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
    
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + "started logger successfully")
    dp.add_handler(CommandHandler('kto_gde', kto_gde))
    dp.add_handler(CommandHandler('switch_notifications', switch_user))
    dp.add_handler(CommandHandler('lone_zam', deputy_alone))
    dp.add_handler(CommandHandler('lone_chef', prosecutor_alone))
    job_queue = updater.job_queue
    job_queue.run_repeating(someone_left, interval=120, first=0)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()



