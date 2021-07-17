from discord.ext import commands
import discord

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "社群相關"

    @commands.command()
    async def 開發者資訊(self, ctx):
        print()

    # @commands.command()
    # async def 開發者資訊(self, ctx):
    #     print()

def setup(bot):
    bot.add_cog(About(bot))