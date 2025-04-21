from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню контактов
company_info_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📲 Связаться с нами', callback_data='contact')],
    [InlineKeyboardButton(text='🗺️ Наше местоположение', callback_data='geolocation')],
    [InlineKeyboardButton(text='🌐 Наш сайт и почта', callback_data='website')],
    [InlineKeyboardButton(text="⬅️ Вернуться в главное меню", callback_data="back-main")]
])

# Меню контактов по отделам
contacts_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📞 Общий отдел", callback_data="contact_common")],
    [InlineKeyboardButton(text="💼 Отдел продаж", callback_data="contact_sales")],
    [InlineKeyboardButton(text="🔧 Сервисный отдел", callback_data="contact_service")],
    [InlineKeyboardButton(text="🔩 Отдел запчастей", callback_data="contact_parts")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="back-contacts")]
])


website_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌐 Перейти на сайт", url="https://kts77.ru/")],
    [InlineKeyboardButton(text="📧 Написать на почту", url='https://mail.yandex.ru/compose?to=info@kts77.ru')],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="back-contacts")]
])





# Кнопка возврата в главное меню
back_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Вернуться в главное меню", callback_data="back-main")]
])

# Кнопка возврата назад
back_only_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="back-contacts")]
])
