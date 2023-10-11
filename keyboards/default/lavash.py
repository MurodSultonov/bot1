from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_lavash_keyboards():
    lavash_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Mol go'shtidan lavash"),
                KeyboardButton(text="Mol go'shtidan pishloqli lavash Standart")
            ],
            [
                KeyboardButton(text="FITTER"),
                KeyboardButton(text="tovuq go'shli qalampir lavash")
            ],
            [
                KeyboardButton(text="lavash cheese tovuq go'sht standart"),
                KeyboardButton(text="Lavash tovuq go'sht")
            ],
            [
                KeyboardButton(text="Lavash mol go'shti")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return lavash_buttons