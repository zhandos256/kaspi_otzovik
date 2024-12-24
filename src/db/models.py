from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from core.const import DEFAULT_TEMPLATE_MSG
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.today())
    tg_userid: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String(length=32), nullable=True)
    first_name: Mapped[str] = mapped_column(String(length=32), nullable=True)
    last_name: Mapped[str] = mapped_column(String(length=32), nullable=True)
    language: Mapped[str] = mapped_column(String(length=2), default='ru')
    count_used: Mapped[int] = mapped_column(Integer, default=0)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    template_msg: Mapped[str] = mapped_column(Text(length=4096), default=DEFAULT_TEMPLATE_MSG)
