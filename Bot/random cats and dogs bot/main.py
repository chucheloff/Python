from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from telegram.ext.dispatcher import run_async
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info('lets start this new adventure')

def get_dog_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_dog_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_dog_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_cat_url():
    contents = requests.get('https://aws.random.cat/meow').json()    
    url = contents['file']
    return url

def get_cat_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_cat_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def meow(bot, update):
    logging.debug('requesting cat image url')
    url = get_cat_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    print('sending a lil meow')
    
def get_cat_gif_url():
    file_extension = ''
    while file_extension != 'gif':
        url = get_cat_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async  
def meow_gif (bot, update):
    url = get_cat_gif_url()
    chat_id = update.message.chat_id
    bot.send_document(chat_id = chat_id, document = url)
    print('sending a cat gif')
    

def get_dog_gif_url():
    file_extension = ''
    while file_extension != 'gif':
        url = get_dog_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
 
@run_async 
def woof_gif (bot, update):
    url = get_dog_gif_url()
    chat_id = update.message.chat_id
    bot.send_document(chat_id = chat_id, document = url)
    print('sending a dog gif')
    
@run_async
def woof(bot, update):
    url = get_dog_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    print('sending a cute doggo')
    
    
def main():
    TOKEN="953608142:AAHNAwTTe4kFHldfP_m2s_eRqkq1RT-2FXs"
    REQUEST_KWARGS={
        'proxy_url': 'socks5://193.37.152.154:8814',
        
        'urllib3_proxy_kwargs': {
           'username': 'anus_rkn',
           'password': 'is_blocked_hard',
        }
    }
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS, workers= 20)
    dp = updater.dispatcher
    
    logging.debug("started logger successfully")
    dp.add_handler(CommandHandler('woof',woof))


    dp.add_handler(CommandHandler('woof_gif',woof_gif))
    dp.add_handler(CommandHandler('meow_gif', meow_gif))
    dp.add_handler(CommandHandler('meow',meow))
    
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()