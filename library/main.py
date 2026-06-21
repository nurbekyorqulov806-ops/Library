import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
import database

async def main():
    await database.init()


bot = Bot(TOKEN)
dp = Dispatcher()




from handlers.start import router as start_router
from handlers.search import router as search_router
from handlers.favorites import router as favorites_router
from handlers.admin import router as admin_router

dp.include_router(start_router)
dp.include_router(search_router)
dp.include_router(favorites_router)
dp.include_router(admin_router)




async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())