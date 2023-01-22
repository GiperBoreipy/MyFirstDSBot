import disnake
from disnake.ext import commands
from random import randint

class SlashCommands(commands.Cog):
    def __init__(self, bot = commands.Bot):
        self.bot = bot

    @commands.slash_command(description='трахать')
    async def clear(self, ctx, amount: int):
        'очищает чат на выбранное колличество сообщений'
        await ctx.response.send_message(f"трахнули {amount} сообщения")
        await ctx.channel.purge(limit=amount)

    @commands.slash_command(description='шлёпок')
    async def ku(self, ctx, user: disnake.User):
        'выбираешь пользователя сервера, и отправляешь ему ку'
        await ctx.response.send_message(f'{user.mention} ку')

    @commands.slash_command(name='рандом', description='угадайка)')
    async def randomnumber(self, ctx, value: int):
        'угадать рандомное число в диапазоне от 0 до 10'
        x = randint(1,10)
        await ctx.response.send_message(f'я загадал число {x}')
        if value == x:
            await ctx.send('ты угадал ✅✅✅✅👍👍а')
        else:
            await ctx.send('не угадал')

def setup(bot:commands.Bot):
    bot.add_cog(SlashCommands(bot))
    print(f'запустился {__name__}')