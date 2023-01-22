import disnake
from disnake.ext import commands

class GayTest(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    class Gay(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=10.0)
            self.flag = False

        @disnake.ui.button(label='да', style=disnake.ButtonStyle.red)
        async def gayda(self, button: disnake.ui.Button, ctx):
            await ctx.message.delete()
            await ctx.response.send_message('на костёр таких как ты')

        @disnake.ui.button(label='нет', style=disnake.ButtonStyle.green)
        async def gaynet(self, button: disnake.ui.Button, ctx):
            await ctx.message.delete()
            await ctx.response.send_message('всё правильно!')

    @commands.command()
    async def test(self, ctx):
        global msg
        msg = await ctx.send('ты поддерживаешь LGBTQ+?', view=GayTest.Gay())
#gay test


def setup(bot:commands.Bot):
    bot.add_cog(GayTest(bot))
    print(f'запустился {__name__}')
#setup cog