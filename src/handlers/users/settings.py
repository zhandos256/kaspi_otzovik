from aiogram import F, Router, types
from aiogram.utils.i18n import gettext as _

from keyboards.inline.settings import settings_kb

router = Router()


@router.callback_query(F.data == 'settings')
async def settings(call: types.CallbackQuery):
    await call.message.edit_text(text=_('Настройки'), reply_markup=settings_kb())
