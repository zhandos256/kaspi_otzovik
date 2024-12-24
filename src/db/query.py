from typing import Optional

from sqlalchemy import select

from core.const import DEFAULT_TEMPLATE_MSG
from db.config import async_session_maker
from db.models import User


async def register_user(
    tg_userid: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        exist_user = res.scalar_one_or_none()
        if exist_user:
            return
        new_user = User(
            tg_userid=tg_userid,
            username=username if username else '-',
            first_name=first_name if username else '-',
            last_name=last_name if username else '-',
        )
        session.add(new_user)
        await session.commit()


async def get_user_lang(tg_userid: int):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        return user.language if user else None


async def update_user_lang(tg_userid: int, value: str):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        if user:
            user.language = value
            await session.commit()


async def get_template_msg(tg_userid: int):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        return user.template_msg


async def update_template_msg(tg_userid: int, text: str):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        user.template_msg = text
        await session.commit()
    

async def reset_template_msg_default(tg_userid: int):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        user.template_msg = DEFAULT_TEMPLATE_MSG
        await session.commit()


async def increment_counter(tg_userid: int):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        user.count_used += 1
        await session.commit()


async def get_count(tg_userid: int):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        res = await session.execute(query)
        user = res.scalar_one_or_none()
        return user.count_used