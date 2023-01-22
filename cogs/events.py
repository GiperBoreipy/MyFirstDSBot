import disnake
import datetime
from disnake.ext import commands

badwords = ['пон']

class Events(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        'когда бот загружен, в консоль пишется print'
        print('гоу', self.bot.user)

    @commands.Cog.listener()
    async def on_message(self, message):
        'таймаут за слово пон'
        new_message_content = []
        for content in message.content.lower().split():
            if len(content) > 1:
                for i in content:
                    if i.isalpha() == True:
                        new_message_content.append(i)
                for q in badwords:
                    if ''.join(new_message_content) == q:
                        time = datetime.datetime.now() + datetime.timedelta(minutes=1)
                        member = message.author
                        await member.timeout(reason='антипон', until=time)




def setup(bot:commands.Bot):
    bot.add_cog(Events(bot))
    print(f'запустился {__name__}')
