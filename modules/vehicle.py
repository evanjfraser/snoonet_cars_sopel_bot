import sopel
import riak
import unicodedata

bucket='rcarsvehicle'

@sopel.module.commands('vehicle')

def vehicle(bot, trigger):
    n=trigger.nick
    r=" has a: "
    l=""
    if not trigger.group(2):
        fetch=readdbattr(n.lower(),'vehicle')
        if fetch:
            l=fetch
        else:
            r=": Tell me what vehicle you have: "
    else:
        t = unicodedata.normalize('NFKD', trigger.group(2)).encode('ascii', 'ignore').split(' ')
        if len(t) >= 1:
            if t[0] == 'set':
                if len(t) < 2:
                    r=': You forgot to tell me what vehicle you have!'
                else:
                    updatedbattr(n.lower(), 'vehicle',trigger.group(2)[4:])
                    return bot.say('Saving your vehicle!')
            else:
                n=t[0].lower()
                fetch=readdbattr(n,'vehicle')
                if fetch:
                    l=fetch
                else:
                    r=": Give me a vehicle with .vehicle set <vehicle type>"
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
