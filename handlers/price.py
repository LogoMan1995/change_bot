from aiogram import Router, F
from aiogram.types import CallbackQuery
import information.description as service_text
import kbds.services_kbd as keyboard

price_router = Router()


@price_router.callback_query(F.data == 'pricelist')
async def price(callback: CallbackQuery):
    await callback.message.edit_text(service_text.price_list, reply_markup=keyboard.back_main)
    await callback.answer()


@price_router.callback_query(F.data == 'back-main')
async def back_button(callback: CallbackQuery):
   welcome_text = service_text.welcome.format(user=callback.from_user.first_name)
   await callback.message.edit_text(text=welcome_text, reply_markup=keyboard.start_kbd)
   await callback.answer()


