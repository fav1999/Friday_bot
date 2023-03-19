import discord
from discord.ext import commands
import os
from apikey import key
import asyncio

bot = commands.Bot(command_prefix=".", help_command=None, intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Streaming(name='League of Legends',
                                                                                     url='https://www.leagueoflegends'
                                                                                         '.com/ru-ru/'))
    print(f"Bot {bot.user} is ready to work!")


initial_extensions = []


async def load_extensions():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"Cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(key)


asyncio.run(main())
