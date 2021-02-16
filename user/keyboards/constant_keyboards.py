from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Get code', callback_data='get_code'),
     InlineKeyboardButton(text='What is this', callback_data='description')]
])
