from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.reply import main_menu


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("📚 Kutubxona botiga xush kelibsiz!",reply_markup=main_menu)



