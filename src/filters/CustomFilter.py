from typing import Union

from aiogram import types
from aiogram.filters import BaseFilter


class TextFilter(BaseFilter):
    async def __call__(self, obj: Union[types.Message, types.CallbackQuery]):
        if isinstance(obj, types.Message):
            msg = obj.text
            if msg:
                return True if ',' in msg and len(msg.split(',')) > 3 else False
        elif isinstance(obj, types.CallbackQuery):
            msg = obj.message.text
            if msg:
                return True if ',' in msg and len(msg.split(',')) > 3 else False