import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, add, list_ads
from logger import logger


async def main():
    logger.info("🚀 Запуск Telegram-бота...")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(start.router, add.router, list_ads.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
