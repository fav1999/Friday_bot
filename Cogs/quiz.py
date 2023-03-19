import asyncio

from Dict.dict_quiz import dict_quiz_var
import discord
from discord.ext import commands


class Quiz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command()
    async def embed(self, ctx):

        embed = discord.Embed(
            title='Викторина',
            description=f'{dict_quiz_var[1][0]}',
            color=ctx.author.color,
            type='rich'
        )

        # embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        embed.set_thumbnail(url='https://oir.mobi/uploads/posts/2021-02/1612353417_29-p-anime-devushka-s-knigoi-art-kartinki-42.jpg')

        var1 = dict_quiz_var[1][1]
        var2 = dict_quiz_var[1][2]
        var3 = dict_quiz_var[1][3]
        var4 = dict_quiz_var[1][4]

        embed.add_field(name=f'1. {var1}', value='', inline=False)
        embed.add_field(name=f'2. {var2}', value='', inline=False)
        embed.add_field(name=f'3. {var3}', value='', inline=False)
        embed.add_field(name=f'4. {var4}', value='', inline=False)
        embed.set_footer(text='===============================================')

        message = await ctx.send(embed=embed)
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')

        await asyncio.sleep(5)

        new_message = await ctx.fetch_message(message.id)

        one_choice = new_message.reactions[0].count - 1
        second_choice = new_message.reactions[1].count - 1
        third_choice = new_message.reactions[2].count - 1
        fourth_choice = new_message.reactions[3].count - 1

        await ctx.send(f'Результат голосования:\nза {var1}: {one_choice} голосов\nза {var2}: {second_choice} голосов\nза {var3}: {third_choice} голосов\nза {var4}: {fourth_choice} голосов')

        await asyncio.sleep(3)

        await ctx.send(f'Правильный ответ:\n||{var3}||')


async def setup(bot):
    await bot.add_cog(Quiz(bot))
