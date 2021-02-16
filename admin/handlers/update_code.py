from aiogram import types
from aiogram.dispatcher import FSMContext

from database.db_commands import database
from loader import dp, bot
from ..state import Admin


@dp.callback_query_handler(lambda c: c.data == 'set_code')
async def set_code(message: types.Message):
    """Request new code."""
    current_code = await database.get_code()
    text = f'Current_code: {current_code}\n\nSend me code to be set please:'
    await bot.send_message(message.from_user.id, text)
    await Admin.SetCode.set()


@dp.message_handler(content_types=['text'], state=Admin.SetCode)
async def update_code(message: types.Message, state: FSMContext):
    """Update secret_code in DB."""
    new_code = message.text
    await database.set_code(new_code)
    text = 'Your code was successfully updated'
    await bot.send_message(message.from_user.id, text)
    await state.finish()
