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

bot = commands.Bot(command_prefix="+")

@bot.event
async def on_ready():
    print(">> Online <<")
    await bot.change_presence(activity=discord.Game(name="陰陽師 / help查看更多"))

@bot.event
async def on_message(msg):
    keywords = list(jdata_2.keys())
    rewardchannellist = list(jdata_1["RewardAgreeChannel"])
    for keyword in keywords:
        if keyword in msg.content and msg.channel.id in rewardchannellist and msg.author != bot.user and msg.is_system() == False:
            for ans in jdata_2[keyword]:
                await msg.channel.send(ans)

    questions = list(jdata_3.keys())
    qachannellist = list(jdata_1["QAAgreeChannel"])
    for question in questions:
        if msg.content in question and msg.channel.id in qachannellist and msg.author != bot.user and msg.is_system() == False:
            await msg.channel.send(jdata_3[question])

bot.run(os.environ['TOKEN'])
