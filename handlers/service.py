from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

import information.description as service_text
import kbds.services_kbd as keyboard
import logging

service_router = Router()
logger = logging.getLogger(__name__)


@service_router.message(CommandStart())
async def start(message: Message):
    welcome = service_text.welcome.format(user=message.from_user.first_name)
    await message.answer(welcome, reply_markup=keyboard.start_kbd)


@service_router.callback_query(F.data == 'service')
async def service(callback: CallbackQuery):
    try:
        await callback.message.edit_text(text='Выберите услугу:', reply_markup=keyboard.promo)
    except Exception as e:
        logger.error(f"Ошибка при показе услуг: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer(text='Выберите услугу:', reply_markup=keyboard.promo)
    
    await callback.answer()


@service_router.callback_query(F.data == 'maintenance')
async def maintenance(callback: CallbackQuery):
    try:
        media = InputMediaPhoto(
            media=FSInputFile("img/mechanical-engineering960.jpg"),
            caption=service_text.maintenance,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=keyboard.back_button)
    except Exception as e:
        logger.error(f"Ошибка при показе ТО: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/mechanical-engineering960.jpg"),
            caption=service_text.maintenance,
            reply_markup=keyboard.back_button,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'metalworking')
async def metalworking(callback: CallbackQuery):
    try:
        # Создаем клавиатуру с кнопками для навигации
        kbd = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Следующая часть ➡️", callback_data="metalworking_part2")],
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back")]
        ])
        
        media = InputMediaPhoto(
            media=FSInputFile("img/metalworking960.jpg"),
            caption=service_text.metalworkingshop_part1,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=kbd)
    except Exception as e:
        logger.error(f"Ошибка при показе слесарного цеха: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/metalworking960.jpg"),
            caption=service_text.metalworkingshop_part1,
            reply_markup=kbd,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'metalworking_part2')
async def metalworking_part2(callback: CallbackQuery):
    try:
        # Создаем клавиатуру с кнопками для навигации
        kbd = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Предыдущая часть", callback_data="metalworking")],
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back")]
        ])
        
        media = InputMediaPhoto(
            media=FSInputFile("img/metalworking960.jpg"),
            caption=service_text.metalworkingshop_part2,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=kbd)
    except Exception as e:
        logger.error(f"Ошибка при показе второй части слесарного цеха: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/metalworking960.jpg"),
            caption=service_text.metalworkingshop_part2,
            reply_markup=kbd,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'chassisrepair')
async def chassisrepair(callback: CallbackQuery):
    try:
        media = InputMediaPhoto(
            media=FSInputFile("img/chassisrepair960.jpg"),
            caption=service_text.ChassisRepair,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=keyboard.back_button)
    except Exception as e:
        logger.error(f"Ошибка при показе ремонта ходовой: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/chassisrepair960.jpg"),
            caption=service_text.ChassisRepair,
            reply_markup=keyboard.back_button,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'diagnostic')
async def diagnostic(callback: CallbackQuery):
    try:
        # Создаем клавиатуру с кнопками для навигации
        kbd = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Следующая часть ➡️", callback_data="diagnostic_part2")],
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back")]
        ])
        
        media = InputMediaPhoto(
            media=FSInputFile("img/computer-diagnostics960.jpg"),
            caption=service_text.diagnostic_services_part1,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=kbd)
    except Exception as e:
        logger.error(f"Ошибка при показе диагностики: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/computer-diagnostics960.jpg"),
            caption=service_text.diagnostic_services_part1,
            reply_markup=kbd,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'diagnostic_part2')
async def diagnostic_part2(callback: CallbackQuery):
    try:
        # Создаем клавиатуру с кнопками для навигации
        kbd = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Предыдущая часть", callback_data="diagnostic")],
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back")]
        ])
        
        media = InputMediaPhoto(
            media=FSInputFile("img/computer-diagnostics960.jpg"),
            caption=service_text.diagnostic_services_part2,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=kbd)
    except Exception as e:
        logger.error(f"Ошибка при показе второй части диагностики: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/computer-diagnostics960.jpg"),
            caption=service_text.diagnostic_services_part2,
            reply_markup=kbd,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'electrical')
async def electrical(callback: CallbackQuery):
    try:
        media = InputMediaPhoto(
            media=FSInputFile("img/electrical960.jpg"),
            caption=service_text.electrical_equipment_repair,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=keyboard.back_button)
    except Exception as e:
        logger.error(f"Ошибка при показе ремонта электрооборудования: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/electrical960.jpg"),
            caption=service_text.electrical_equipment_repair,
            reply_markup=keyboard.back_button,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'semitrailer')
async def semitrailer(callback: CallbackQuery):
    try:
        # Создаем клавиатуру с кнопками для навигации
        kbd = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Следующая часть ➡️", callback_data="semitrailer_part2")],
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back")]
        ])
        
        media = InputMediaPhoto(
            media=FSInputFile("img/semitrailerrepair960.jpg"),
            caption=service_text.semitrailerpart1,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=kbd)
    except Exception as e:
        logger.error(f"Ошибка при показе ремонта полуприцепов: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/semitrailerrepair960.jpg"),
            caption=service_text.semitrailerpart1,
            reply_markup=kbd,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'semitrailer_part2')
async def semitrailer_part2(callback: CallbackQuery):
    try:
        # Создаем клавиатуру с кнопками для навигации
        kbd = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Предыдущая часть", callback_data="semitrailer")],
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back")]
        ])
        
        media = InputMediaPhoto(
            media=FSInputFile("img/semitrailerrepair960.jpg"),
            caption=service_text.semitrailerpart2,
            parse_mode="HTML"
        )
        await callback.message.edit_media(media=media, reply_markup=kbd)
    except Exception as e:
        logger.error(f"Ошибка при показе второй части ремонта полуприцепов: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer_photo(
            photo=FSInputFile("img/semitrailerrepair960.jpg"),
            caption=service_text.semitrailerpart2,
            reply_markup=kbd,
            parse_mode="HTML"
        )
    
    await callback.answer()


@service_router.callback_query(F.data == 'back')
async def back_button(callback: CallbackQuery):
    try:
        await callback.message.edit_text(text='Выберите услугу:', reply_markup=keyboard.promo)
    except Exception as e:
        logger.error(f"Ошибка при возврате к услугам: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer(text='Выберите услугу:', reply_markup=keyboard.promo)
    
    await callback.answer()


@service_router.callback_query(F.data == 'back-main')
async def back_to_main(callback: CallbackQuery):
    welcome_text = service_text.welcome.format(user=callback.from_user.first_name)
    try:
        await callback.message.edit_text(text=welcome_text, reply_markup=keyboard.start_kbd)
    except Exception as e:
        logger.error(f"Ошибка при возврате в главное меню: {e}")
        try:
            await callback.message.delete()
        except Exception as delete_error:
            logger.error(f"Ошибка при удалении сообщения: {delete_error}")
        await callback.message.answer(text=welcome_text, reply_markup=keyboard.start_kbd)
    
    await callback.answer()







