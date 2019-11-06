from mediawiki import MediaWiki
def get_search(search_phrase):
    wikipedia = MediaWiki(user_agent='chucha-user-agent-string')
    open_search_result = wikipedia.search(search_phrase)
    return open_search_result