from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_sets_keyboards():
    sets_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Kombo plus Isutuvchan (Qora Choy)"),
                KeyboardButton(text="Iftar Kofte grill mol goshtidan")
            ],
            [
                KeyboardButton(text="Donar boks tovuq goshtidan"),
                KeyboardButton(text="Iftar strips tovuq goshtidan")
            ],
            [
                KeyboardButton(text="Fit Combo"),
                KeyboardButton(text="Donar boks mol go'shtidan")
            ],
            [
                KeyboardButton(text="COMBO+"),
                KeyboardButton(text="kids COMBO")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return sets_buttons