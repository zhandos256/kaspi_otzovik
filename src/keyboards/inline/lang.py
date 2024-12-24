from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def lang_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='🇰🇿 Казахский', callback_data='kk'),
        InlineKeyboardButton(text='🇷🇺 Русский', callback_data='ru'),
        width=2
    )
    builder.row(
        InlineKeyboardButton(text=_('🔙 Вернутся в меню'), callback_data='menu'),
        width=1
    )
    return builder.as_markup()
