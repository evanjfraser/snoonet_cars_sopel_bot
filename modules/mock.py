import sopel
import unicodedata
import random


@sopel.module.commands('mock')
def mock(bot, trigger):
    if trigger.group(2):
        out = mocktext(trigger.group(2))
    else:
        out = "Gimme something to mock!"
    return bot.say(out)


def mocktext(text):
    output_text = ""
    for char in text:
        if char.isalpha():
            if random.random() > 0.5:
                output_text += char.upper()
            else:
                output_text += char.lower()
        else:
            output_text += char
    return output_text
