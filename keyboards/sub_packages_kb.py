from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def sub_packages_kb():
    buttons = [
        [types.InlineKeyboardButton(text='1 месяц — 500₽', callback_data='sub_package_month')]
    ]
    kb = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
