import sopel
import unicodedata
import json
import urllib
import pprint
import os

from random import randrange
from sopel import web

end_point = "http://api.giphy.com/v1/gifs/search?"

with open('creds.json', 'r') as credsfile:
    api_key = json.load(credsfile)['giphy_key']

@sopel.module.commands('giphy')


def giphy(bot, trigger):
    nick = trigger.nick
    search_term = urllib.quote_plus(trigger.group(2))
    print(search_term)

    query = 'q=%s&api_key=%s' % (search_term,api_key)
    print(query)
    body = web.get(end_point + query,
                   dont_decode=True)
    json_data = json.loads(body)

    if json_data['data']:
        gif_range = len(json_data['data']) 

        if gif_range > 5:
            gif_range = 5
        gif_num = randrange(gif_range)
        img_url = json_data['data'][gif_num]['images']['original']['url']
        out = '%s: %s' % (nick, img_url)
    else:
        out = '%s: Nothing matches sorry!' % (nick)

    return bot.say(out)
    
