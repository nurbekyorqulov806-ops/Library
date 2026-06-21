from aiogram.types import CallbackQuery, InlineKeyboardButton, FSInputFile
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from router import router
from loader import db

# "product:1"
# "product:3"
# "product:2"

@router.callback_query(lambda call: "product" in call.data)
async def send_product_data(call: CallbackQuery):
    product_id = int(call.data.split(":")[-1])
    product = db.get_product(product_id=product_id)

    text = f"{product.get('name')}\n\n"
    text += f"{product.get('description')}\n\n"
    text += f"{product.get('price')} UZS"

    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="-", callback_data="..."),
        InlineKeyboardButton(text="1", callback_data="..."),
        InlineKeyboardButton(text="+", callback_data="..."),
    )
    keyboard.row(
        InlineKeyboardButton(text="🛒 Savatga qo'shish", callback_data="..."),
    )

    photo = FSInputFile(path=product.get('image_path'))
    await call.message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=keyboard.as_markup(),
    )
