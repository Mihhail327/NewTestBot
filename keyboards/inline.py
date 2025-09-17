from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
def main_menu_inline():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📝 Создать объявление", callback_data="menu_add")],
            [InlineKeyboardButton(text="📋 Список объявлений", callback_data="menu_list")]
        ]
    )

# Подтверждение текста
def confirm_text_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Сохранить", callback_data="save_text")],
            [InlineKeyboardButton(text="❌ Отменить", callback_data="cancel")],
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_menu")]
        ]
    )

# Назад в меню
def back_to_menu_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_menu")]
        ]
    )