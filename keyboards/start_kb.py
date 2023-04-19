from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def select_ai_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='ChatGPT')
    kb.button(text='DALLE-2')
    kb.button(text='Midjourney')
    kb.button(text='Аккаунт')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard=True)
