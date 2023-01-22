import disnake
from disnake.ext import commands
from TOKEN import TOKEN
#Ru: импорт нужных библиотек

bot = commands.Bot(
    command_prefix='!',
    intents= disnake.Intents.all(),
    activity=disnake.Game('трахает'),
    status=disnake.Status('online'),
    test_guilds=[1]
)
#Ru: настройки бота - префикс=!, подключаем интенты, играет в 'трахает', статус=онлайн, тестсервер= чтобы быстрее загружылись слэшконмады

bot.remove_command('help')
#Ru: удаляем команду help

bot.load_extension('cogs.slash_commands')
bot.load_extension('cogs.commands')
bot.load_extension('cogs.events')
bot.load_extension('cogs.gaytest')
#Ru: загружаем коги

if __name__ == '__main__':
    bot.run(TOKEN)

#start