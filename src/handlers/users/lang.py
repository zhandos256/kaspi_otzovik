from aiogram import F, Router, types
from aiogram.utils.i18n import gettext as _

from database.query import update_user_lang
from keyboards.inline.lang import lang_kb
from keyboards.inline.menu import back_menu_kb

router = Router()


@router.callback_query(F.data == 'lang')
async def lang_cb(call: types.CallbackQuery):
    await call.message.edit_text(text=_('Выберите язык'), reply_markup=lang_kb())


@router.callback_query(F.data == 'kk')
async def update_lang_kk(call: types.CallbackQuery):
    await update_user_lang(tg_userid=call.from_user.id, value='kk')
    await call.message.edit_text(
        text='Интерфейс тілі жаңартылды!',
        reply_markup=back_menu_kb()
    )


@router.callback_query(F.data == 'ru')
async def update_lang_ru(call: types.CallbackQuery):
    await update_user_lang(tg_userid=call.from_user.id, value='ru')
    await call.message.edit_text(
        text='Язык интерфейса обновлен!',
        reply_markup=back_menu_kb()
    )
