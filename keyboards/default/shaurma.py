from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_shaurma_keyboards():
    shaurma_buttons = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Shaurma qalampir mol go'sht"),
                KeyboardButton(text="Shaurma qalampir to'vuq go'sht")
            ],
            [
                KeyboardButton(text="Shaurma mol go'sht"),
                KeyboardButton(text="Shaurma to'vuq go'sht")
            ],
            [
                KeyboardButton(text="Orqaga⬅")
            ]
        ],
        resize_keyboard=True
    )
    return shaurma_buttons