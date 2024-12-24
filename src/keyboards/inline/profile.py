from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def profile_kb():
    builder =  InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=_('🔙 Вернутся в меню'), callback_data='menu'))
    builder.adjust(1)
    return builder.as_markup()