import sopel
import unicodedata
import random
import tungsten
import urllib
import json

from sopel import web

end_point = 'https://www.googleapis.com/customsearch/v1?'

with open('creds.json','r') as credsfile:
     api_key = json.load(credsfile)['google_key']

search_engine_id = '003328756286211179155%3Au2rpsdxrmru'
#eg GET https://www.googleapis.com/customsearch/v1?q=horses&cx=003328756286211179155%3Au2rpsdxrmru&key=AIzaSyCBB5aNVVPYd9rbxobKFu3Lwe-Zif6iwSs

@sopel.module.commands('g','go','goo','google')

def google(bot, trigger):
    nick = trigger.nick
    search_term = urllib.quote_plus(trigger.group(2))

    query = 'q=%s&key=%s&cx=%s' % (search_term,api_key,search_engine_id)
    body = web.get(end_point + query,
                   dont_decode=True)
    json_data = json.loads(body)

    # if json_data['data']:
    #     img_url = json_data['data']['image_original_url']
    #     out = '%s: %s' % (nick, img_url)
    # else:
    #     out = '%s: Nothing matches sorry!' % (nick)
    if json_data['items']:
        link = json_data['items'][0]['link']
        title = json_data['items'][0]['title']
        out = '%s: %s %s' % (nick, title, link)
    else:
        out = '%s: Nothing matches sorry!' % (nick)

    return bot.say(out)

