from aiogram import Router, F
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.start_kb import select_ai_kb
from handlers import chatgpt, dalle, midjourney, account
import users_work

router = Router()

class MainState(StatesGroup):
    nothing = State()
    select_ai = State()

@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    if users_work.is_user_exist(message.from_user.id) == False:
        users_work.create_new_user(message.from_user.id)
    
    await message.answer(
        'Здравствуйте! Выберите нейросеть, с которой будете работать.',
        reply_markup=select_ai_kb()
    )
    
    await state.set_state(MainState.select_ai)
    await state.set_state(dalle.DalleState.nothing)
    await state.set_state(chatgpt.ChatState.nothing)
    await state.set_state(midjourney.MidState.nothing)
    await state.set_state(account.AccountState.nothing)


@router.message(F.text == 'Выход')
async def exit(message: Message, state: FSMContext):
    await message.answer(
        'Здравствуйте! Выберите нейросеть, с которой будете работать.',
        reply_markup=select_ai_kb()
    )
    
    await state.set_state(MainState.select_ai)
    await state.set_state(dalle.DalleState.nothing)
    await state.set_state(chatgpt.ChatState.nothing)
    await state.set_state(midjourney.MidState.nothing)
    await state.set_state(account.AccountState.nothing)

  
