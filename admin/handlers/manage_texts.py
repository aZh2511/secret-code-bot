from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from ..state import Admin
from database.db_commands import database
from ..keyboards import manage_texts


@dp.callback_query_handler(lambda c: c.data == "manage_texts")
async def texts_main(call: types.CallbackQuery):
    """Send current text and buttons to choose which text to change."""

    text = f"""Current texts:
/start - {await database.get_text('text_start')}

"What is this" - {await database.get_text('text_what_is_this')}

"Get code" - {await database.get_text('text_get_code')}

/getdrops - {await database.get_text('text_getdrops')}

Choose which text you want to change:
"""
    await call.message.answer(text, reply_markup=manage_texts)
    await Admin.ManageTexts.set()


@dp.callback_query_handler(lambda c: c.data in ['text_start', 'text_get_code', 'text_what_is_this', 'text_getdrops'],
                           state=Admin.ManageTexts)
async def change_text(call: types.CallbackQuery, state: FSMContext):
    """Update text in db."""
    await state.update_data(button=call.data)

    text = 'Send me new text for button.'
    await call.message.answer(text)
    await Admin.UpdateButton.set()


@dp.message_handler(state=Admin.UpdateButton)
async def update_button(message: types.Message, state: FSMContext):
    """Confirm successful change."""
    button = await state.get_data('button')
    await database.set_text(message.text, button['button'])
    text = 'Changed!'
    await bot.send_message(message.chat.id, text)



