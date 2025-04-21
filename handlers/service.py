from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram.filters import CommandStart

import information.description as service_text
import kbds.services_kbd as keyboard

service_router = Router()


@service_router.message(CommandStart())
async def start(message: Message):
    welcome = service_text.welcome.format(user=message.from_user.first_name)
    await message.answer(welcome, reply_markup=keyboard.start_kbd)


@service_router.callback_query(F.data == 'service')
async def show_services(callback: CallbackQuery):
    await callback.message.edit_text("Выберите услугу:", reply_markup=keyboard.promo)
    await callback.answer()


@service_router.callback_query(F.data == 'maintenance')
async def maintenance(callback: CallbackQuery):
    await update_service(callback, "img/mechanical-engineering960.jpg", service_text.maintenance)


@service_router.callback_query(F.data == "metalworking")
async def metalworking(callback: CallbackQuery):
    text = f"{service_text.metalworkingshop_part1}\n{service_text.metalworkingshop_part2}"
    await update_service(callback, "img/metalworking960.jpg", text)


@service_router.callback_query(F.data == "chassisrepair")
async def chassis(callback: CallbackQuery):
    await update_service(callback, "img/chassisrepair960.jpg", service_text.ChassisRepair)


@service_router.callback_query(F.data == "diagnostic")
async def diagnostic(callback: CallbackQuery):
    text = f"{service_text.diagnostic_services_part1}\n{service_text.diagnostic_services_part2}"
    await update_service(callback, "img/computer-diagnostics960.jpg", text)


@service_router.callback_query(F.data == "electrical")
async def electrical(callback: CallbackQuery):
    await update_service(callback, "img/electrical960.jpg", service_text.electrical_equipment_repair)


@service_router.callback_query(F.data == "semitrailer")
async def semitrailer(callback: CallbackQuery):
    text = f"{service_text.semitrailerpart1}\n{service_text.semitrailerpart2}"
    await update_service(callback, "img/semitrailerrepair960.jpg", text)


@service_router.callback_query(F.data == "back_to_services")
async def back_to_services(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Выберите услугу:", reply_markup=keyboard.promo)
    await callback.answer()
    
    
@service_router.callback_query(F.data == "back-main")
async def return_main(callback: CallbackQuery):
    await callback.message.answer(text=service_text.welcome, reply_markup=keyboard.start_kbd)
    await callback.answer()


async def update_service(callback: CallbackQuery, image_path: str, caption_text: str):
    media = InputMediaPhoto(media=FSInputFile(image_path), caption=caption_text)
    try:
        await callback.message.edit_media(media=media, reply_markup=keyboard.back_button)
    except Exception:
        # Если редактировать не удаётся (например, сообщение не фото), удалить и отправить заново
        await callback.message.delete()
        photo = FSInputFile(image_path)
        await callback.message.answer_photo(photo=photo, caption=caption_text, reply_markup=keyboard.back_button)
    await callback.answer()




