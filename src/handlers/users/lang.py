from aiogram import F, Router, types
from aiogram.utils.i18n import gettext as _

from database.query import update_user_lang
from keyboards.inline.lang import lang_kb
from keyboards.inline.menu import back_menu_kb

router = Router()

lang_messages = {
    "kk": "Интерфейс тілі жаңартылды!",
    "ru": "Язык интерфейса обновлен!"
}

@router.callback_query(F.data == 'lang')
async def lang_cb(call: types.CallbackQuery):
    await call.message.edit_text(text=_('Выберите язык'), reply_markup=lang_kb())


@router.callback_query(F.data.in_(['kk', 'ru']))
async def update_lang(call: types.CallbackQuery):
    await update_user_lang(tg_userid=call.from_user.id, value=call.data)
    await call.message.edit_text(
        text=lang_messages[call.data],
        reply_markup=back_menu_kb()
    )