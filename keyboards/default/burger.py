from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_burger_keyboards():
    burger_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Gamburger"),
                KeyboardButton(text="Cheese burger")
            ],
            [
                KeyboardButton(text="Double burger"),
                KeyboardButton(text="Double cheese")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return burger_buttons