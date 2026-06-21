from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def book_buttons(key, title):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📖 Batafsil", callback_data=f"book:{key}")
        ],
        [
            InlineKeyboardButton(text="⭐ Sevimli", callback_data=f"fav:{key}:{title}")
        ]
    ])