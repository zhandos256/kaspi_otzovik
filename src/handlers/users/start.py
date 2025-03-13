from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

from database.query import register_user
from keyboards.inline.menu import menu_kb

router = Router()


@router.message(Command('start'))
async def start(msg: types.Message):
    await register_user(
        tg_userid=msg.from_user.id,
        username=msg.from_user.username,
        first_name=msg.from_user.first_name,
        last_name=msg.from_user.last_name
    )
    temp_msg = (
        _('Привет!\n'),
        _('Я помогу тебе быстро сгенерировать ссылку на отзыв Kaspi с 5 ⭐ для быстрой отправки в WhatsApp\n'),
        _('⬇ Готов? Нажми на кнопку «Сгенерировать ссылку» чтобы начать!'),
    )
    await msg.answer(text='\n'.join(temp_msg), reply_markup=menu_kb())
