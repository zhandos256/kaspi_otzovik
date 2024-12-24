from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

from keyboards.inline.menu import back_menu_kb

router = Router()


@router.message(Command('help'))
async def help(msg: types.Message):
    t = [
        _('/start - Начать работу бота\n'),
        _('Есть вопросы? <b>Ответим тут</b> - @clementshop'),
    ]
    await msg.answer(text='\n'.join(t), reply_markup=back_menu_kb())