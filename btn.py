from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def translate_langs_btn():
    btn = InlineKeyboardMarkup(row_width=2)

    btn.add(
        InlineKeyboardButton(
            text='ru', callback_data='lang:ru'
        ),
        InlineKeyboardButton(
            text='uz', callback_data='lang:uz'
        ),
        InlineKeyboardButton(
            text='ar', callback_data='lang:ar'
        )
    )
    return btn
