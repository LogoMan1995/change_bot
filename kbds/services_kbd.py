from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



start_kbd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛠️ Услуги', callback_data='service')],
    [InlineKeyboardButton(text='💸 Выкуп', callback_data='buyout')],
    [InlineKeyboardButton(text='🤝 Наши партнёры', callback_data='partner')],
    [InlineKeyboardButton(text='📜 Сертификаты', callback_data='certificat')],
    [InlineKeyboardButton(text='💲 Прайс-лист', callback_data='pricelist')],
    [InlineKeyboardButton(text='📞 Контакты', callback_data='contacts')],
])



promo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔧 ТО и регламентное обслуживание грузовых автомобилей и полуприцепов', callback_data='maintenance')],
    [InlineKeyboardButton(text='⚙️ Слесарный Цех', callback_data='metalworking')],
    [InlineKeyboardButton(text='🚗 Ремонт ходовой', callback_data='chassisrepair')],
    [InlineKeyboardButton(text='💻 Компьютерная диагностика', callback_data='diagnostic')],
    [InlineKeyboardButton(text='🔌 Ремонт электрооборудования', callback_data='electrical')],
    [InlineKeyboardButton(text='🚛 Ремонт полуприцепов', callback_data='semitrailer')],
    [InlineKeyboardButton(text="⬅️ Вернуться в главное меню", callback_data="back-main")]
])


back_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]
)


back_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Вернуться в главное меню", callback_data="back-main")]
])


