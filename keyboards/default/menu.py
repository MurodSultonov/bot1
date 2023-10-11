from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_menu_keyboards():
    menu_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Setlar🍱"),
                KeyboardButton(text="Lavash🌯")
            ],
            [
                KeyboardButton(text="Shaurma"),
                KeyboardButton(text="Burger")
            ],
            [
                KeyboardButton(text="Hot-Dog"),
                KeyboardButton(text="Ichimliklar")
            ],
            [
                KeyboardButton(text="Shirinlik va Desertlar"),
                KeyboardButton(text="Garnirlar")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return menu_buttons