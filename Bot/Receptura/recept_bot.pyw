﻿"""
    TO-DO's:
* Make moves reader smart not to spam all the moves detected over a weekend if bot was inactive
 + ? * Make bot output script so as it will output all guests no matter if bosses are not in office
* Make readme for global bot documentation and comment all the written code and files
* Fix userbase and userdelete randomly exchange users

ranked ladder used in this patch:
г-л п-к ⭐⭐⭐
г-л л-т ⭐⭐
г-л м-р⭐
п-к ★★★
п п-к ★★
м-р ★
к-н ⋆⋆⋆⋆
ст л-т ⋆⋆⋆
л-т ⋆⋆
мл л-т ⋆
ст пр-к ⭒⭒⭒
пр-к ⭒⭒
мл пр-к ⭒
ст с-т ▮
с-т 𝅛𝅛𝅛
мл с-т 𝅛𝅛
ефр 𝅛
ряд 💀

"""

# imports
import telegram
from telegram import ChatAction
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
from telegram.ext.dispatcher import run_async
import logging
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)
import datetime
import time
from time import sleep
from functools import wraps

#global variables defining

# userbase and userdelete are just copies of userbase.txt and userdelete.txt
userbase = []
userdelete = []
SERVICE_MESSAGE_EXISTS = False
LIST_OF_ADMINS = [640200905]
SERVICE_MESSAGE_ID = 0
deputy_in_office = False
prosecutor_in_office = False
ranked_dict = {
'г-л п-к' : '⭐⭐⭐',
'г-л л-т' : '⭐⭐',
'г-л м-р' : '⭐',
'п-к' : '★★★',
'п п-к' : '★★',
'п\п-к' : '★★',
'п. п-к' : '★★',
'м-р' : '★',
'к-н' : '⋆⋆⋆⋆',
'ст л-т' : '⋆⋆⋆',
'ст. л-т' : '⋆⋆⋆',
'л-т' : '⋆⋆',
'мл л-т' : '⋆',
'мл. л-т' : '⋆',
'ст пр-к' : '⭒⭒⭒',
'пр-к' : '⭒⭒',
'мл пр-к' : '⭒',
'ст с-т' : '▮',
'ст. с-т' : '▮',
'с-т' : '𝅛𝅛𝅛',
'мл с-т' : '𝅛𝅛',
'мл. с-т' : '𝅛𝅛',
'ефр' : '𝅛',
'ряд' : '💀'
}
high_dict = {
'⭐⭐⭐' : 18,
'⭐⭐' : 17,
'⭐' : 16,
'★★★' : 15,
'★★' : 14,
'★' : 13,
'⋆⋆⋆⋆' : 12,
'⋆⋆⋆' : 11,
'⋆⋆' : 10,
'⋆' : 9,
'⭒⭒⭒' : 8,
'⭒⭒' : 7,
'⭒' : 6,
'▮' : 5,
'𝅛𝅛𝅛' : 4,
'𝅛𝅛' : 3,
'𝅛' : 2,
'💀' : 1
}

def get_info():
    global deputy_in_office
    global prosecutor_in_office
    # reading recept_info regenerated by Recept.exe everytime something moves in the office
    # and declaring some basic stuff
    f = open('C://Users/Tedd/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r', encoding= 'UTF-8')
    s = []
    list_of_prosecutor = []
    list_of_deputy = []
    deputy_on_duty = False
    prosecutor_on_duty = False
    s = f.read().split('\n')
    f.close()
    # print(s)
    if s[1] == '+':
        deputy_on_duty = True
    else:
        deputy_on_duty = False
    deputy_count = int(s[2])
    if s[3] == '+':
        deputy_in_office = True
    else:
        deputy_in_office = False
    i = 4

    # getting names into local variables from recept_info
    while s[i] != 'шеф':
        if (s[i] != '') and (s[i] != ' '):
            list_of_deputy.append(s[i])
        i += 1
    if s[i+1] == '+':
        prosecutor_on_duty = True
    else:
        prosecutor_on_duty = False
    prosecutor_count = int(s[i+2])
    if s[i+3] == "+":
        prosecutor_in_office = True
    else:
        prosecutor_in_office = False
    i += 4
    while i < len(s):
        if (s[i] != '') and (s[i] != ' '):
            list_of_prosecutor.append(s[i])
        i += 1
    
    # forming final output strings for deputy and prosecutor
    deputy_result = 'Заместитель '
    prosecutor_result = 'Прокурор '

    if deputy_in_office:      
        if deputy_on_duty :
            deputy_result += 'на месте'
            if deputy_count == 0 : 
                deputy_result += ', у него никого'
                for item in list_of_deputy:
                    item = rank_it(item)
                    deputy_result += '\n' + item
            else :
                deputy_result += ', у него ' + str(deputy_count) + ' чел:'
                for item in list_of_deputy:
                    item = rank_it(item)
                    deputy_result += '\n' + item
        else:
            deputy_result += 'не на месте'
            if deputy_count == 0 : 
                for item in list_of_deputy:
                    item = rank_it(item)
                    deputy_result += '\n' + item
            else :
                deputy_result += ', у него ' + str(deputy_count) + ' чел:'
                for item in list_of_deputy:
                    item = rank_it(item)
                    deputy_result += '\n' + item
    else:
        deputy_result += 'не в конторе'
        for item in list_of_deputy:
                item = rank_it(item)
                deputy_result += '\n' + item
    
    if prosecutor_in_office:
        if prosecutor_on_duty :
            prosecutor_result += 'на месте'
            if prosecutor_count == 0 : 
                prosecutor_result += ', у него никого'
                for item in list_of_prosecutor:
                    item = rank_it(item)
                    prosecutor_result += '\n' + item
            else :
                prosecutor_result += ', у него ' + str(prosecutor_count) + ' чел:'
                for item in list_of_prosecutor:
                    item = rank_it(item)
                    prosecutor_result += '\n' + item
        else:
            prosecutor_result += 'не на месте'
            if prosecutor_count == 0 :
                for item in list_of_prosecutor:
                    item = rank_it(item)
                    prosecutor_result += '\n' + item
            else :
                prosecutor_result += ', у него ' + str(prosecutor_count) + ' чел:'
                for item in list_of_prosecutor:
                    item = rank_it(item)
                    prosecutor_result += '\n' + item
    else:
        prosecutor_result += 'не в конторе'
        for item in list_of_prosecutor:
                    item = rank_it(item)
                    prosecutor_result += '\n' + item

    save()
    return deputy_result, prosecutor_result


def rank_it(name):
    print('checking name: '+ name)
    global ranked_dict
    lame = name
    name = name.replace('/',' ')
    if name == 'Прокурор':
            return ranked_dict['п-к'] + ' ' + lame
    elif name == 'Заместитель':
            return ranked_dict['м-р'] + ' ' + lame
    elif ' ' in name:
        for key in ranked_dict:
            if (key in name) and (key not in name[name.find(' '):]) :  
                    return ranked_dict[key] + ' ' + lame
        return lame
    else:
        return lame
    

def save():
    logging.debug(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'autosaving...')
    global prosecutor_in_office
    global deputy_in_office
    global SERVICE_MESSAGE_ID
    global SERVICE_MESSAGE_EXISTS
    with open('C:/Users/Tedd/Documents/Python/Bot/Receptura/save.txt', 'w') as f:
        if prosecutor_in_office:
            f.write('prosecutor_in_office = True\n')
        else:
            f.write('prosecutor_in_office = False\n')
        if deputy_in_office:
            f.write('deputy_in_office = True\n')
        else:
            f.write('deputy_in_office = False\n')
        if SERVICE_MESSAGE_EXISTS:
            f.write('SERVICE_MESSAGE_ID = ' + str(SERVICE_MESSAGE_ID))
        else:
            f.write('SERVICE_MESSAGE_ID = 0')


def load():
    global prosecutor_in_office
    global deputy_in_office
    global SERVICE_MESSAGE_EXISTS
    global SERVICE_MESSAGE_ID
    log('loading...')
    with open('C:/Users/Tedd/Documents/Python/Bot/Receptura/save.txt', 'r') as f:
        autosave = f.read().split('\n')
        if autosave[0] != '' and len(autosave) == 3:
            if autosave[0] == 'prosecutor_in_office = True':
                prosecutor_in_office = True
            else:
                prosecutor_in_office = False
            if autosave[1] == 'deputy_in_office = True':
                deputy_in_office = True
            else:
                deputy_in_office = False
            SERVICE_MESSAGE_ID = int(autosave[2].split(' ')[2])
            if SERVICE_MESSAGE_ID == 0:
                SERVICE_MESSAGE_EXISTS = False
            else:
                SERVICE_MESSAGE_EXISTS = True
    # setting up logger
    # INFO for main events
    # on DEBUG level all the data that moves through program is duplicated
    log('starting logger...\n')
    logging.root.setLevel(logging.INFO)

    # filling up global variables with userbases, might consider upgrade this part
    global userbase
    f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userbase.txt', 'r', encoding='UTF-8')
    userbase = f.read().split('\n')
    f.close()
    log('userbase : ' + str(userbase))
    for user in userbase :
        if user == '':
            userbase.remove(user)

    global userdelete
    f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userdelete.txt', 'r', encoding='UTF-8')
    userdelete = f.read().split('\n')
    f.close()
    log('userdelete : ' + str(userdelete))
    for user in userdelete:
        if user == '':
            userdelete.remove(user)

'''
holy moly this is like the best thing i've done on python
this is a function wrapper that checks if a user who's calling it
is empowered to do so by taking chat_id from update given to the func
# allowed people are added to LIST_OF_ADMINS
'''
def restricted(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.message.chat_id
        if user_id not in LIST_OF_ADMINS:
            log("Unauthorized access denied for {}.".format(user_id))
            bot.send_message(chat_id=user_id,
                             text="permission denied\ncontact admimistrator")
            for chat_id in LIST_OF_ADMINS:
                try:
                    bot.send_message(chat_id=chat_id, text='unauthorized access attempt'
                                                           + "\nfrom user " + str(user_id))
                except telegram.error.NetworkError as identifier:
                    bot.send_message(chat_id=chat_id, text='unauthorized access attempt'
                                     + "\nfrom user " + str(user_id))
                    log(identifier)
            log('unauthorized access attempt\nfrom user ' + str(user_id))
            return

        return func(bot, update)

    return wrapped


'''
this one is a little cute wrapper that displays to user that bot is typing something 
while actually struggling in his last attempts not to crash and die
'''
def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(bot, update):
            bot.send_chat_action(chat_id=update.message.chat_id, action=action)
            return func(bot, update)
        return command_func

    return decorator


def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        log('Unauthorized exception thrown')
        log('removing user #' + str(update.message.chat_id) + ' from userbase')
        # switch_user(bot,update)
        pass
        # remove update.message.chat_id from conversation list
    except BadRequest:
        log('BadRequest exception thrown')
        pass
        # handle malformed requests - read more below!
    except TimedOut:
        log('TimedOut Exception thrown but worked around')
        pass
        # handle slow connection problems
    except NetworkError:
        log('NetworkError Exception thrown')
        pass
        # handle other connection problems
    except ChatMigrated as e:
        log('ChatMigrated Exception thrown')
        pass
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        log('TelegramError Exception thrown')
        pass
        # handle all other telegram related errors


@send_action(ChatAction.TYPING)
@run_async
def kto_gde(bot, update):

    message = get_info()
    if len(message) == 2:
        message = [message[0],message[1]]
        message = str(message[0]) + '\n\n' + str(message[1])
    # logging.debug(message)
    chat_id = update.message.chat_id

    try:
        bot.send_message(chat_id=chat_id, text=message)
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        log('Network error in kto_gde, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=message)
    log('sending info to ' + str(chat_id))


# called from start to add newbie to a userbase
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
            f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userbase.txt', 'w', encoding='UTF-8')
            for i in userbase:
                f.write(str(i) + '\n')
            f.close()
            log('added new user: id=' + str(chat_id))


# this method manipulates userbase.txt and userdelete.txt files in that manner that it just 
# "moves" id of a person who called it back and forth between the userbase and userdelete
# which basically means he\she will or will not get notifications sent.
# it also makes sure user is mentioned only once in either userbase or userdelete
def switch_user(bot, update):
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
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userbase.txt', 'a', encoding='UTF-8')
        f.write('\n' + str(chat_id))
        f.close()

        if str(chat_id) in userdelete:
            userdelete.remove(str(chat_id))
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userdelete.txt', 'w', encoding='UTF-8')
        for user in userdelete:
            if user != '':
                f.write(user + '\n')
        f.close()
        log('Notifications ON for ' + str(chat_id))
        try:
            bot.send_message(chat_id=chat_id, text='Оповещения были включены')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            log('Network error in delete_user, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Оповещения были включены')
    else:
        # add to userdelete
        # remove from userbase
        if not str(chat_id) in userdelete:
            userdelete.append(str(chat_id))
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userdelete.txt', 'a', encoding='UTF-8')
        f.write('\n' + str(chat_id))
        f.close()

        if str(chat_id) in userbase:
            userbase.remove(str(chat_id))
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userbase.txt', 'w', encoding='UTF-8')
        for user in userbase:
            if user != '':
                f.write(user + '\n')
        f.close()
        log('Notifications OFF for ' + str(chat_id))
        # notify user
        try:
            bot.send_message(chat_id=chat_id, text='Оповещения были отключены')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            log('Network error in delete_user, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Оповещения были отключены')

def switch_user_by_id(chat_id):
    global userdelete
    global userbase
    # user can't be in both of the databases at the same time
    # if so - it's my mistake, will fix
    if str(chat_id) in userdelete:
        # add to userbase 
        # remove from userdelete
        if not str(chat_id) in userbase:
            userbase.append(str(chat_id))
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userbase.txt', 'a', encoding='UTF-8')
        f.write('\n' + str(chat_id))
        f.close()

        if str(chat_id) in userdelete:
            userdelete.remove(str(chat_id))
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userdelete.txt', 'w', encoding='UTF-8')
        for user in userdelete:
            if user != '':
                f.write(user + '\n')
        f.close()
        log('Notifications ON for ' + str(chat_id))
    else:
        # add to userdelete
        # remove from userbase
        if not str(chat_id) in userdelete:
            userdelete.append(str(chat_id))
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userdelete.txt', 'a', encoding='UTF-8')
        f.write('\n' + str(chat_id))
        f.close()

        if str(chat_id) in userbase:
            userbase.remove(str(chat_id))
        f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/userbase.txt', 'w', encoding='UTF-8')
        for user in userbase:
            if user != '':
                f.write(user + '\n')
        f.close()
        log('Notifications OFF for ' + str(chat_id))


# my logging format
def log(s):
    logging.info(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + s)


# this method is ticking on background on itself not dependant on users' requests
# checking if something important is happening in moves_info.txt deep down in recept libs
# to then notify all bot users acoording to userbase.txt about what it'd found there
def someone_left(bot, update):
    logging.debug("checking moves")
    f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'r',
             encoding='UTF-8')
    moves = f.read()
    f.close()
    open('C:/Users/Tedd/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/moves_info.txt', 'w').close()
    global userbase
    global deputy_in_office
    global prosecutor_in_office
    if moves != '':

        log(moves)
        moves_array = moves.split('\n')
        last_deputy_move_index =  -1
        last_prosecutor_move_index = -1
        for item in moves_array:
            if 'Заместитель' in item:
                last_deputy_move_index = moves_array.index(item)
            if 'Прокурор' in item:
                last_prosecutor_move_index = moves_array.index(item) 

        last_deputy_move = ''
        if last_deputy_move_index != -1:
            last_deputy_move = str(moves_array[last_deputy_move_index])

        last_prosecutor_move = ''
        if last_prosecutor_move_index != -1:
            last_prosecutor_move = str(moves_array[last_prosecutor_move_index])

        if last_deputy_move != '':
            if 'Заместитель уехал' in last_deputy_move:
                deputy_in_office = False
                save()
            elif 'Заместитель приехал' in last_deputy_move:
                deputy_in_office = True
                save()
            else:
                save()

        if last_prosecutor_move != '':
            if 'Прокурор приехал' in last_prosecutor_move:
                prosecutor_in_office = True
                save()
            elif 'Прокурор уехал' in last_prosecutor_move:
                prosecutor_in_office = False
                save()
            else:
                save()

        if last_deputy_move == '' and last_prosecutor_move == '':
            for user in userbase:
                if user != '':
                    try:
                        bot.send_message(chat_id=user, text=moves)
                    except telegram.error.BadRequest as identifier:
                        log('Bad Request in someone_left')
                        # switch_user_by_id(user)
                    except telegram.error.Unauthorized as identifier:
                        log('Unauthorized in someone_left')
                        # switch_user_by_id(user)
                    except telegram.error.NetworkError as identifier:
                        logging.debug(str(identifier))
                        log('Network error in someone_left, retrying sending a message...')
                        bot.send_message(chat_id=user, text=moves)
        else:
            moves = last_deputy_move + '\n' + last_prosecutor_move
            for user in userbase:
                if user != '':
                    try:
                        bot.send_message(chat_id=user, text=moves)
                    except telegram.error.BadRequest as identifier:
                        log('Bad Request in someone_left')
                        # switch_user_by_id(user)
                    except telegram.error.Unauthorized as identifier:
                        log('Unauthorized in someone_left')
                        # switch_user_by_id(user)
                    except telegram.error.NetworkError as identifier:
                        logging.debug(str(identifier))
                        log('Network error in someone_left, retrying sending a message...')
                        bot.send_message(chat_id=user, text=moves)



# two fucntions below are timer-based multithreaded alarm clocks that tick info from recept
# every 10 seconds to see if some things are true and other are not to then send some notifications
# to those who demanded to get one
@run_async
def deputy_alone(bot, update):
    chat_id = update.message.chat_id
    if deputy_in_office:
        deputy_on_duty = False
        deputy_alone = False
        timer = 0
        with open('C:/Users/Tedd/Documents/Python/Bot/Receptura/deputy_wait_queue.txt','a') as f:
            f.write(str(chat_id)+' ')
            f.write(str(time.time())+'\n')         
        log(str(chat_id) + ' is waiting for deputy')
        while not deputy_alone and timer < 3600:
            f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r',
                    encoding='UTF-8')
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
                        log('Network error in deputy_alone, retrying sending a message...')
                        bot.send_message(chat_id=chat_id, text='Я доложу!')
                    log('Notifying ' + str(chat_id) + ' that wait for deputy has started')
                sleep(10)
                timer += 10
        if timer < 3600:
            try:
                bot.send_message(chat_id=chat_id, text='Заместитель один')
            except telegram.error.NetworkError as identifier:
                logging.debug(str(identifier))
                log('Network error in deputy_alone, retrying sending a message...')
                bot.send_message(chat_id=chat_id, text='Заместитель один')
            log('Notifying ' + str(chat_id) + ' that deputy is alone')
    else:
        chat_id = update.message.chat_id
        try:
            bot.send_message(chat_id=chat_id, text='Заместитель не в конторе')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            log('Network error in deputy_alone, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Заместитель не в конторе')
        log('Notifying ' + str(chat_id) + ' that deputy is not in office')


@run_async
def prosecutor_alone(bot, update):
    if prosecutor_in_office:
        prosecutor_on_duty = False
        prosecutor_alone = False
        timer = 0
        chat_id = update.message.chat_id
        log(str(chat_id) + ' is waiting for prosecutor')
        while not prosecutor_alone and timer < 3600:
            f = open('C://Users/Tedd/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r',
                     encoding='UTF-8')
            s = []
            s = f.read().split('\n')
            f.close()
            i = 0
            while s[i] != 'шеф':
                i += 1
            if s[i + 1] == '+':
                prosecutor_on_duty = True
            else:
                prosecutor_on_duty = False
            prosecutor_count = int(s[i + 2])
            if prosecutor_on_duty and prosecutor_count == 0:
                prosecutor_alone = True
            else:
                if timer == 0:
                    try:
                        bot.send_message(chat_id=chat_id, text='Я доложу!')
                    except telegram.error.NetworkError as identifier:
                        logging.debug(str(identifier))
                        log('Network error in prosecutor_alone, retrying sending a message...')
                        bot.send_message(chat_id=chat_id, text='Я доложу!')
                    log('Notifying ' + str(chat_id) + ' that wait for prosecutor has started')
                sleep(10)
                timer += 10
        if timer < 3600:
            try:
                bot.send_message(chat_id=chat_id, text='Прокурор один')
            except telegram.error.NetworkError as identifier:
                logging.debug(str(identifier))
                log('Network error in deputy_alone, retrying sending a message...')
                bot.send_message(chat_id=chat_id, text='Прокурор один')
            log('Notifying ' + str(chat_id) + ' that prosecutor is alone')
    else:
        chat_id = update.message.chat_id
        try:
            bot.send_message(chat_id=chat_id, text='Прокурор не в конторе')
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            log('Network error in deputy_alone, retrying sending a message...')
            bot.send_message(chat_id=chat_id, text='Прокурор не в конторе')
        log('Notifying ' + str(chat_id) + ' that prosecutor is not in office')


# sending help_start.txt contents to user on /start and help.txt on /pomogite
@send_action(ChatAction.TYPING)
def pomogite_start(bot, update):
    chat_id = update.message.chat_id
    f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/help_start.txt', 'r', encoding='UTF-8')
    pomosh = f.read()
    f.close()
    write_user(chat_id)
    try:
        bot.send_message(chat_id=chat_id, text=pomosh)
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        log('Network error in pomogite, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=pomosh)
    log('Sending help to ' + str(chat_id))

    try:
        bot.send_message(chat_id=chat_id, text='Не хотите представиться?')
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        log('Network error in pomogite, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=pomosh)
    log('Asking to uncover the identity '
                 + str(chat_id))


@send_action(ChatAction.TYPING)
def pomogite(bot, update):

    chat_id = update.message.chat_id
    f = open('C:/Users/Tedd/Documents/Python/Bot/Receptura/help.txt', 'r', encoding='UTF-8')
    pomosh = f.read()
    f.close()
    sleep(2)
    try:
        bot.send_message(chat_id=chat_id, text=pomosh)
    except telegram.error.NetworkError as identifier:
        logging.debug(str(identifier))
        log('Network error in pomogite, retrying sending a message...')
        bot.send_message(chat_id=chat_id, text=pomosh)
    log('Sending help to ' + str(chat_id))


# every minute bot de-sleepes itself by sending me a message and then deleting it right after
# gotta be a smarter way to stay connected, but it seems like not with proxy enabled
def check_connection(bot, update):
    global SERVICE_MESSAGE_ID
    global SERVICE_MESSAGE_EXISTS
    global LIST_OF_ADMINS
    for chat_id in LIST_OF_ADMINS:
        if SERVICE_MESSAGE_EXISTS:
            try:
                bot.delete_message(chat_id=chat_id, message_id=SERVICE_MESSAGE_ID, timeout=10)
                logging.debug(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + 'removing old service message')
            except telegram.error.BadRequest as identifier:
                log('creating new service message')

        logging.debug(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") +
                      'trying to keep this thing alive sending new service message')
        try:
            SERVICE_MESSAGE_ID = bot.send_message(chat_id=chat_id, text='bot online').message_id
        except telegram.error.NetworkError as identifier:
            SERVICE_MESSAGE_ID = bot.send_message(chat_id=chat_id,
                                                  text='bot died with message: '
                                                       + str(identifier) + '\n\nbut now online').message_id
        SERVICE_MESSAGE_EXISTS = True
        save()


# i made a wise decision to log everything users input into the bot here
def log_user_messages(bot, update):
    chat_id = update.message.chat_id
    log('user ' + str(chat_id)
                 + ' sent a message: ' + update.message.text)
    with open('C:/Users/Tedd/Documents/Python/Bot/Receptura/user_chat_log.txt', 'a', encoding='UTF-8') as f:
        f.write(datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ") + str(chat_id)
                + ' : ' + update.message.text+'\n')


@restricted
def whisper(bot, update):
    whisper_text = update.message.text
    whisper_text = whisper_text.replace("/whisper ", '')
    for user in userbase:
        try:
            bot.send_message(chat_id=user, text=whisper_text)
        except telegram.error.Unauthorized as identifier:
            log('Unauthorized in whisper')
            # switch_user_by_id(user)
        except telegram.error.BadRequest as identifier:
            log('Bad Requset in whisper')
            # switch_user_by_id(user)
        except telegram.error.NetworkError as identifier:
            logging.debug(str(identifier))
            log('Network error in whisper, retrying sending a message...')
            bot.send_message(chat_id=user, text=whisper_text)
        log('echoing whisper to ' + str(user))


# program execution starts here
def main():
    logging.basicConfig(level=logging.DEBUG)
    # loading autosave
    # and basic preparations
    load()

    # testbot token : 986575172:AAHAppjUU5zdld-9tHb2ZlHs2Y43WWOKLkI
    # main release bot token : 1050540100:AAES5K5asAlvQdB1BjhlFDJEvaCf3COFF_A
    # admin id = 640200905
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
    log("started logger successfully")
    dp.add_handler(CommandHandler('kto_gde', kto_gde))
    dp.add_handler(CommandHandler('switch_notifications', switch_user))
    dp.add_handler(CommandHandler('lone_zam', deputy_alone))
    dp.add_handler(CommandHandler('lone_chef', prosecutor_alone))
    dp.add_handler(CommandHandler('pomogite', pomogite))
    dp.add_handler(CommandHandler('start', pomogite_start))
    dp.add_handler(CommandHandler('whisper', whisper))
    dp.add_handler(MessageHandler(Filters.text, log_user_messages))
    job_queue = updater.job_queue
    job_queue.run_repeating(someone_left, interval=60, first=0)
    job_queue.run_repeating(check_connection, interval=60, first=0)

    # some more magic just dont ever touch it 
    updater.start_polling()
    updater.idle()


# i read somewhere that this is needed somehow
if __name__ == "__main__":
    main()
