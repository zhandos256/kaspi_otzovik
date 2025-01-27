import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from core.const import BOT_COMMANDS, DEBUG, BOT_TOKEN
from handlers.users import (
    cancel, 
    echo, 
    help, 
    menu, 
    review_generator, 
    start, 
    settings, 
    lang, 
    profile, 
    about
    )
from middleware.I18nMiddleware import i18n_middleware
from misc.notify import notify_admins


async def on_startup(bot: Bot):
    await notify_admins(bot=bot, text='Bot started!')


async def on_shutdown(bot: Bot):
    await notify_admins(bot=bot, text='Bot ended work!')


async def configure():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        help.router,
        menu.router,
        profile.router,
        about.router,
        lang.router,
        review_generator.router,
        settings.router,
        cancel.router,
        echo.router,
    )
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.outer_middleware.register(i18n_middleware) 
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=BOT_COMMANDS)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.exception(e)
    finally:
        await dp.storage.close()
        await bot.session.close()


def main():
    logging.basicConfig(level=logging.INFO if not DEBUG else logging.DEBUG)
    asyncio.run(configure())
