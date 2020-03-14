import sopel
import riak
import unicodedata

bucket='rcars'

@sopel.module.commands('photo')


def photo(bot, trigger):
    #bot.say('Hi ' + trigger.nick + ', Im a truck!')
    n=trigger.nick
    r="'s pride and joy looks like: "
    l=""
    if not trigger.group(2):
        fetch=readdbattr(n.lower(),'photo')
        if fetch:
            l=fetch
        else:
            r=": Give me a photo URL with .photo set url"
    else:
        t = unicodedata.normalize('NFKD', trigger.group(2)).encode('ascii', 'ignore').split(' ')
        if len(t) >= 1:
            if t[0] == 'set':
                if len(t) < 2:
                    r=': You forgot to give me the URL!'
                else:
                    updatedbattr(n.lower(), 'photo',trigger.group(2)[4:])
                    return bot.say('Saving your photo!')
            else:
                n=t[0].lower()
                fetch=readdbattr(n,'photo')
                if fetch:
                    l=fetch
                else:
                    r=": Give me a photo URL with .photo set url"
    return bot.say(n + r + l)

def readdb(key):
    r=riak.RiakClient(pb_port=8087, protocol='pbc')
    b=r.bucket(bucket)
    #   print 'readdb data'+ str(b.get(key).data)
    #return b.get(key).get_data()
    print b.get(key).data
    return b.get(key).data

def readdbattr(key,attr):
    r=readdb(key)
    if r:
        try:
            return r[attr]
        except:
            return None
    return None

def updatedbattr(key, attr, data):                                                                                                                                                     
    old=readdb(key)
    if old:
        old[attr]=data
    else:
        old={attr:data}
    savedb(key,old)

def savedb(key, data):                                                                                                                                                       
    db=riak.RiakClient(pb_port=8087, protocol='pbc')
    user_bucket=db.bucket(bucket)
    new_user=user_bucket.new(key, data)
    new_user.store()
