import sopel
import unicodedata
import random


bang = ["BANG", "POW", "SLAM", "WHACK", "SLAP", "KAPOW", "ZAM", "BOOM"]
blow_type = ["devastating", "destructive", "ruthless", "damaging", "ruinous", "catastrophic", "traumatic", "shattering", "overwhelming", "crushing", "fierce", "deadly", "lethal", "fatal", "savage", "violent"]
victory = ["wins", "stands victorious", "triumphs", "conquers", "is the champion", "is the victor" ]
blow = ["uppercut", "hammerfist", "elbow strike", "shoulder strike", "front kick", "side kick", "roundhouse kick", "knee strike", "butt strike", "headbutt", "haymaker punch", "palm strike", "pocket bees"]

@sopel.module.commands('fight',"fite", "spar", "challenge")


def fight(bot, trigger):
    """<nick>, makes you fight <nick> and generates a winner."""
    fighter1 = trigger.nick
    if not trigger.group(2):
        out = "gimme something for you to fight with"
    else:
        fighter2 = trigger.group(2)
        if random.random() < .5:
            out = "{}! {}! {}! {} {} over {} with a {} {}.".format(random.choice(bang), random.choice(bang), random.choice(bang), fighter1, random.choice(victory),fighter2, random.choice(blow_type), random.choice(blow))
        else:
            out = "{}! {}! {}! {} {} over {} with a {} {}.".format(random.choice(bang), random.choice(bang), random.choice(bang), fighter2, random.choice(victory),fighter1, random.choice(blow_type), random.choice(blow))

    return bot.say(out)
    
