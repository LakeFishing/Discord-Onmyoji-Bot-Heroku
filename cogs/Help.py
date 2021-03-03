from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "幫助"

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "Help", color = 0xffff00)
        for x in self.bot.cogs:
            cog_commands = (self.bot.get_cog(x)).get_commands()
            cog_name = (self.bot.get_cog(x)).name
            if cog_commands and x not in ["Help"]:
                commands = []
                for y in cog_commands:
                    commands.append(y.name)
                commands = "```" + (" / ".join(map(str, sorted(commands)))) + "```"
                embed.add_field(name = f"> {cog_name}", value = commands, inline = False)
        await ctx.channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))