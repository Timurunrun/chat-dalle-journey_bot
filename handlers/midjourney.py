from aiogram import Router, F, types
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

import users_work

from handlers import start
from keyboards.exit_kb import exit_kb
from keyboards.select_upscale_kb import select_upscale_kb
from neuro import mid_api

router = Router()

gen = []

class MidState(StatesGroup):
    nothing = State()
    input_descripton = State()
    upscale = State()

@router.message(F.text == 'Midjourney')
async def start_input(message: Message, state: FSMContext):
    if users_work.sub_status(message.from_user.id) <= 0:
        await message.answer(
        'К сожалению, у вас ещё нет подписки на бота. Вы можете оформить её в разделе «Аккаунт»',
        reply_markup=exit_kb()
        )
    else:
        await message.answer(
            text='Выбрано: Midjourney\nВведите текстовое описание для генерации изображения (на английском):',
            reply_markup=exit_kb()
        )
        await state.set_state(start.MainState.nothing)
        await state.set_state(MidState.input_descripton)

@router.message(F.text, MidState.input_descripton)
async def generating(message: Message, state: FSMContext):
    global gen
    await message.answer(
        text='Ожидайте генерации изображения...'
    )
    
    prompt = message.text
    gen = mid_api.generate_image(prompt)
    for i in range(4):
        await message.answer_photo(photo=gen[i])
 
    await message.answer(
        text=f'Сгенерировано по запросу: «{prompt}»\nВыберите версию для улучшения или попробуйте вновь, просто введя текстовое описание:',
        reply_markup=select_upscale_kb()
    )
    await state.set_state(MidState.upscale)

@router.callback_query(Text(startswith='upscale_1'), MidState.upscale)
async def upscale_1(callback: types.CallbackQuery, state: FSMContext):
    global gen
    await callback.message.answer(
            text='Ожидайте улушения картинки...',
        )
    upscaled_pic = mid_api.upscale_image(gen[0])
    await callback.message.answer(
            text=f'Улучшенная картинка доступна по ссылке: {upscaled_pic}',
        )
    #await callback.message.answer_photo(photo=upscaled_pic)
    await callback.message.answer(
            text='Введите текстовое описание для генерации изображения (на английском):',
        )
    await state.set_state(MidState.input_descripton)

@router.callback_query(Text(startswith='upscale_2'), MidState.upscale)
async def upscale_2(callback: types.CallbackQuery, state: FSMContext):
    global gen
    await callback.message.answer(
            text='Ожидайте улушения картинки...',
        )
    upscaled_pic = mid_api.upscale_image(gen[1])
    await callback.message.answer(
            text=f'Улучшенная картинка доступна по ссылке: {upscaled_pic}',
        )
    #await callback.message.answer_photo(photo=upscaled_pic)
    await callback.message.answer(
            text='Введите текстовое описание для генерации изображения (на английском):',
        )
    await state.set_state(MidState.input_descripton)

@router.callback_query(Text(startswith='upscale_3'), MidState.upscale)
async def upscale_3(callback: types.CallbackQuery, state: FSMContext):
    global gen
    await callback.message.answer(
            text='Ожидайте улушения картинки...',
        )
    upscaled_pic = mid_api.upscale_image(gen[2])
    await callback.message.answer(
            text=f'Улучшенная картинка доступна по ссылке: {upscaled_pic}',
        )
    #await callback.message.answer_photo(photo=upscaled_pic)
    await callback.message.answer(
            text='Введите текстовое описание для генерации изображения (на английском):',
        )
    await state.set_state(MidState.input_descripton)

@router.callback_query(Text(startswith='upscale_4'), MidState.upscale)
async def upscale_4(callback: types.CallbackQuery, state: FSMContext):
    global gen
    await callback.message.answer(
            text='Ожидайте улушения картинки...',
        )
    upscaled_pic = mid_api.upscale_image(gen[3])
    await callback.message.answer(
            text=f'Улучшенная картинка доступна по ссылке: {upscaled_pic}',
        )
    #await callback.message.answer_photo(photo=upscaled_pic)
    await callback.message.answer(
            text='Введите текстовое описание для генерации изображения (на английском):',
        )
    await state.set_state(MidState.input_descripton)

