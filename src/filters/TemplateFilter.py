from aiogram.filters import BaseFilter
from aiogram.types import Message


class UpdateTemplateFilter(BaseFilter):
    async def __call__(self, msg: Message):
        text = msg.text
        if '{ordercode}' in text and '{productname}' in text and '{link}' in text and len(text) > 50 and len(text) <= 4096:
            return True
        else:
            return False