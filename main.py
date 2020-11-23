import discord
from discord.ext import commands
import json
import os

from PIL import Image

import rare
import event

with open("setting.json","r",encoding="utf-8") as jFile_1:
    jdata_1 = json.load(jFile_1)

with open("search_reward.json","r",encoding="utf-8") as jFile_2:
    jdata_2 = json.load(jFile_2)

with open("search_qa.json","r",encoding="utf-8") as jFile_3:
    jdata_3 = json.load(jFile_3)

with open("search_clue.json","r",encoding="utf-8") as jFile_4:
    jdata_4 = json.load(jFile_4)

bot = commands.Bot(command_prefix="+")
bot.remove_command("help")
prefix = "+"

@bot.event
async def on_ready():
    print(">> Online <<")
    await bot.change_presence(activity=discord.Game(name="陰陽師 / +help查看更多"))

@bot.event
async def on_message(msg):
    
    qa_string = ""
    clue_string = ""

    result = False
    qa_result = False
    clue_result = False

    rewardchannellist = list(jdata_1["RewardAgreeChannel"])
    qachannellist = list(jdata_1["QAAgreeChannel"])
    keywords = list(jdata_2.keys())
    questions = list(jdata_3.keys())
    clues = list(jdata_4.keys())

    embed=discord.Embed(title="查詢結果", color=0xffff00)

    if msg.author != bot.user and msg.author.bot == False and msg.is_system() == False and msg.content.startswith("+"):
        word_string_in_temp = msg.content.lstrip("+")
        word_string = word_string_in_temp.lstrip()

        """懸賞封印"""
        for keyword in keywords:
            if keyword in word_string and msg.channel.id in rewardchannellist:
                embed.add_field(name="> 懸賞封印", value=jdata_2[keyword], inline=False)
                result = True

        """懸賞封印線索"""
        for clue in clues:
            if word_string in clue and msg.channel.id in rewardchannellist:
                clue_string += jdata_4[clue]
                result = True
                clue_result = True
        if clue_result == True:
            embed.add_field(name="> 懸賞封印線索", value=clue_string, inline=False)

        """逢魔之時"""
        for question in questions:
            if word_string.upper() in question and msg.channel.id in qachannellist:
                qa_string += jdata_3[question]
                result = True
                qa_result = True
        if qa_result == True:
            embed.add_field(name="> 逢魔之時", value=qa_string, inline=False)

        """HELP"""
        if word_string.upper() == "HELP":
            embed=discord.Embed(title="Help", color=0xffff00)
            embed.add_field(name="> 名稱", value="```陰陽師助手```", inline=False)
            embed.add_field(name="> 查詢相關", value="```懸賞封印 / 懸賞封印線索 / 逢魔答題```", inline=False)
            embed.add_field(name="> 抽卡相關", value="```無活動概率十抽 / 活動概率十抽```", inline=False)
            embed.add_field(name="> 更新時間", value="```2020/11/15```", inline=False)
            embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
            await msg.channel.send(embed=embed)

        """更新日誌"""
        if word_string.upper() == "LOG":
            embed=discord.Embed(title="Change Log", color=0xffff00)
            embed.add_field(name="> 更新日誌", value="```新增：活動十抽模擬抽卡``````新增：抽卡結果下方概率公示```", inline=False)
            embed.add_field(name="> 更新時間", value="```2020/11/23```", inline=False)
            embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
            await msg.channel.send(embed=embed)

        """正常結果"""
        if result == True and embed.__len__() < 1000:
            embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
            await msg.channel.send(embed=embed)

        """錯誤結果"""
        if embed.__len__() >= 1000:
            embed.clear_fields()
            embed.add_field(name="> 錯誤", value="```查詢結果過多，判定為錯誤查詢```", inline=False)
            embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
            await msg.channel.send(embed=embed)

    await bot.process_commands(msg)

@bot.command()
async def 十抽(msg):

    white = False

    rolledchannellist = list(jdata_1["RolledChannel"])

    if msg.channel.id in rolledchannellist:
        toImage = Image.new('RGBA',(600,240),color="white")
        pic_list, pic_num, rare_list = event.Rolled()

        for i in range(10):
            try:
                fromImage = Image.open(pic_list[i])
                loc = ((int(i/2) * 120), (i % 2) * 120)
                toImage.paste(fromImage, loc)
                fromImage.close()
            except:
                white = True
                break
        
        if white == False:
            save_name = str(pic_num) + ".png"
            toImage.save(save_name)
            toImage.close()
            file = discord.File(save_name, filename="image.png")
            
            embed = discord.Embed(title="十抽結果", color=0xffff00)
            embed.add_field(name="> SP & SSR 數量", value="```" + str(rare_list[0] + rare_list[1]) + "```", inline=False)
            embed.add_field(name="> SR 數量", value="```" + str(rare_list[2]) + "```", inline=True)
            embed.add_field(name="> R 數量", value="```" + str(rare_list[3]) + "```", inline=True)
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="SP : 0.25% ; SSR : 1% ; SR : 20% ; R : 78.75%\n有任何問題或建議請找 YellowToFish#5671")
            await msg.channel.send(file=file, embed = embed)
            os.remove(save_name)
        else:
            embed = discord.Embed(title="十抽結果", color=0xffff00)
            embed.add_field(name="> SP & SSR 數量", value="```" + str(rare_list[0] + rare_list[1]) + "```", inline=False)
            embed.add_field(name="> SR 數量", value="```" + str(rare_list[2]) + "```", inline=True)
            embed.add_field(name="> R 數量", value="```" + str(rare_list[3]) + "```", inline=True)
            embed.set_footer(text="暫時無法生成抽卡結果圖片\n有任何問題或建議請找 YellowToFish#5671")
            await msg.channel.send(embed = embed)

@bot.command()
async def 活動十抽(msg):

    white = False

    rolledchannellist = list(jdata_1["RolledChannel"])

    if msg.channel.id in rolledchannellist:
        toImage = Image.new('RGBA',(600,240),color="white")
        pic_list, pic_num, rare_list = rare.Rolled()

    for i in range(10):
            try:
                fromImage = Image.open(pic_list[i])
                loc = ((int(i/2) * 120), (i % 2) * 120)
                toImage.paste(fromImage, loc)
                fromImage.close()
            except:
                white = True
                break
        
    if white == False:
        save_name = str(pic_num) + ".png"
        toImage.save(save_name)
        toImage.close()
        file = discord.File(save_name, filename="image.png")
            
        embed = discord.Embed(title="活動十抽結果", color=0xffff00)
        embed.add_field(name="> SP & SSR 數量", value="```" + str(rare_list[0] + rare_list[1]) + "```", inline=False)
        embed.add_field(name="> SR 數量", value="```" + str(rare_list[2]) + "```", inline=True)
        embed.add_field(name="> R 數量", value="```" + str(rare_list[3]) + "```", inline=True)
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text="SP : 0.625% ; SSR : 2.5% ; SR : 20% ; R : 76.875%\n新式神SSR千姬出現概率占SSR概率中的15%\n有任何問題或建議請找 YellowToFish#5671")
        await msg.channel.send(file=file, embed = embed)
        os.remove(save_name)
    else:
        embed = discord.Embed(title="活動十抽結果", color=0xffff00)
        embed.add_field(name="> SP & SSR 數量", value="```" + str(rare_list[0] + rare_list[1]) + "```", inline=False)
        embed.add_field(name="> SR 數量", value="```" + str(rare_list[2]) + "```", inline=True)
        embed.add_field(name="> R 數量", value="```" + str(rare_list[3]) + "```", inline=True)
        embed.set_footer(text="暫時無法生成抽卡結果圖片\n有任何問題或建議請找 YellowToFish#5671")
        await msg.channel.send(embed = embed)

bot.run(os.environ['TOKEN'])
