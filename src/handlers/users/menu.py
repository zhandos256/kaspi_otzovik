from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

from keyboards.inline.menu import menu_kb

router = Router()


@router.message(Command('menu'))
async def menu(msg: types.Message):
    t = [
        _('Привет!\n'),
        _('Я помогу тебе быстро сгенерировать ссылку на отзыв Kaspi с 5 ⭐ для быстрой отправки в WhatsApp\n'),
        _('⬇ Готов? Нажми на кнопку «Сгенерировать ссылку» чтобы начать!'),
    ]
    await msg.answer(text='\n'.join(t), reply_markup=menu_kb())


@router.callback_query(F.data == 'menu')
async def menu_cb(call: types.CallbackQuery):
    t = [
        _('Привет!\n'),
        _('Я помогу тебе быстро сгенерировать ссылку на отзыв Kaspi с 5 ⭐ для быстрой отправки в WhatsApp\n'),
        _('⬇ Готов? Нажми на кнопку «Сгенерировать ссылку» чтобы начать!'),
    ]
    await call.message.edit_text(text='\n'.join(t), reply_markup=menu_kb())
