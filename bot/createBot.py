import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import load_dotenv

load_dotenv()


bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

ADMIN_ID = int(os.getenv('ADMIN_ID'))
