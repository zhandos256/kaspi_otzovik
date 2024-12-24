import urllib.parse

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.markdown import hlink
from aiogram.utils.i18n import gettext as _

from db.query import (
    get_template_msg, 
    update_template_msg, 
    reset_template_msg_default,
    increment_counter
    )
from filters.CustomFilter import TextFilter
from filters.TemplateFilter import UpdateTemplateFilter
from keyboards.inline.cance import cancel_kb
from keyboards.inline.menu import gen_again_kb, back_menu_kb
from keyboards.inline.template import template_kb

router = Router()


class Template(StatesGroup):
    url = State()


@router.callback_query(F.data == 'generate_url')
async def generate_url_handler(call: types.CallbackQuery, state: FSMContext):
    t = [
        _('Отправьте мне следующие данные:\n'),
        _('<b><u>Имя Товара</u></b>, <b><u>Номер Заказа</u></b>, <b><u>Артикул Продукта</u></b>, <b><u>Номер Телефона</u></b>\n'),
        _('📋 Пример:\n'),
        _('<b>iPhone 16, 42145214, 110145324, 77089091122</b>'),
    ]
    await call.message.edit_text(text='\n'.join(t), reply_markup=cancel_kb())
    await state.set_state(Template.url)


@router.message(Template.url, F.text, TextFilter())
async def url_state_handler(msg: types.Message, state: FSMContext):
    m = msg.text.split(',')
    tm = await get_template_msg(tg_userid=msg.from_user.id)
    link = f"https://kaspi.kz/shop/review/productreview?orderCode={m[1].strip()}&productCode={m[2].strip()}&rating=5"
    end_m = tm.format(productname=m[0].title().strip(), ordercode=m[1].strip(), productcode=m[2].strip(), link=link.strip())
    await msg.answer(text=end_m)
    encoded_msg = urllib.parse.quote(end_m)
    w_link = hlink(title=_('✉️ Отпавить шаблон в WhatsApp'), url=f'https://wa.me/{m[3].strip().replace("+", "")}?text={encoded_msg}')
    await msg.answer(text=f'<b><u>{w_link}</u></b>', reply_markup=gen_again_kb(), disable_web_page_preview=True)
    await state.clear()
    await increment_counter(tg_userid=msg.from_user.id)


@router.message(Template.url)
async def invalid_url_state_handler(msg: types.Message):
    t = [
        _('❗ Не Правильный Ввод, Попробуйте Снова!\n'),
        _('Отправьте мне следующие данные:\n'),
        _('<b><u>Имя Товара</u></b>'),
        _('<b><u>Номер Заказа</u></b>'),
        _('<b><u>Артикул Продукта</u></b>'),
        _('<b><u>Номер Телефона</u></b>\n'),
        _('📋 Пример:\n'),
        _('<b><u>iPhone 16, 42145214, 110145324, 77089091122</u></b>'),
    ]
    await msg.answer(text='\n'.join(t), reply_markup=cancel_kb())


@router.callback_query(F.data == 'template_msg')
async def template_msg(call: types.CallbackQuery):
    m = await get_template_msg(tg_userid=call.from_user.id)
    await call.message.edit_text(text=m, reply_markup=template_kb())


class EditTemplate(StatesGroup):
    text = State()

@router.callback_query(F.data == 'edit_template')
async def edit_template_msg(call: types.CallbackQuery, state: FSMContext):
    t = [
        _('Отправьте ваш шаблонный текст одним сообщением.\n'),
        _('В шаблоне должны присутствовать следующие данные:\n'),
        _('<b><u>{ordercode}</u></b> — номер заказа'),
        _('<b><u>{productname}</u></b> — имя товара\n'),
        _('<b><u>{link}</u></b> — ссылка на отзыв\n'),
        _('Также шаблон должен содержать не меньше <b><u>50</u></b> и не больше <b><u>4096</u></b> символов!\n'),
        _('Пример:\n'),
        _('------------------------'),
        _('Здравствуйте!\n'),
        _('Ваш заказ № <b><u>{ordercode}</u></b>'),
        _('Имя товара: <b><u>{productname}</u></b>\n'),
        _('Будем благодарны, если вы оставите отзыв c 5 ⭐\n'),
        _('Ссылка на отзыв: <b><u>{link}</u></b>\n'),
        _('С уважением,'),
        _('Каспи магазин'),
        _('------------------------'),
    ]
    await call.message.edit_text(text='\n'.join(t), reply_markup=cancel_kb())
    await state.set_state(EditTemplate.text)


@router.message(EditTemplate.text, F.text, UpdateTemplateFilter())
async def edit_template_state_handler(msg: types.Message, state: FSMContext):
    await update_template_msg(tg_userid=msg.from_user.id, text=msg.text)
    await msg.answer( text=_('✅ Шаблон успешно обновлен!'), reply_markup=back_menu_kb())
    await state.clear()


@router.message(EditTemplate.text)
async def invalid_update_state(msg: types.Message):
    t = [
        _('Не верный шаблонный текст, попробуйте заново!\n'),
        _('В шаблоне должны быть <b><u>{ordercode} {productname} {link}</u></b>\n'),
        _('Также шаблон должен содержать не меньше <b><u>50</u></b> и не больше <b><u>4096</u></b> символов'),
    ]
    await msg.answer(text='\n'.join(t), reply_markup=cancel_kb())


@router.callback_query(F.data == 'reset_template_default')
async def reset_template_default(call: types.CallbackQuery):
    await reset_template_msg_default(tg_userid=call.from_user.id)
    await call.message.edit_text(text=_('✅ Шаблон сброшен по умолчанию!'), reply_markup=back_menu_kb())