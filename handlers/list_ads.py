from aiogram import Router, types
from keyboards.inline import back_to_menu_kb
from utils.storage import load_ads
from logger import logger

router = Router()

@router.callback_query(lambda c: c.data == "menu_list")
async def menu_list(callback: types.CallbackQuery):
    logger.info(f"Список объявлений от {callback.from_user.id}")
    ads = load_ads()
    if not ads:
        await callback.message.answer("📭 Нет объявлений.", reply_markup=back_to_menu_kb())
        await callback.answer()
        return

    for idx, ad in enumerate(ads):
        text = f"❤️ {ad['likes']} лайков\n"
        if ad["type"] == "text":
            text += ad["content"]
            await callback.message.answer(text)
        elif ad["type"] == "photo":
            await callback.message.answer_photo(ad["file_id"], caption=f"{ad.get('caption', '')}\n{text}")
        elif ad["type"] == "audio":
            await callback.message.answer_audio(ad["file_id"], caption=text)

    await callback.message.answer("📍 Конец списка.", reply_markup=back_to_menu_kb())
    await callback.answer()