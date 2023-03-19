import json
import random
import string

from discord.ext import commands

from Dict.dict_send_msg import dict_msg


class Censore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command
    @commands.command()
    async def test(self, ctx):
        await ctx.send('Hallo!')

    # event
    @commands.Cog.listener()
    async def on_message(self, message):
        if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.content.split(' ')} \
                .intersection(set(json.load(open('I:/Projects/Friday_bot/Dict/censor_words.json')))) != set():
            await message.channel.send(f'{message.author.mention}, {dict_msg[random.randint(0, len(dict_msg) - 1)]}')


async def setup(bot):
    await bot.add_cog(Censore(bot))
