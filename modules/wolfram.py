import sopel
import unicodedata
import random
import tungsten
import json

with open('creds.json','r') as credsfile:
     wa_api = json.load(credsfile)['wolfram_key']

@sopel.module.commands('wat','wa','wolfram')


def wolfram(bot, trigger):
    nick = trigger.nick

    client = tungsten.Tungsten(wa_api)
    if not trigger.group(2):
        out = "%s please provide a query" % (nick)
        return bot.say(out)

    result = client.query(trigger.group(2))
    if result.success:
        out = "%s: %s" % (nick, result.pods[1].format['plaintext'][0])
    else:
        if result.error is None:
            msg = "No match found sorry"
            out = "%s: %s" % (nick, msg)
        else:
            out = "%s: %s" % (nick, result.error)

    return bot.say(out)
    
