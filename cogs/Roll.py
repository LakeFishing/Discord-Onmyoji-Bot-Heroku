from discord.ext import commands
from PIL import Image
import discord
import random
import os

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "抽卡相關"

    @commands.command()
    async def 十抽(self, ctx):
        toImage = Image.new('RGBA',(600,240),color="white")
        pic_list, pic_num, rare_list = Rolled()

        for i in range(10):
            fromImage = Image.open(pic_list[i])
            loc = ((int(i/2) * 120), (i % 2) * 120)
            toImage.paste(fromImage, loc)
            fromImage.close()
            
        save_name = str(pic_num) + ".png"
        toImage.save(save_name)
        toImage.close()
        file = discord.File(save_name, filename = "image.png")

        amount_SPSSR = "```" + str(rare_list[0] + rare_list[1]) + "```"
        amount_SR = "```" + str(rare_list[2]) + "```"
        amount_R = "```" + str(rare_list[3]) + "```"
                
        embed = discord.Embed(title = "十抽結果", color = 0xffff00)
        embed.add_field(name = "> SP & SSR 數量", value = amount_SPSSR, inline = True)
        embed.add_field(name = "> SR 數量", value = amount_SR, inline = True)
        embed.add_field(name = "> R 數量", value = amount_R, inline = True)
        embed.set_image(url = "attachment://image.png")
        embed.set_footer(text = "有任何問題或建議請找 YellowToFish#5671")
        await ctx.channel.send(file = file, embed = embed)
        os.remove(save_name)

    @commands.command()
    async def 活動十抽(self, ctx):
        toImage = Image.new('RGBA',(600,240),color="white")
        pic_list, pic_num, rare_list = Rolled_event()

        for i in range(10):
            fromImage = Image.open(pic_list[i])
            loc = ((int(i/2) * 120), (i % 2) * 120)
            toImage.paste(fromImage, loc)
            fromImage.close()
            
        save_name = str(pic_num) + ".png"
        toImage.save(save_name)
        toImage.close()
        file = discord.File(save_name, filename = "image.png")

        amount_SPSSR = "```" + str(rare_list[0] + rare_list[1]) + "```"
        amount_SR = "```" + str(rare_list[2]) + "```"
        amount_R = "```" + str(rare_list[3]) + "```"
                
        embed = discord.Embed(title = "活動十抽結果", color = 0xffff00)
        embed.add_field(name = "> SP & SSR 數量", value = amount_SPSSR, inline = True)
        embed.add_field(name = "> SR 數量", value = amount_SR, inline = True)
        embed.add_field(name = "> R 數量", value = amount_R, inline = True)
        embed.set_image(url = "attachment://image.png")
        embed.set_footer(text = "有任何問題或建議請找 YellowToFish#5671")
        await ctx.channel.send(file = file, embed = embed)
        os.remove(save_name)
    
    @commands.command()
    async def 概率(self, ctx):
        embed = discord.Embed(title = "抽卡概率", color = 0xffff00)
        embed.add_field(name = "> 十抽概率", value = "```SP  : 0.25%``````SSR : 1%```")
        embed.add_field(name = "> 活動十抽概率", value = "```SP  : 0.625%``````SSR : 2.5%```")
        embed.set_footer(text = "有任何問題或建議請找 YellowToFish#5671")
        await ctx.channel.send(embed = embed)

def Rolled_event():
        pic_list = []
        pic_num = 0

        sp_num = 0
        ssr_num = 0
        sr_num = 0
        r_num = 0

        chance = 10
        while chance != 0:
            luckNum = random.randint(1,100000)
            pic_num = pic_num + luckNum
            if luckNum <= 625:
                pic_list.append(SP_event())
                sp_num = sp_num + 1
            elif luckNum <= 3125:
                pic_list.append(SSR())
                ssr_num = ssr_num + 1
            elif luckNum <= 23125:
                pic_list.append(SR())
                sr_num = sr_num + 1
            elif luckNum <= 100000:
                pic_list.append(R())
                r_num = r_num + 1
            chance = chance - 1
        return pic_list, pic_num, [sp_num, ssr_num, sr_num, r_num]

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

def SP_event():
    eventUP = random.randint(1, 100)
    if eventUP <= 15:
        return str("icons/SP/358.png")
    elif eventUP <= 100:
        sp_file = os.listdir("icons/SP/")
        sp_pic = random.choice(sp_file)
        return str("icons/SP/" + sp_pic)

def SSR_event():
    eventUP = random.randint(1, 100)
    if eventUP <= 15:
        return str("icons/SSR/356.png")
    elif eventUP <= 100:
        ssr_file = os.listdir("icons/SSR/")
        ssr_pic = random.choice(ssr_file)
        return str("icon/SSR/" + ssr_pic)

def SP():
    sp_file = os.listdir("icons/SP/")
    sp_pic = random.choice(sp_file)
    return str("icons/SP/" + sp_pic)

def SSR():
    ssr_file = os.listdir("icons/SSR/")
    ssr_pic = random.choice(ssr_file)
    return str("icons/SSR/" + ssr_pic)

def SR():
    sr_file = os.listdir("icons/SR/")
    sr_pic = random.choice(sr_file)
    return str("icons/SR/" + sr_pic)

def R():
    r_file = os.listdir("icons/R/")
    r_pic = random.choice(r_file)
    return str("icons/R/" + r_pic)

def setup(bot):
    bot.add_cog(Roll(bot))