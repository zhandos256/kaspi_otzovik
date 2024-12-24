from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

router = Router()


@router.message()
async def echo(msg: types.Message, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        pass
    else:
        t = [
            _('❗ Извините, я не понимаю ваше сообщение\n'),
            _('/start - Начать работу боту'),
            _('/help - Получить справку\n'),
            _('Есть вопросы? <b>Ответим тут</b> - @clementshop'),
        ]
        await msg.answer(text='\n'.join(t))