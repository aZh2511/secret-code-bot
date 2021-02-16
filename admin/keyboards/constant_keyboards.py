from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Update code', callback_data='set_code'),
     InlineKeyboardButton(text='Get users', callback_data='get_users')],
    [InlineKeyboardButton(text='Manage texts', callback_data='manage_texts')]
])


manage_texts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='/start', callback_data='text_start'),
     InlineKeyboardButton(text='Get code', callback_data='text_get_code')],
    [InlineKeyboardButton(text='What is this', callback_data='text_what_is_this'),
     InlineKeyboardButton(text='/getdrops', callback_data='text_getdrops')],
])
