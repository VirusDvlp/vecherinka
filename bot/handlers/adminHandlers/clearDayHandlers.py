from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from json import load, dump

from createBot import ADMIN_ID
from keyboards import get_cancel_kb, get_choice_day_kb, get_choice_edit_kb
from FSM import MainAdminFSM, ClearDayFSM


async def ask_clear_day(message: types.Message):
    await ClearDayFSM.dayState.set()
    await message.answer('Удаление событий в дне недели', reply_markup=get_cancel_kb('УДАЛЕНИЕ'))
    await message.answer(
        'Выберите день недели, события в котором хотите очистить',
        reply_markup=get_choice_day_kb()
    )


async def clear_day(callback: types.CallbackQuery):
    await MainAdminFSM.adminState.set()
    with open('daysTexts.json', 'r', encoding='utf-8') as file:
        days = load(file)
    days[callback.data.split('_')[1]] = []
    with open('daysTexts.json', 'w', encoding='utf-8') as file:
        dump(days, file, ensure_ascii=False, indent=1)
    await callback.message.answer('День недели успешно очищен', reply_markup=get_choice_edit_kb())
    await callback.answer()


def register_clear_day_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        ask_clear_day,
        Text('УДАЛИТЬ ВСЕ ВЕЧЕРИНКИ'),
        state=MainAdminFSM.adminState
    )
    dp.register_callback_query_handler(clear_day, Text(startswith='day_'), state=ClearDayFSM.dayState)
