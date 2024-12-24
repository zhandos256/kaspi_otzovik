from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def cancel_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=_('⛔️ отменить операцию?'), callback_data='cancel'))
    return builder.as_markup()
