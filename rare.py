import random
import os

def Rolled():
    pic_list = []
    pic_num = 0

    sp_num = 0
    ssr_num = 0
    sr_num = 0
    r_num = 0

    chance = 10
    while chance != 0:
        luckNum = random.randint(1,10000)
        pic_num = pic_num + luckNum
        if luckNum <= 25:
            pic_list.append(SP())
            sp_num = sp_num + 1
        elif luckNum <= 125:
            pic_list.append(SSR())
            ssr_num = ssr_num + 1
        elif luckNum <= 2125:
            pic_list.append(SR())
            sr_num = sr_num + 1
        elif luckNum <= 10000:
            pic_list.append(R())
            r_num = r_num + 1
        chance = chance - 1
    return pic_list, pic_num, [sp_num, ssr_num, sr_num, r_num]

def SP():
    sp_file = os.listdir("./icons/SP/")
    sp_pic = random.choice(sp_file)
    return str("./icons/SP/" + sp_pic)

def SSR():
    ssr_file = os.listdir("./icons/SSR/")
    ssr_pic = random.choice(ssr_file)
    return str("./icons/SSR/" + ssr_pic)

def SR():
    sr_file = os.listdir("./icons/SR/")
    sr_pic = random.choice(sr_file)
    return str("./icons/SR/" + sr_pic)

def R():
    r_file = os.listdir("./icons/R/")
    r_pic = random.choice(r_file)
    return str("./icons/R/" + r_pic)