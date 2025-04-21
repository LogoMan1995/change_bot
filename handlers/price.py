from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import information.description as service_text
import kbds.services_kbd as keyboard

price_router = Router()


@price_router.callback_query(F.data == 'pricelist')
async def price(callback: CallbackQuery):
    await callback.message.edit_text(service_text.price_list, reply_markup=keyboard.back_button)
    await callback.answer()




