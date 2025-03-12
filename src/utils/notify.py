import asyncio
import logging

from aiogram import Bot

from database.query import get_admins


async def notify_admins(bot: Bot, text: str):
    admins = await get_admins()
    if admins:
        for admin in admins:
            try:
                await bot.send_message(chat_id=admin.tg_userid, text=text)
                await asyncio.sleep(0.05)
            except Exception as e:
                logging.exception(e)
