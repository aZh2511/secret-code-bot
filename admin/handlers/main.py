from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from database.db_commands import database
from config import IP_WHITELIST
from ..state import Admin
from ..keyboards import main_menu


@dp.message_handler(lambda message: message.from_user.id in IP_WHITELIST,
                    commands=['admin'], state='*')
async def admin_panel(message: types.Message, state: FSMContext):
    """Process /admin, send admin-panel."""
    await state.finish()
    text = 'Welcome to the admin panel. Choose what you want to do:'
    await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=main_menu)


@dp.callback_query_handler(lambda c: c.data == 'set_code')
async def set_code(message: types.Message):
    """Request new secret-code input."""
    current_code = await database.get_code()
    text = f'Current_code: {current_code}\n\nSend me code to be set please:'
    await bot.send_message(message.from_user.id, text)
    await Admin.SetCode.set()


@dp.message_handler(content_types=['text'], state=Admin.SetCode)
async def update_code(message: types.Message, state: FSMContext):
    """Update secret-code in DB."""
    new_code = message.text
    await database.set_code(new_code)
    text = 'Your code was successfully updated'
    await bot.send_message(message.from_user.id, text)
    await state.finish()


