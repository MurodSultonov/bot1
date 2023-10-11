from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import get_menu_keyboards
from keyboards.default.start import get_start_keyboards
from keyboards.default.setlar import get_sets_keyboards
from keyboards.default.lavash import get_lavash_keyboards
from keyboards.default.shaurma import get_shaurma_keyboards
from keyboards.default.burger import get_burger_keyboards
from keyboards.default.htdg import get_ht_keyboards
from keyboards.default.napitka import get_suv_keyboards



from loader import dp

@dp.message_handler(text="Меню🍴")
async def about(message: types.Message):
    await message.answer("Menu: ", reply_markup=get_menu_keyboards())
    
    
    
@dp.message_handler(text="Orqaga⬅")
async def about(message: types.Message):
    await message.answer("Orqaga", reply_markup=get_start_keyboards())
    
    
    
@dp.message_handler(text="Setlar🍱")
async def about(message: types.Message):
    await message.answer("Setlar:", reply_markup=get_sets_keyboards())
    
    
    
@dp.message_handler(text="Orqaga?")
async def back_line(message: types.Message):
    await message.answer("Orqaga", reply_markup=get_menu_keyboards())
    
    
    
@dp.message_handler(text="Lavash🌯")
async def back_line(message: types.Message):
    await message.answer("lavash:", reply_markup=get_lavash_keyboards())
    
    
    
@dp.message_handler(text="Orqaga?")
async def back_line(message: types.Message):
    await message.answer("Orqaga", reply_markup=get_menu_keyboards())
    
    
    
@dp.message_handler(text="Shaurma")
async def back_line(message: types.Message):
    await message.answer("Shaurma:", reply_markup=get_shaurma_keyboards())
    
    

@dp.message_handler(text="Burger")
async def back_line(message: types.Message):
    await message.answer("Burger:", reply_markup=get_burger_keyboards())
    
    
    
@dp.message_handler(text="Hot-Dog")
async def back_line(message: types.Message):
    await message.answer("Hot-Dog:", reply_markup=get_ht_keyboards())



@dp.message_handler(text="Ichimliklar")
async def back_line(message: types.Message):
    await message.answer("Ichimliklar:", reply_markup=get_suv_keyboards())