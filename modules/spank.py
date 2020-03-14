import codecs
import json
import os
import random
import sopel
import textgen



#f = codecs.open('spank.json',encoding="utf-8"))
#spank_data = json.load(f)

#bdsm_data = json.load(codecs.open('bdsm.json',encoding="utf-8"))


@sopel.module.commands('spank')

def spank(bot, trigger):
    user = trigger.nick
    victim = trigger.group(2)
    with codecs.open("spank.json", encoding="utf-8") as f:
        spank_data = json.load(f)

    generator = textgen.TextGenerator(spank_data["templates"], spank_data["parts"],
                                      variables={"user": victim})
    # act out the message
    out = "%s %s" % (user,generator.generate_string())

    return bot.say(out)

@sopel.module.commands('bdsm')
def bdsm(bot, trigger):
    """Just a little bit of kinky fun."""
    user = trigger.nick
    victim = trigger.group(2)
    with codecs.open("bdsm.json", encoding="utf-8") as f:
        bdsm_data = json.load(f)

    generator = textgen.TextGenerator(bdsm_data["templates"], bdsm_data["parts"], variables={"user": victim})
    out = "%s %s" % (user,generator.generate_string())

    return bot.say(out)

