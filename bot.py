import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, chatgpt, dalle, midjourney, account
from decouple import config

# Запуск бота
async def main():
    tg_token = config('tg_token',default='')
    bot = Bot(token=tg_token)
    
    # storage = MemoryStorage()
    dp = Dispatcher()

    dp.include_routers(start.router, chatgpt.router, dalle.router, midjourney.router, account.router)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
