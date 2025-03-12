from aiogram import Bot, types


async def set_bot_commands(bot: Bot):
    bot_commands = [
        types.BotCommand(command='/start', description='start command'),
        types.BotCommand(command='/help', description='help command'),
    ]
    await bot.set_my_commands(bot_commands)