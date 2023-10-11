from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_suv_keyboards():
    вде_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="so'k dena 0,33"),
                KeyboardButton(text="Pepsi 0,5")
            ],
            [
                KeyboardButton(text="Quyib beriladigan pepsi"),
                KeyboardButton(text="Amerikano")
            ],
            [
                KeyboardButton(text="Quyib beriladigan pepsi"),
                KeyboardButton(text="ko'k choy")
            ],
            [
                KeyboardButton(text="Suv 0,5"),
                KeyboardButton(text="Pepsi 1,5")
            ],
            [
                KeyboardButton(text="Bliss sharbati"),
                KeyboardButton(text="Latte")
            ],
            [
                KeyboardButton(text="Bliss sharbati"),
                KeyboardButton(text="Qora choy")
            ],
            [
                KeyboardButton(text="Limonli ko'k choy")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return вде_buttons