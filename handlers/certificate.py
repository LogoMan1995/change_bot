import logging
from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    Message,
    FSInputFile,
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import kbds.services_kbd as keyboard
import information.description as service_text

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

certificates_router = Router()

IMAGE_FOLDER = "img/"

certificates = [
    "certificate1.jpg",
    "certificate2.jpg",
    "certificate3.jpg",
    "certificate4.jpg",
    "certificate5.jpg",
    "certificate6.jpg",
    "certificate7.jpg",
    "certificate8.jpg",
    "certificate9.jpg",
    "certificate10.jpg",
]

# Хранилище состояния пользователя
user_states: dict[int, dict] = {}


def get_certificate_keyboard(index: int) -> InlineKeyboardMarkup:
    keyboard_rows = []

    nav_buttons = []
    if index > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Предыдущая", callback_data="prev-certification"))
    if index < len(certificates) - 1:
        nav_buttons.append(InlineKeyboardButton(text="Следующая ➡️", callback_data="next-certification"))

    if nav_buttons:
        keyboard_rows.append(nav_buttons)

    # Кнопка назад
    back_button = InlineKeyboardButton(text="⬅️ Вернуться в главное меню", callback_data="back-main")
    keyboard_rows.append([back_button])

    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)


@certificates_router.callback_query(F.data == 'certificat')
async def show_certification(callback: CallbackQuery):
    user_id = callback.from_user.id
    user_states[user_id] = {"cert_index": 0}

    index = 0
    image_path = IMAGE_FOLDER + certificates[index]
    caption = f"<b>📜 Сертификат {index + 1}/{len(certificates)} 📜</b>"

    try:
        # Пытаемся отредактировать существующее сообщение
        media = InputMediaPhoto(media=FSInputFile(image_path), caption=caption, parse_mode="HTML")
        await callback.message.edit_media(media=media, reply_markup=get_certificate_keyboard(index))
    except Exception as e:
        logger.error(f"Ошибка при редактировании сертификата: {e}")
        # Если не удалось отредактировать, отправляем новое сообщение
        await callback.message.answer_photo(
            photo=FSInputFile(image_path),
            caption=caption,
            reply_markup=get_certificate_keyboard(index),
            parse_mode="HTML"
        )
    
    await callback.answer()


@certificates_router.callback_query(F.data.in_({"next-certification", "prev-certification"}))
async def certification_button(callback: CallbackQuery):
    user_id = callback.from_user.id
    state = user_states.setdefault(user_id, {"cert_index": 0})
    index = state["cert_index"]

    if callback.data == "next-certification" and index < len(certificates) - 1:
        index += 1
    elif callback.data == "prev-certification" and index > 0:
        index -= 1

    state["cert_index"] = index

    image_path = IMAGE_FOLDER + certificates[index]
    caption = f"<b>📜 Сертификат {index + 1}/{len(certificates)} 📜</b>"
    media = InputMediaPhoto(media=FSInputFile(image_path), caption=caption, parse_mode="HTML")

    try:
        # Пытаемся отредактировать существующее сообщение
        await callback.message.edit_media(media=media, reply_markup=get_certificate_keyboard(index))
    except Exception as e:
        logger.error(f"Ошибка при замене сертификата: {e}")
        # Если не удалось отредактировать, отправляем новое сообщение
        await callback.message.answer_photo(
            photo=FSInputFile(image_path),
            caption=caption,
            reply_markup=get_certificate_keyboard(index),
            parse_mode="HTML"
        )

    await callback.answer()


@certificates_router.callback_query(F.data == 'back-main')
async def back_button(callback: CallbackQuery):
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
