import disnake
import random
import typing
from disnake.ext import commands

ccommands = ['!бутылочка', '!bottles', '!podkl', "!трахнуть", '!slap', '!zxc', '!test']

class Commands(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.command()
    async def podkl(self, ctx):
        'подключает бота к гс каналу'
        await ctx.author.voice.channel.connect()

    @commands.command(name='бутылочка')
    async def bottles(self, ctx, value: typing.Optional[int] = 1, *, zxc='water'):
        'никому не нужная команда бутылочка)'
        await ctx.send(f'{value} бутылочек {zxc}')

    @commands.command(name='трахнуть')
    async def slap(self, ctx):
        'рандомно трахаешь кого нибудь из сервера'
        await ctx.send(f'{ctx.author.mention} выебал {random.choice(ctx.guild.members).mention}')

    @commands.command()
    async def zxc(self, ctx, *, value='курсед'):
        'команда zxc отправляет embed сообщение с курседом'
        embed = disnake.Embed(
            title=value,
            description='фак оф'
        )
        embed.set_image('https://i1.sndcdn.com/artworks-qUiYk9VrgWKm5TiP-2E4RoA-t500x500.jpg')
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        'удаляет все сообщения с вызовом команды'
        for i in ccommands:
            if i == message.content:
                await message.delete()

def setup(bot:commands.Bot):
    bot.add_cog(Commands(bot))
    print(f'запустился {__name__}')