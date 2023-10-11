from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_shirin_keyboards():
    shirin_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Medovik Asalim"),
                KeyboardButton(text="Donut caaremile")
            ],
            [
                KeyboardButton(text="Chiskeyk"),
                KeyboardButton(text="Donut mevali")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return shirin_buttons