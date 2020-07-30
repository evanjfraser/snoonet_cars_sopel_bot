
import sopel
import unicodedata
import random
import urllib


@sopel.module.commands('insult')


def insult(bot, trigger):
    nick = trigger.nick
    insult_file = "list-of-insults"

    with open(insult_file) as f:
        insult_list = f.readlines()

    random.seed()
    insult = insult_list[random.randrange(len(insult_list))]

    if trigger.group(2):
        if nick in trigger.group(2):
            out = "Hey, %s! %s said you're a %s!" % (trigger.group(2), nick, insult)
    else:
        out = "Hey, %s! You're a %s!" % (nick, insult)

    return bot.say(out)
