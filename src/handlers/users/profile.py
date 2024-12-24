from aiogram import Router, types, F
from aiogram.utils.i18n import gettext as _

from db.query import get_user_lang, get_count
from keyboards.inline.profile import profile_kb

router = Router()


@router.callback_query(F.data == 'profile')
async def profile(call: types.CallbackQuery):
    lang = await get_user_lang(tg_userid=call.from_user.id)
    count = await get_count(tg_userid=call.from_user.id)
    template_msg = [
        _('👤 Мой профиль\n'),
        f'ID: {call.from_user.id}',
        f'Username: {call.from_user.username}',
        f'Имя: {call.from_user.first_name}',
        f'Фамилия: {call.from_user.last_name}',
        f'Язык интерфейса: {lang}',
        f'Колличество генерации: {count}',
    ]
    await call.message.edit_text(
        text='\n'.join(template_msg),
        reply_markup=profile_kb()
    )