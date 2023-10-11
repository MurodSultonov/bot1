from aiogram.dispatcher.filters.state import StatesGroup, State

class Contactstate(StatesGroup):
    phone = State()
    name = State()
    soni = State()