from aiogram import Router, types, F
from aiogram.utils.i18n import gettext as _

from keyboards.inline.menu import back_menu_kb

router = Router()


@router.callback_query(F.data == 'about')
async def about(call: types.CallbackQuery):
    t = [
        _('Как это работает:\n'),
        _('1) Бот автоматически подставит данные вашего заказа в готовый шаблон.\n'),
        _(' 📋 Пример:\n'),
        _(' iPhone 16, 42145214, 110145324, 77089091122\n'),
        _('2) После генерации шаблона, вы получите уникальную ссылку для отправки в WhatsApp.\n'),
        _('3) Просто нажмите на ссылку, и ваш шаблон будет отправлен в WhatsApp.\n'),
        _('👉 Нажмите /start, чтобы начать.'),
        _('❓ Есть вопросы? Напишите — @clementshop\n'),
    ]
    await call.message.edit_text(text='\n'.join(t), reply_markup=back_menu_kb())