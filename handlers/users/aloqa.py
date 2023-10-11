from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start import get_start_keyboards

from loader import dp

@dp.message_handler(text="Aloqa")
async def about(message: types.Message):
    photo="https://warm1069.com/wp-content/uploads/2020/02/bigstock-Customer-Service-Agents-In-A-C-6555094-scaled-1.jpg"
    msg = """
    Kontaktlar
    Call-центр

    +998 71-203-12-12
    +998 71-203-55-55
    Yetkazib berish telefon raqamlar:

    Toshkent
    +998 71-203-12-12
    Namangan
    +998 78-147-12-12
    Farg`ona
    +998 73-249-12-12
    Qo`qon
    +998 73-542-78-78
    Andijon
    +998 74-224-12-12
    Samarqand
    +998 78-129-16-16
    Qarshi
    +998 78-129-17-17
    """
    await message.answer_photo(photo=photo, caption=msg)