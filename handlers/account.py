from aiogram import Bot, Router, F, types
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from decouple import config

from handlers import start

import users_work

from keyboards.exit_kb import exit_kb
from keyboards.sub_kb import buy_sub_kb
from keyboards.sub_packages_kb import sub_packages_kb

router = Router()

class AccountState(StatesGroup):
    nothing = State()
    summary = State()
    select_package = State()

tg_token = config('tg_token',default='')
bot = Bot(token=tg_token)

PAYMENTS_TOKEN = '1902332405:LIVE:638148241432483531'

def days(value):
    words = ['день', 'дня', 'дней']

    if all((value % 10 == 1, value % 100 != 11)):
        return words[0]
    elif all((2 <= value % 10 <= 4,
            any((value % 100 < 10, value % 100 >= 20)))):
        return words[1]
    return words[2]

@router.message(F.text == 'Аккаунт')
async def overview(message: Message, state: FSMContext):
    await message.answer(
        'Ваш аккаунт:',
        reply_markup=exit_kb()
    )
    
    if users_work.sub_status(message.from_user.id) <= 0:
        await message.answer(
        'Статус подписки: неактивна',
        reply_markup=buy_sub_kb()
        )
    else:
        remaining=users_work.sub_status(message.from_user.id)
        await message.answer(
        f'Статус подписки: активна (будет действовать ещё {remaining} {days(remaining)})',
        )
    
    await state.set_state(start.MainState.nothing)
    await state.set_state(AccountState.summary)

@router.callback_query(Text(startswith='buy_sub'), AccountState.summary)
async def buy(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Подписка\n\nОформление подписки позволит вам пользоваться всеми функциями бота без ограничений.\n\nВыберите подходящий вам вариант подписки.',
        reply_markup=sub_packages_kb()
    )

@router.callback_query(Text(startswith='sub_package_month'), AccountState.summary)
async def buy_for_month(callback: types.CallbackQuery, state: FSMContext):
    PRICE = types.LabeledPrice(label='Подписка на 1 месяц', amount=500*100)
    await bot.send_invoice(callback.message.chat.id,
                           title='Подписка на 1 месяц',
                           description='Активация подписки на бота на 1 месяц',
                           provider_token=PAYMENTS_TOKEN,
                           currency='rub',
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter='one-month-subscription',
                           payload='one-month')

@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

@router.message(F.successful_payment)
async def successful_payment(message: types.Message):
    if (message.successful_payment.total_amount // 100) == 500:
        users_work.sub_renewal(message.chat.id, 31)
