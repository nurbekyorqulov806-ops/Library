from aiogram import Router, F
from aiogram.types import Message
from config import ADMIN_ID

router = Router()

@router.message(F.text == "/admin")
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Ruxsat yo'q")
    await message.answer("👑 Admin panelga xush kelibsiz!")
