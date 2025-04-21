from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
import information.description as service_text
import kbds.contacts_kbd as contact_kb

contact_router = Router()


@contact_router.callback_query(F.data == 'contacts')
async def contact(callback: CallbackQuery):
    await callback.message.edit_text(
        service_text.description,
        reply_markup=contact_kb.company_info_kb
    )
    await callback.answer()


@contact_router.callback_query(F.data == 'contact')
async def post_contact(callback: CallbackQuery):
    await callback.message.edit_text(
        text=service_text.call,
        reply_markup=contact_kb.contacts_menu_kb
    )
    await callback.answer()

@contact_router.callback_query(F.data == "contact_common")
async def contact_common(callback: CallbackQuery):
    await callback.message.edit_text(
        "📞 <b>Общий отдел</b>\n"
        "Телефон: +74951428194",
        reply_markup=contact_kb.contacts_menu_kb,
    )
    await callback.answer()


@contact_router.callback_query(F.data == "contact_sales")
async def contact_sales(callback: CallbackQuery):
    await callback.message.edit_text(
        "💼 <b>Отдел продаж</b>\n"
        "Телефон: +79015003343",
        reply_markup=contact_kb.contacts_menu_kb,
    )
    await callback.answer()


@contact_router.callback_query(F.data == "contact_service")
async def contact_service(callback: CallbackQuery):
    await callback.message.edit_text(
        "🔧 <b>Сервисный отдел</b>\n"
        "Телефон: +79775453344",
        reply_markup=contact_kb.contacts_menu_kb,
    )
    await callback.answer()


@contact_router.callback_query(F.data == "contact_parts")
async def contact_parts(callback: CallbackQuery):
    await callback.message.edit_text(
        "🔩 <b>Отдел запчастей</b>\n"
        "Телефон: +79915948006",
        reply_markup=contact_kb.contacts_menu_kb,
    )
    await callback.answer()


@contact_router.callback_query(F.data == 'geolocation')
async def geolocation(callback: CallbackQuery):
    await callback.message.edit_text(
        (
            "📍 <b>Сервисный центр КОМТРАКСЕРВИС</b>\n\n"
            "🗺️ Московская область, г.о. Чехов, Баранцевский участок\n"
            "📌 Координаты: <code>55.135484, 37.516621</code>\n"
            "<a href='https://yandex.com.ge/maps/-/CHqRMVk2'>Открыть в Яндекс.Картах</a>"
        ),
        reply_markup=contact_kb.back_only_kb
    )
    await callback.answer()


@contact_router.callback_query(F.data == 'website')
async def show_online(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выберите, куда хотите перейти:",
        reply_markup=contact_kb.website_kb
    )
    await callback.answer()




@contact_router.callback_query(F.data == 'back')
async def back_button(callback: CallbackQuery):
   await callback.message.edit_text(text = service_text.description, reply_markup=contact_kb.company_info_kb)
   await callback.answer()




@contact_router.callback_query(F.data == 'back-main')
async def back_button(callback: CallbackQuery):
   await callback.message.edit_text(text = service_text.welcome, reply_markup=contact_kb.start_kbd)
   await callback.answer()

