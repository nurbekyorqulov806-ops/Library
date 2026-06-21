from aiogram import types
from aiogram.filters.command import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from pymysql import IntegrityError

from router import router
from loader import db


@router.message(CommandStart())
async def start(message: types.Message):

    text = "Assalomu alaykum !\n"
    text += "Online magazinimizga xush kelibsiz !\n"

    try:
        db.add_user(
            telegram_id=message.from_user.id,
            fullname=message.from_user.full_name,
        )
        text += "Muvaffaqiyatli ro'yxatga olindingiz"
    except IntegrityError:
        text += "Qaytganingizdan xursandmiz"

    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="📝 Kategoriyalar")
    keyboard.adjust(1)

    await message.answer(
        text=text,
        reply_markup=keyboard.as_markup(resize_keyboard=True)
    )
