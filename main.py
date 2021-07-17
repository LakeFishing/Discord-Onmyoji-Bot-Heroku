from discord.ext import commands
import discord
import json
import os

bot = commands.Bot(command_prefix="+")

@bot.event
async def on_ready():
    print(">> Online <<")
    await bot.change_presence(activity=discord.Game(name="陰陽師 / +help查看更多"))
    count = 0
    for _ in bot.guilds:
        count +=1
        print(_.id)
    print(str(count))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

bot.remove_command("help")
bot.load_extension("cogs.Help")
bot.load_extension("cogs.Roll")
bot.load_extension("cogs.Search")
bot.load_extension("cogs.Updates")
bot.run(os.environ['TOKEN'])