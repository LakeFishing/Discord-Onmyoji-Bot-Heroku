from discord.ext import commands
import discord
import json
import pymysql
import requests
import os

DB_setting = {
    "host" : str(os.environ['HOST']),
    "port" : 3306,
    "user" : str(os.environ['USER']),
    "password" : str(os.environ['PASSWORD']),
    "db" : "lakefish_onmyoji",
    "charset" : "utf8"
}

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "查詢相關"

    @commands.command()
    async def 懸賞(self, ctx, target):
        embed = discord.Embed(title = "查詢結果", color = 0xffff00)
        conn = pymysql.connect(**DB_setting)
        try:
            with conn.cursor() as cursor:
                command = f"SELECT ans1, ans2, ans3 FROM reward WHERE name = '{target}'"
                cursor.execute(command)
                fetch = cursor.fetchone()
                reward_result = []
                for x in fetch:
                    if x != "":
                        reward_result.append("```" + x + "```")
                reward_result = ("".join(map(str, reward_result)))
            embed.add_field(name = "> 懸賞封印", value = reward_result, inline = True)
        except:
            reward_result = "```該式神無資料或輸入錯誤```"
            embed.add_field(name = "> 錯誤", value = reward_result, inline = True)
        await ctx.channel.send(embed = embed)

    @commands.command()   
    async def 線索(self, ctx, target):
        embed = discord.Embed(title = "查詢結果", color = 0xffff00)
        conn = pymysql.connect(**DB_setting)
        try:
            with conn.cursor() as cursor:
                command = f"SELECT name FROM clues WHERE clue LIKE '%{target}%'"
                cursor.execute(command)
                fetch = cursor.fetchall()
                clue_result = []
                reward_result = []
                if len(fetch) == 1:
                    command = f"SELECT name FROM clues WHERE clue LIKE '%{target}%'"
                    cursor.execute(command)
                    fetch = cursor.fetchone()
                    for x in fetch:
                        if x != "":
                            clue_result.append("```" + x + "```")
                            command = f"SELECT ans1, ans2, ans3 FROM reward WHERE name = '{x}'"
                            cursor.execute(command)
                            fetch = cursor.fetchone()
                            for y in fetch:
                                if y != "":
                                    reward_result.append("```" + y + "```")
                            reward_result = ("".join(map(str, reward_result)))
                    clue_result = ("".join(map(str, clue_result)))
                    embed.add_field(name = "> 線索對應式神", value = clue_result, inline = False)
                    embed.add_field(name = "> 懸賞封印", value = reward_result, inline = False)
                elif len(fetch) > 1:
                    for x in fetch:
                        for y in x:
                            if y != "":
                                y = y.replace("\'","")
                                clue_result.append("```" + y + "```")
                    clue_result = ("".join(map(str, clue_result)))
                    embed.add_field(name="> 線索對應式神", value=clue_result, inline=False)
        except:
            clue_result = "```該式神無資料或輸入錯誤```"
            embed.add_field(name = "> 錯誤", value = clue_result, inline = True)
        await ctx.channel.send(embed = embed)

    @commands.command()
    async def 逢魔(self, ctx, target):
        embed = discord.Embed(title = "查詢結果", color = 0xffff00)
        conn = pymysql.connect(**DB_setting)
        try:
            with conn.cursor() as cursor:
                command = f"SELECT question, answer FROM qa WHERE question LIKE '%{target}%'"
                cursor.execute(command)
                fetch = cursor.fetchall()
                qa_result = []
                if len(fetch) != 0:
                    for x in range(len(fetch)):
                        qa_result.append("```題目：" + fetch[x][0] + " / 答案：" + fetch[x][1] + "```")
                    qa_result = ("".join(map(str, qa_result)))
                    embed.add_field(name = "> 逢魔之時", value = qa_result, inline = False)
                else:
                    qa_result = "```該關鍵字無資料或輸入錯誤```"
                    embed.add_field(name = "> 錯誤", value = qa_result, inline = True)
        except:
            qa_result = "```該關鍵字無資料或輸入錯誤```"
            embed.add_field(name = "> 錯誤", value = qa_result, inline = True)
        if embed.__len__() >= 1000:
            embed.clear_fields()
            embed.add_field(name = "> 錯誤", value = "```查詢結果過多，判定為錯誤查詢```", inline = False)
            embed.set_footer(text="有任何問題或建議請找 YellowToFish#5671")
        await ctx.channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Search(bot))