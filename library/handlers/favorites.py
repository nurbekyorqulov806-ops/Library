from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database import cursor, conn


router = Router()

@router.callback_query(F.data.startswith("fav:"))
async def add_fav(call: CallbackQuery):
    _, key, title = call.data.split(":", 2)
    user_id = call.from_user.id
    
    cursor.execute("INSERT INTO favorites VALUES (?, ?, ?)", (user_id, key, title))
    conn.commit()
    await call.answer("⭐️ Saqlandi!")

# Tugma orqali bosganda ham ishlaydigan qilish
@router.message(F.text.in_({"⭐️ Sevimlilarim", "/favorites"}))
async def show_favs(message: Message):
    user_id = message.from_user.id
    cursor.execute("SELECT title FROM favorites WHERE user_id=?", (user_id,))
    data = cursor.fetchall()
    
    if not data:
        await message.answer("Sizda hali sevimli kitoblar yo‘q.")
        return
        
    text = "⭐️ Sevimlilar:\n\n" + "\n".join([f"📚 {d[0]}" for d in data])
    await message.answer(text)