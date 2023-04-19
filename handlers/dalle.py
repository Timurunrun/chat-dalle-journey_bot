from aiogram import Router, F
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

import openai

import users_work

from handlers import start
from keyboards.exit_kb import exit_kb
from neuro import dalle_api

router = Router()

class DalleState(StatesGroup):
    nothing = State()
    input_descripton = State()

openai.api_key = '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'

@router.message(F.text == 'DALLE-2')
async def start_input(message: Message, state: FSMContext):
    if users_work.sub_status(message.from_user.id) <= 0:
        await message.answer(
        'К сожалению, у вас ещё нет подписки на бота. Вы можете оформить её в разделе «Аккаунт»',
        reply_markup=exit_kb()
        )
    else:
        await message.answer(
            text='Выбрано: DALLE\nВведите текстовое описание для генерации изображения:',
            reply_markup=exit_kb()
        )
        await state.set_state(start.MainState.nothing)
        await state.set_state(DalleState.input_descripton)

@router.message(F.text, DalleState.input_descripton)
async def generating(message: Message, state: FSMContext):
    await message.answer(
        text='Ожидайте генерации изображения...',
    )
    
    gen = dalle_api.generate_image(message.text)
    await message.answer_photo(photo=gen, caption=f'Сгенерировано по запросу: «{message.text}»')
    
    await message.answer(
        text='Введите текстовое описание для генерации изображения:',
        reply_markup=exit_kb()
    )
