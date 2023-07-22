import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import client, admin, common
import database as db
from config_reader import config


async def main():
    # Запуск логгирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Объект бота и диспетчер
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрация роутеров
    dp.include_routers(client.router, admin.router, common.router)

    # Пропускаем все накопленные входящие и запускаем процесс поллинга новых апдейтов
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

    # Старт базы данных
    await db.db_start()


if __name__ == "__main__":
    asyncio.run(main())
