from discord.ext import commands
import discord

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "社群相關"

    @commands.command()
    async def 推廣平台(self, ctx):
        await ctx.channel.send("https://top.gg/bot/721313416509390848")

    @commands.command()
    async def 意見反饋(self, ctx):
        await ctx.channel.send("https://discord.gg/fK8QhqZVMx")

def setup(bot):
    bot.add_cog(About(bot))