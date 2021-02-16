from aiogram import types

from database.db_commands import database
from loader import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'get_users')
async def set_code(message: types.Message):
    """Send a list of users."""

    users = await database.get_users()
    amount_of_users = await database.count_users()
    text = f'Users: {amount_of_users}'
    await bot.send_message(message.from_user.id, text)
    await bot.send_message(message.from_user.id, users)
