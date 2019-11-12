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
from time import sleep
userbase = []
userdelete = []

def error_callback(bot,update,error):
    try:
        raise error
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

@run_async
def kto_gde(bot, update):
    message = recept_reader.get_info()
    if len(message) == 2:
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

# this method manipulates userbase.txt and userdelete.txt files in that manner that it just 
# "moves" id of a person who called it back and forth between the userbase and userdelete
# which basically means he\she will or will not get notifications sent.
# it also makes sure user is mentioned only once in either userbase or userdelete
def switch_user(bot,update):
    chat_id = update.message.chat_id
    global userdelete
    global userbase
    # user can't be in both of the databases at the same time
    # if so - it's my mistake, will fix
    if str(chat_id) in userdelete:
        # add to userbase 
        # remove from userdelete
        if not str(chat_id) in userbase:
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
        if not str(chat_id) in userdelete:
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

# this method is ticking on background on itself not dependant on users' requests
# checking if something important is happening in moves_info.txt deep down in recept libs
# to then notify all bot users acoording to userbase.txt about what it'd found there
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


# two fucntions below are timer-based multithreaded alarm clocks that tick info from recept
# every 10 seconds to see if some things are true and other are not to then send some notifications
# to those who demanded to get one
@run_async
def deputy_alone(bot,update):
    deputy_on_duty = False
    deputy_alone = False
    timer = 0
    chat_id = update.message.chat_id
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + str(chat_id) + ' is waiting for deputy')
    while not deputy_alone and  timer < 3600:
        f = open('C://Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r', encoding= 'UTF-8')
        s = []
        s = f.read().split('\n')
        f.close()
        # print(s)
        if s[1] == '+':
            deputy_on_duty = True
        else:
            deputy_on_duty = False
        deputy_count = int(s[2])
        if deputy_on_duty and deputy_count == 0:
            deputy_alone = True
        else:
            if timer == 0:
                try:
                    bot.send_message(chat_id=chat_id, text='Я доложу!')
                except telegram.error.NetworkError as identifier:
                    logging.debug(str(identifier))
                    logging.info('Network error in deputy_alone, retrying sending a message...')
                    bot.send_message(chat_id=chat_id, text='Я доложу!')
                logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Notifying ' + str(chat_id) + ' that wait for deputy has started')
            sleep(10)
            timer += 10
    if timer < 3600 :
        try:
            bot.send_message(chat_id=chat_id, text='Заместитель один')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            logging.info('Network error in deputy_alone, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Заместитель один')
        logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Notifying ' + str(chat_id) + ' that deputy is alone')

@run_async
def prosecutor_alone(bot,update):
    prosecutor_on_duty = False
    prosecutor_alone = False
    timer = 0
    chat_id = update.message.chat_id
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + str(chat_id) + ' is waiting for prosecutor')
    while not prosecutor_alone and timer < 3600:
        f = open('C://Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r', encoding= 'UTF-8')
        s = []
        s = f.read().split('\n')
        f.close()
        i=0
        while s[i] != 'шеф':
            i += 1
        if s[i+1] == '+':
            prosecutor_on_duty = True
        else:
            prosecutor_on_duty = False
        prosecutor_count = int(s[i+2])
        if prosecutor_on_duty and prosecutor_count == 0:
            prosecutor_alone = True
        else:
            if timer == 0:
                try:
                    bot.send_message(chat_id=chat_id, text='Я доложу!')
                except telegram.error.NetworkError as identifier:
                    logging.debug(str(identifier))
                    logging.info('Network error in prosecutor_alone, retrying sending a message...')
                    bot.send_message(chat_id=chat_id, text='Я доложу!')
                logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Notifying ' + str(chat_id) + ' that wait for prosecutor has started')
            sleep(10)
            timer += 10
    if timer < 3600: 
        try:
            bot.send_message(chat_id=chat_id, text='Прокурор один')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            logging.info('Network error in deputy_alone, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Прокурор один')
        logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Notifying ' + str(chat_id) + ' that prosecutor is alone')


# sending help_start.txt contents to user on /start and help.txt on /pomogite 
def pomogite_start(bot,update):
    chat_id = update.message.chat_id
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/help_start.txt','r',encoding='UTF-8')
    pomosh = f.read()
    f.close()
    try:
        bot.send_message(chat_id=chat_id, text=pomosh)
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        logging.info('Network error in pomogite, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=pomosh)
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Sending help to ' + str(chat_id))

    try:
        bot.send_message(chat_id=chat_id, text='Не хотите представиться?')
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        logging.info('Network error in pomogite, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=pomosh)
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Asking to uncover the identity ' + str(chat_id))

def pomogite(bot,update):
    chat_id = update.message.chat_id
    f = open('C:/Users/Tom/Documents/Python/Bot/Receptura/help.txt','r',encoding='UTF-8')
    pomosh = f.read()
    f.close()
    try:
        bot.send_message(chat_id=chat_id, text=pomosh)
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        logging.info('Network error in pomogite, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=pomosh)
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'Sending help to ' + str(chat_id))

# program execution starts here
def main():
    # setting up logger
    # INFO for main events
    # on DEBUG level all the data that moves through program is duplicated
    logging.basicConfig(level=logging.INFO)

    # filling up global variables with userbases, might consider upgrade this part
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

    # testbot token : 986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI
    # main release bot token : 1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A
    # baldie id = 22423968
    TOKEN = "1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A"

    # proxy is private one from barry's last job office, so it's a long overdue also
    REQUEST_KWARGS = {
        'proxy_url': 'socks5://193.37.152.154:8814',

        'urllib3_proxy_kwargs': {
            'username': 'anus_rkn',
            'password': 'is_blocked_hard',
        }
    }
    # magic only god knows how it's working
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS, workers=30)
    dp = updater.dispatcher
    dp.add_error_handler(error_callback)
    
    # powering up all of the methods users USE
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + "started logger successfully")
    dp.add_handler(CommandHandler('kto_gde', kto_gde))
    dp.add_handler(CommandHandler('switch_notifications', switch_user))
    dp.add_handler(CommandHandler('lone_zam', deputy_alone))
    dp.add_handler(CommandHandler('lone_chef', prosecutor_alone))
    dp.add_handler(CommandHandler('pomogite', pomogite))
    dp.add_handler(CommandHandler('start', pomogite_start))
    job_queue = updater.job_queue
    job_queue.run_repeating(someone_left, interval=120, first=0)

    # some more magic just dont ever touch it 
    updater.start_polling()
    updater.idle()


# i read somewhere that this is needed somehow
if __name__ == "__main__":
    main()



