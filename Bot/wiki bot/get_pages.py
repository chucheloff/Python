import wikipedia
import random

def get_page(title):
    try:
        page = wikipedia.page(title)
    except wikipedia.exceptions.DisambiguationError as e:
        if len(e.options) > 0:
            s = random.choice(e.options)
            while 'disambiguation' in s.lower():
                s = random.choice(e.options)
            page = wikipedia.page(s)
        else:
            print ('...\nwtf is this error omg\n')
    return page