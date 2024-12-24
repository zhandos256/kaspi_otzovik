from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=_('♻️ Сгенерировать ссылку'), callback_data='generate_url'))
    builder.add(InlineKeyboardButton(text=_('👤 Профиль'), callback_data='profile'))
    builder.add(InlineKeyboardButton(text=_('⚙️  Настройки'), callback_data='settings'))
    builder.add(InlineKeyboardButton(text=_('❔ О боте'), callback_data='about'))
    builder.adjust(1)
    return builder.as_markup()


def back_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=_('🔙 Вернутся в меню'), callback_data='menu'))
    return builder.as_markup()


def gen_again_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=_('️♻️ Генерировать повторно'), callback_data='generate_url'))
    builder.add(InlineKeyboardButton(text=_('🔙 Вернутся в меню'), callback_data='menu'))
    builder.adjust(1)
    return builder.as_markup()