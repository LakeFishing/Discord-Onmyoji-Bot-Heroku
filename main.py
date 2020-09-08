import discord
from discord.ext import commands
import json
import os

with open("setting.json","r",encoding="utf-8") as jFile_1:
    jdata_1 = json.load(jFile_1)

with open("search_reward.json","r",encoding="utf-8") as jFile_2:
    jdata_2 = json.load(jFile_2)

with open("search_qa.json","r",encoding="utf-8") as jFile_3:
    jdata_3 = json.load(jFile_3)

with open("search_clue.json","r",encoding="utf-8") as jFile_4:
    jdata_4 = json.load(jFile_4)

bot = commands.Bot(command_prefix="+")

@bot.event
async def on_ready():
    print(">> Online <<")
    await bot.change_presence(activity=discord.Game(name="陰陽師 / help查看更多"))

@bot.event
async def on_message(msg):
    qa_string = ""
    clue_string = ""

    result = False
    qa_result = False
    clue_result = False

    embed=discord.Embed(title="查詢結果", color=0xffff00)

    keywords = list(jdata_2.keys())
    rewardchannellist = list(jdata_1["RewardAgreeChannel"])
    if msg.author != bot.user:
        for keyword in keywords:
            if keyword in msg.content and msg.channel.id in rewardchannellist and msg.is_system() == False:
                embed.add_field(name="> 懸賞封印", value=jdata_2[keyword], inline=False)
                result = True

    clues = list(jdata_4.keys())
    if msg.author != bot.user:
        for clue in clues:
            if msg.content in clue and msg.channel.id in rewardchannellist and msg.is_system() == False:
                clue_string += jdata_4[clue]
                result = True
                clue_result = True
        if clue_result == True:
            embed.add_field(name="> 懸賞封印線索", value=clue_string, inline=False)

    questions = list(jdata_3.keys())
    qachannellist = list(jdata_1["QAAgreeChannel"])
    if msg.author != bot.user:
        for question in questions:
            if msg.content.upper() in question and msg.channel.id in qachannellist and msg.is_system() == False:
                qa_string += jdata_3[question]
                result = True
                qa_result = True
        if qa_result == True:
            embed.add_field(name="> 逢魔之時", value=qa_string, inline=False)

    if result == True and embed.__len__() < 1000:
        embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
        await msg.channel.send(embed=embed)

    if embed.__len__() >= 1000:
        embed.clear_fields()
        embed.add_field(name="> 錯誤", value="```查詢結果過多，判定為錯誤查詢```", inline=False)
        embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
        await msg.channel.send(embed=embed)

    await bot.process_commands(msg)

    if msg.content.upper() == "HELP" and msg.author != bot.user and msg.is_system() == False:
        embed=discord.Embed(title="Help", color=0xffff00)
        embed.add_field(name="> 名稱", value="```陰陽師查詢工具```", inline=False)
        embed.add_field(name="> 查詢範圍", value="```懸賞封印 / 懸賞封印線索 / 逢魔答題```", inline=False)
        embed.add_field(name="> 更新時間", value="```2020/09/08```", inline=False)
        embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
        await msg.channel.send(embed=embed)

bot.run(os.environ['TOKEN'])