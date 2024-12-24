from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from keyboards.inline.menu import back_menu_kb

router = Router()


@router.callback_query(F.data == 'cancel')
async def cancel_cb(call: types.CallbackQuery, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        await call.message.edit_text(text=_('Операция отменена!'), reply_markup=back_menu_kb())
        await state.clear()
