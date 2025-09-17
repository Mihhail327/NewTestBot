from aiogram import Router, types, F
from aiogram.types import Message
from keyboards.inline import confirm_text_kb, back_to_menu_kb
from utils.storage import save_ad
from logger import logger

router = Router()

@router.callback_query(lambda c: c.data == "menu_add")
async def menu_add(callback: types.CallbackQuery):
    await callback.message.answer("✏️ Напишите текст объявления или отправьте фото/аудио.")
    await callback.answer()

@router.message(F.text)
async def handle_text(message: Message):
    logger.info(f"Текст от {message.from_user.id}: {message.text}")
    await message.answer(f"Ваш текст:\n{message.text}", reply_markup=confirm_text_kb())

@router.callback_query(F.data == "save_text")
async def save_text(callback: types.CallbackQuery):
    text = callback.message.text.replace("Ваш текст:\n", "")
    ad = {
        "user_id": callback.from_user.id,
        "type": "text",
        "content": text,
        "likes": 0
    }
    save_ad(ad)
    await callback.message.edit_text("✅ Объявление сохранено.", reply_markup=back_to_menu_kb())
    await callback.answer()

@router.callback_query(F.data == "cancel")
async def cancel(callback: types.CallbackQuery):
    logger.info(f"Отмена от {callback.from_user.id}")
    await callback.message.edit_text("❌ Отменено.", reply_markup=back_to_menu_kb())
    await callback.answer()

@router.message(F.photo)
async def handle_photo(message: Message):
    file_id = message.photo[-1].file_id
    caption = message.caption or ""
    ad = {
        "user_id": message.from_user.id,
        "type": "photo",
        "file_id": file_id,
        "caption": caption,
        "likes": 0
    }
    logger.info(f"Фото от {message.from_user.id}, file_id: {file_id}")
    save_ad(ad)
    await message.answer("📸 Фото-объявление сохранено.", reply_markup=back_to_menu_kb())

@router.message(F.audio | F.voice)
async def handle_audio(message: Message):
    file_id = message.audio.file_id if message.audio else message.voice.file_id
    ad = {
        "user_id": message.from_user.id,
        "type": "audio",
        "file_id": file_id,
        "likes": 0
    }
    logger.info(f"Аудио от {message.from_user.id}, file_id: {file_id}")
    save_ad(ad)
    await message.answer("🎶 Аудио-объявление добавлено.", reply_markup=back_to_menu_kb())