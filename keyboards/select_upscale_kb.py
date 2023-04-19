from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def select_upscale_kb():
    buttons = [
        [types.InlineKeyboardButton(text='Картинка 1', callback_data='upscale_1')],
        [types.InlineKeyboardButton(text='Картинка 2', callback_data='upscale_2')],
        [types.InlineKeyboardButton(text='Картинка 3', callback_data='upscale_3')],
        [types.InlineKeyboardButton(text='Картинка 4', callback_data='upscale_4')],
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
