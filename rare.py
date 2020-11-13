import random
import json

with open("picture.json","r",encoding="utf-8") as jFile_5:
    jdata_5 = json.load(jFile_5)

def Rolled():
    pic_list = []
    pic_num = 0
    chance = 10
    while chance != 0:
        luckNum = random.randint(1,10000)
        pic_num = pic_num + luckNum
        if luckNum <= 25:
            pic_list.append(SP())
        elif luckNum <= 125:
            pic_list.append(SSR())
        elif luckNum <= 2125:
            pic_list.append(SR())
        elif luckNum <= 10000:
            pic_list.append(R())
        chance = chance - 1
    return pic_list, pic_num

def SP():
    a = random.choice(jdata_5["sp"])
    return a[1]

def SSR():
    b = random.choice(jdata_5["ssr"])
    return b[1]

def SR():
    c = random.choice(jdata_5["sr"])
    return c[1]

def R():
    d = random.choice(jdata_5["r"])
    return d[1]