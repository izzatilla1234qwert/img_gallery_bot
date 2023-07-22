from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def img_btn(start_num, end_num):
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton('⬅️', callback_data='prev'),
        InlineKeyboardButton(f'{start_num}/{end_num}', callback_data='0'),
        InlineKeyboardButton('➡️', callback_data='next')
    )
    return btn