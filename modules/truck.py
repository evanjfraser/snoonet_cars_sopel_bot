import sopel

@sopel.module.commands('truck')
def truck(bot, trigger):
    bot.say('Hi ' + trigger.nick + ', Im a truck!')
