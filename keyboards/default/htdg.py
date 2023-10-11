from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_ht_keyboards():
    ht_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Hot-Dog begauete"),
                KeyboardButton(text="Sub tovuq")
            ],
            [
                KeyboardButton(text="Hot-dog kids"),
                KeyboardButton(text="Hot-dog classic")
            ],
            [
                KeyboardButton(text="Sub tovuq cheese"),
                KeyboardButton(text="Hot-dog baguette double")
            ],
            [
                KeyboardButton(text="Sub go'sht cheese"),
                KeyboardButton(text="Sub go'sht")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return ht_buttons