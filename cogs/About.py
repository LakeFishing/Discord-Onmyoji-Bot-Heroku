from discord.ext import commands
import discord

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "社群相關"

    @commands.command()
    async def 開發者資訊(self, ctx):
        embed = discord.Embed(title = "開發者資訊", color = 0xffff00)
        embed.add_field(name = "> Name and Tag", value = "```YellowToFish#5671```", inline = False)
        embed.add_field(name = "> Support URL", value = "https://discord.gg/fK8QhqZVMx", inline = False)
        await ctx.channel.send(embed = embed)

    # @commands.command()
    # async def 開發者資訊(self, ctx):
    #     print()

def setup(bot):
    bot.add_cog(About(bot))