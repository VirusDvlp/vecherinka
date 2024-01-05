from aiogram import executor

from createBot import dp
from handlers import register_all_handlers


async def on_startup(dp):
    register_all_handlers(dp)
    print('Бот успешно запущен')


async def on_shutdown(dp):
    print('Бот завершил свою работу')


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
