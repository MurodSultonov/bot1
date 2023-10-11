from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_start_keyboards():
    start_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Меню🍴")
            ],
            [
                KeyboardButton(text="Мои заказы📒")
            ],
            [
                KeyboardButton(text="Карзина📥"),
                KeyboardButton(text="Aloqa")
            ],
            [
                KeyboardButton(text="Отправить собщение📨"),
                KeyboardButton(text="Помогите!🆘")
            ],
        ],
        resize_keyboard=True
    )
    return start_buttons