from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start import get_start_keyboards

from loader import dp

@dp.message_handler(text="Помогите!🆘")
async def about(message: types.Message):
    await message.answer("Наш контакт для вопросов!")
    await message.answer("https://t.me/themuroddarkprince")