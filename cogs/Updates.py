from discord.ext import commands
import discord
import json

with open("data/updates.json", encoding = "utf-8") as file:
    updates_file = json.load(file)
    date_logs = updates_file["date_logs"]
    commands_logs = updates_file["commands_logs"]
    data_logs = updates_file["data_logs"]

class Updates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "更新相關"

    @commands.command()
    async def 功能更新日誌(self, ctx):
        embed = discord.Embed(title = "Commands Update Logs", color = 0xffff00)
        updates = []
        for x in commands_logs:
            updates.append("```" + x + "```")
        updates = ("".join(map(str, updates)))
        date = "```" + date_logs + "```"
        embed.add_field(name = "> 更新內容", value = updates)
        embed.add_field(name = "> 更新時間", value = date)
        await ctx.channel.send(embed = embed)

    @commands.command()
    async def 資料更新日誌(self, ctx):
        embed = discord.Embed(title = "Data Update Logs", color = 0xffff00)
        updates = []
        for x in data_logs:
            updates.append("```" + x + "```")
        updates = ("".join(map(str, updates)))
        date = "```" + date_logs + "```"
        embed.add_field(name = "> 更新內容", value = updates)
        embed.add_field(name = "> 更新時間", value = date)
        await ctx.channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Updates(bot))