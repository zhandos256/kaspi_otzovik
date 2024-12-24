import asyncio
import logging

from aiogram import Bot
from sqlalchemy import select

from db.config import async_session_maker
from db.models import User


async def notify_admins(bot: Bot, text: str):
    async with async_session_maker() as session:
        query = select(User).filter_by(is_admin=True)
        res = await session.execute(query)
        admins = res.scalars().all()
        if admins:
            for admin in admins:
                try:
                    await bot.send_message(chat_id=admin.tg_userid, text=text)
                    await asyncio.sleep(0.05)
                except Exception as e:
                    logging.exception(e)
