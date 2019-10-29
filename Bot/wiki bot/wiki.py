from mediawiki import MediaWiki
import wikipedia
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import search_pages
import get_pages
from telegram.ext.dispatcher import run_async
import random

query = ''
music_related_syntax = ''
f =  open('C:\\Users\\Tom\\Documents\\Python\\Bot\\wiki bot\\words_alpha.txt')
valid_words = f.read().split()
f = open(r'C:\\Users\\Tom\\Documents\\Python\\Bot\\wiki bot\\query.txt')
query = f.read()
music_related_syntax = query.split('\n')
print('searching for: ' + str(music_related_syntax))
english_words = valid_words
print(len(english_words))

def get_result(mediawiki, search_phrase):
    search_result = search_pages.get_search(search_phrase)
    results_count = len(search_result)

    search_item_id = 0
    if results_count > 0:
        result_page = get_pages.get_page(search_result[search_item_id])
        while not related(result_page.categories):
            search_item_id += 1
            if search_item_id >= results_count:
                return None
            result_page = get_pages.get_page(search_result[search_item_id])
        return result_page
    else:
        return None

def related(categories):
    # TO_DO ADVANCED SEARCH
    entries_count = 0
    for word in music_related_syntax:
        for category in categories:
            for subcats in category.split(' '):
                if word == subcats.lower():
                    entries_count += 1
    if entries_count > 1:
        return True
    else:
        return False

def get_final_page():
    mediawiki = MediaWiki(user_agent='chucha-user-agent-string')
    page = None

    while page == None:
        search_phrase = random.choice(english_words)
        # search_phrase = 'music'
        page = get_result(mediawiki, search_phrase)

    print(page.title)
    print(page.url)
    return page

@run_async
def read(bot, update):
    print('new user request')
    chat_id = update.message.chat_id
    page = get_final_page()
    print('sending user url to a page')
    send_text = page.title + '\n' + page.url
    bot.sendMessage(chat_id = chat_id, text = send_text)

@run_async
def error(bot, update):
    print('Update "%s" caused error "%s"', bot, update.error)

def main():
    TOKEN="939616002:AAHbVEL3YLOJ_Zriy7bqXUmePntjbTqauK8"
    REQUEST_KWARGS={
        'proxy_url': 'socks5://193.37.152.154:8814',

        'urllib3_proxy_kwargs': {
           'username': 'anus_rkn',
           'password': 'is_blocked_hard',
        }
    }
    print("connecting to tg via proxy...")
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS, workers=20)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('read',read))
    dp.add_error_handler(error)
    print("starting polling...")
    updater.start_polling()
    print("idling...")
    updater.idle()


if __name__ == '__main__':
    main()
