from aiogram import Router, F
from aiogram.types import Message

from services.openlibrary import search_books
from keyboards.inline import book_buttons



router = Router()

@router.message(F.text)
async def search(message: Message):
    data = await search_books(message.text)
    books = data.get("docs", [])[:3]

    if not books:
        await message.answer("❌ Topilmadi")
        return

    for b in books:
        key = b.get("key")
        title = b.get("title", "Noma'lum")
        author = ", ".join(b.get("author_name", ["Noma'lum"]))
        year = b.get("first_publish_year", "Noma'lum")

        text = f"📚 {title}\n✍️ {author}\n📅 {year}"

        await message.answer(
            text,
            reply_markup=book_buttons(key, title)
        )

