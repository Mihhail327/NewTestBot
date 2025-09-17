from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import main_menu_inline
from logger import logger

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    logger.info(f"/start от {message.from_user.id}")
    await message.answer("⌨️ Скрываю старые кнопки...", reply_markup=ReplyKeyboardRemove())
    await message.answer("👋 Добро пожаловать! Выберите действие:", reply_markup=main_menu_inline())

@router.callback_query(lambda c: c.data == "back_to_menu")
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Главное меню:", reply_markup=main_menu_inline())
    await callback.answer()