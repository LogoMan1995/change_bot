import logging
from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    FSInputFile,
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import kbds.services_kbd as keyboard
import information.description as service_text



# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

partner_router = Router()

IMAGE_FOLDER = "img/"

partners = [
    ('hyva.jpg', 'Hyva'),
    ('wabco.jpg', 'WABCO'),
    ('bpw.jpg', 'BPW'),
    ('binotto.jpg', 'Binotto'),
    ('jmkipper.jpg', 'JM Kipper'),
    ('gazprom.jpg', 'Gazprom'),
    ('dongfeng.jpg', 'Dongfeng'),
    ('faw.jpg', 'FAW'),
    ('sitrak.jpg', 'Sitrak'),
    ('chengloong.jpg', 'ChengLoong'),
    ('tonar.jpg', 'Tonar'),
    ('wielton.jpg', 'Wielton'),
]

# Хранилище состояния пользователя
user_states: dict[int, dict] = {}


def get_partner_keyboard(index: int) -> InlineKeyboardMarkup:
    keyboard_rows = []

    # Навигационные кнопки
    navigation_buttons = []
    if index > 0:
        navigation_buttons.append(InlineKeyboardButton(text="⬅️ Предыдущая", callback_data="prev-partner"))
    if index < len(partners) - 1:
        navigation_buttons.append(InlineKeyboardButton(text="Следующая ➡️", callback_data="next-partner"))

    if navigation_buttons:
        keyboard_rows.append(navigation_buttons)

    # Кнопка "Назад"
    back_button = InlineKeyboardButton(text="⬅️ Вернуться в главное меню", callback_data="back-main")
    keyboard_rows.append([back_button])

    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)



@partner_router.callback_query(F.data == 'partner')
async def show_first_partner(callback: CallbackQuery):
    user_id = callback.from_user.id
    user_states[user_id] = {'partner_index': 0}

    file_name, partner_name = partners[0]
    image_path = IMAGE_FOLDER + file_name
    caption = f"<b>✨ Партнёр 1/{len(partners)}: {partner_name} ✨</b>"
    media = InputMediaPhoto(media=FSInputFile(image_path), caption=caption, parse_mode="HTML")

    try:
        await callback.message.edit_media(media=media, reply_markup=get_partner_keyboard(0))
    except Exception:
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=FSInputFile(image_path),
            caption=caption,
            reply_markup=get_partner_keyboard(0),
            parse_mode="HTML"
        )

    await callback.answer()


@partner_router.callback_query(F.data.in_({"next-partner", "prev-partner"}))
async def partner_button(callback: CallbackQuery):
    user_id = callback.from_user.id
    state = user_states.setdefault(user_id, {'partner_index': 0})
    index = state['partner_index']

    if callback.data == "next-partner" and index < len(partners) - 1:
        index += 1
    elif callback.data == "prev-partner" and index > 0:
        index -= 1

    state['partner_index'] = index

    file_name, partner_name = partners[index]
    image_path = IMAGE_FOLDER + file_name
    caption = f"<b>✨ Партнёр {index + 1}/{len(partners)}: {partner_name} ✨</b>"
    media = InputMediaPhoto(media=FSInputFile(image_path), caption=caption, parse_mode="HTML")

    try:
        await callback.message.edit_media(media=media, reply_markup=get_partner_keyboard(index))
    except Exception:
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=FSInputFile(image_path),
            caption=caption,
            reply_markup=get_partner_keyboard(index),
            parse_mode="HTML"
        )

    await callback.answer()





@partner_router.callback_query(F.data == 'back-main')
async def back_button(callback: CallbackQuery):
   await callback.message.edit_text(text = service_text.welcome, reply_markup=keyboard.back_main)
   await callback.answer()
