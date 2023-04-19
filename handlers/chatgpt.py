from aiogram import Router, F
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from handlers import start
from neuro import chatgpt_api
from keyboards.exit_kb import exit_kb
import users_work

router = Router()

class ChatState(StatesGroup):
    nothing = State()
    input_descripton = State()

messages = []
tokens = 0

@router.message(F.text == 'ChatGPT')
async def start_input(message: Message, state: FSMContext):
    if users_work.sub_status(message.from_user.id) <= 0:
        await message.answer(
        'К сожалению, у вас ещё нет подписки на бота. Вы можете оформить её в разделе «Аккаунт»',
        reply_markup=exit_kb()
        )
    else:
        await message.answer(
            text='Выбрано: ChatGPT\nВведите запрос:',
            reply_markup=exit_kb()
        )
        await state.set_state(start.MainState.nothing)
        await state.set_state(ChatState.input_descripton)

@router.message(F.text, ChatState.input_descripton)
async def generating(message: Message, state: FSMContext):
    await message.answer(
        text='Ожидайте ответа...'
        )
    gen = chatgpt_api.generate_answer(message.text, message.from_user.id)
    await message.answer(text=gen, reply_markup=exit_kb())
