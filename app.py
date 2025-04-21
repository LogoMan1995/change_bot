import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers.service import service_router
from handlers.buyout import buyout_router
from handlers.partner import partner_router
from handlers.certificate import certificates_router
from handlers.price import price_router
from handlers.contacts import contact_router
from config import TOKEN

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    # Инициализация бота и диспетчера
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Регистрация роутеров
    dp.include_router(service_router)
    dp.include_router(buyout_router)
    dp.include_router(partner_router)
    dp.include_router(certificates_router)
    dp.include_router(price_router)
    dp.include_router(contact_router)
    
    # Запуск бота
    try:
        logger.info("Бот запущен")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")