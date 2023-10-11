from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import Bot, Dispatcher, types, executor
from states.phone import Contactstate
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.default.start import get_start_keyboards

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("ведите свой номер: ")
    await Contactstate.phone.set()



@dp.message_handler(state=Contactstate.phone)
async def get_name(message: types.Message, state: FSMContext):
    await message.answer("Спасибо что ответили!\nВведите свое имя!")
    await Contactstate.name.set()
    
    
    
@dp.message_handler(state=Contactstate.name)
async def get_name(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за информацию!", reply_markup=get_start_keyboards())
    await state.finish()
    await state.reset_data()