from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать объявление")],
        [KeyboardButton(text="Список объявлений")]
    ],
    resize_keyboard=True
)