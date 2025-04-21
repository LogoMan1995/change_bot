from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
import information.description as service_text
import kbds.services_kbd as keyboard

buyout_router = Router()

@buyout_router.callback_query(F.data == 'buyout')
async def buyout(callback: CallbackQuery):
    await callback.message.edit_text(text=service_text.buyout_full_caption,reply_markup=keyboard.back_button)
    await callback.answer()





@buyout_router.callback_query(F.data == 'back')
async def contact_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=service_text.description,
        reply_markup=keyboard.start_kbd
    )
    await callback.answer()


