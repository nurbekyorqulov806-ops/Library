from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Asosiy menyu tugmalari
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Kitoblar ro'yxati")],
        [KeyboardButton(text="⭐️ Sevimlilarim")]
    ],
    resize_keyboard=True  
)