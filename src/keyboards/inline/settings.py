from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def settings_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=_('🏷 Шаблонный текст'), callback_data='template_msg'),
        InlineKeyboardButton(text=_('🌎 Язык интерфейса'), callback_data='lang'),
        width=2,
    )
    builder.row(InlineKeyboardButton(text=_('🔙 Вернутся в меню'), callback_data='menu'), width=1)
    return builder.as_markup()
