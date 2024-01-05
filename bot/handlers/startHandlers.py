from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.dispatcher.storage import FSMContext

from keyboards import get_main_kb


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        'Привет! Я — чат-бот, который поможет тебе узнать, какие вечеринки будут на этой неделе.',
        reply_markup=get_main_kb(message.from_user.id)
    )


def register_start_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, CommandStart(), state='*')
    dp.register_message_handler(start, CommandHelp(), state='*')
