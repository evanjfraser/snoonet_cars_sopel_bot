import sopel
import unicodedata



@sopel.module.commands('2f1b','twof')


def twof(bot, trigger):
    out = "2F1B: Two steps forward, one step back"
    return bot.say(out)
    
