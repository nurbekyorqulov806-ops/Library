from aiogram.types import CallbackQuery
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from router import router
from loader import db


# "category:1"
# "category:3"
# "category:2"
# "category:5"

@router.callback_query(lambda call: "category" in call.data)
async def show_category_products(call: CallbackQuery):
    category_id = int(call.data.split(":")[-1])
    products = db.get_category_product(category_id=category_id)

    keyboard = InlineKeyboardBuilder()
    for product in products:
        keyboard.button(text=product.get("name"), callback_data=f"product:{product.get('id')}")
    keyboard.adjust(2)

    await call.message.answer(
        text="Bu kategoriya bo'yicha ushbu maxsulotlar mavjud",
        reply_markup=keyboard.as_markup(),
    )
