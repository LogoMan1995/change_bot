from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    Message,
    FSInputFile,
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

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

# Простая in-memory переменная для хранения состояния индексов по user_id
user_states = {}

def get_certificate_keyboard(index: int) -> InlineKeyboardMarkup:
    buttons = []
    if index > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Предыдущая", callback_data="prev-certification"))
    if index < len(certificates) - 1:
        buttons.append(InlineKeyboardButton(text="Следующая ➡️", callback_data="next-certification"))
    return InlineKeyboardMarkup(inline_keyboard=[buttons])


@certificates_router.message(F.text == "📜 Сертификаты")
async def show_certification(message: Message):
    user_id = message.from_user.id
    user_states[user_id] = {"cert_index": 0}

    image_path = IMAGE_FOLDER + certificates[0]
    photo = FSInputFile(image_path)
    caption = f"<b>📜 Сертификат 1/{len(certificates)} 📜</b>"

    await message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=get_certificate_keyboard(0),
        parse_mode="HTML"
    )


@certificates_router.callback_query(F.data.in_({"next-certification", "prev-certification"}))
async def certification_button(callback: CallbackQuery):
    user_id = callback.from_user.id
    state = user_states.get(user_id, {"cert_index": 0})
    index = state["cert_index"]

    if callback.data == "next-certification" and index < len(certificates) - 1:
        index += 1
    elif callback.data == "prev-certification" and index > 0:
        index -= 1

    user_states[user_id] = {"cert_index": index}

    image_path = IMAGE_FOLDER + certificates[index]
    caption = f"<b>📜 Сертификат {index + 1}/{len(certificates)} 📜</b>"

    media = InputMediaPhoto(
        media=FSInputFile(image_path),
        caption=caption,
        parse_mode="HTML"
    )

    await callback.message.edit_media(media=media)
    await callback.message.edit_reply_markup(reply_markup=get_certificate_keyboard(index))
    await callback.answer()
