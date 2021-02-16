from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from database.db_commands import database
from ..keyboards import main_menu
from config import GROUP_ID, GROUP_LINK


@dp.message_handler(commands=['start'], state='*')
async def starting(message: types.Message, state: FSMContext):
    """Process /start command, send message with 2 options: get code and description."""
    await database.add_new_user()
    user = types.User.get_current()
    data = await database.get_whitelist()
    await state.finish()

    if user.id in data:
        text = f'Glad to see you, {user.full_name}!\n' + await database.get_text('text_start')
        await bot.send_message(message.from_user.id, text, reply_markup=main_menu)
    else:
        text = f'You must be a member of {GROUP_LINK} to get code. Join the group and follow instructions in the ' \
               f'pinned message.'
        await bot.send_message(message.chat.id, text)


@dp.message_handler(lambda msg: msg.chat.id == GROUP_ID, commands=['getdrops'])
async def add_to_whitelist(message: types.Message):
    """Process /getdrops. Add users to whitelist."""
    await database.add_user_whitelist()
    text = await database.get_text('text_getdrops')

    await message.answer(text)


@dp.callback_query_handler(lambda c: c.data in ['get_code'])
async def send_description(call: types.CallbackQuery):
    """Send secret-code."""
    code = await database.get_code()
    text = f'Your secret code is {code}\n' + await database.get_text('text_get_code')
    await call.message.answer(text)


@dp.callback_query_handler(lambda c: c.data in ['description'])
async def send_description(call: types.CallbackQuery):
    """Send description."""
    text = await database.get_text('text_what_is_this')
    await call.message.answer(text)
