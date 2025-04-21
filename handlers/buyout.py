from aiogram import F, Router
from aiogram.types import CallbackQuery
import information.description as service_text
import kbds.services_kbd as keyboard
import logging

buyout_router = Router()
logger = logging.getLogger(__name__)

@buyout_router.callback_query(F.data == 'buyout')
async def buyout(callback: CallbackQuery):
    await callback.message.edit_text(text=service_text.buyout_full_caption, reply_markup=keyboard.back_main)
    await callback.answer()


@buyout_router.callback_query(F.data == "back-main")
async def return_main(callback: CallbackQuery):
    welcome_text = service_text.welcome.format(user=callback.from_user.first_name)
    try:
        # Пытаемся отредактировать существующее сообщение
        await callback.message.edit_text(text=welcome_text, reply_markup=keyboard.start_kbd)
    except Exception as e:
        logger.error(f"Ошибка при возврате в главное меню: {e}")
        # Если не удалось отредактировать, удаляем текущее сообщение и отправляем новое
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer(text=welcome_text, reply_markup=keyboard.start_kbd)
    
    await callback.answer()



