from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def template_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=_('➕ Обновить шаблонный текст'), callback_data='edit_template'))
    builder.add(InlineKeyboardButton(text=_('➕ Сбросить шаблон по умолчанию'), callback_data='reset_template_default'))
    builder.add(InlineKeyboardButton(text=_('🔙 Вернутся в меню'), callback_data='menu'))
    builder.adjust(1)
    return builder.as_markup()
