from aiogram import F
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from router import router
from loader import db


@router.message(F.text == "📝 Kategoriyalar")
async def show_categories(message: Message):
    categories = db.get_categories()  # [ { "id": 1, "name": "Lavash" }, { "id": 1, "name": "Lavash" }, { "id": 1, "name": "Lavash" } ]

    keyboard = InlineKeyboardBuilder()
    for category in categories:
        keyboard.button(text=category.get("name"), callback_data=f"category:{category.get('id')}")  # category:1, category:2
    keyboard.adjust(2)

    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncJ2Dx_886-_9WimG2j5cwLPgVLGr_kTRzA&s",
        caption="Bizda quyidagi kategoriyalar mavjud",
        reply_markup=keyboard.as_markup(),
    )
