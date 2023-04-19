from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def buy_sub_kb():
    buttons = [
        [types.InlineKeyboardButton(text='Купить подписку', callback_data='buy_sub')]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
