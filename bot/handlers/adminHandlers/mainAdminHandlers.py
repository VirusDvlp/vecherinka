from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text, IDFilter
from aiogram.dispatcher.storage import FSMContext

from createBot import ADMIN_ID
from keyboards import get_main_admin_kb, get_choice_edit_kb, get_main_kb
from FSM import MainAdminFSM


async def set_admin_mode(message: types.Message):
    await MainAdminFSM.adminState.set()
    await message.answer('Выберите, что хотите сделать', reply_markup=get_main_admin_kb())


async def ask_edit(message: types.Message):
    await message.answer('Выберите, что хотите изменить', reply_markup=get_choice_edit_kb())


async def cancel_action(message: types.Message):
    await MainAdminFSM.adminState.set()
    await message.answer('Действие отменено', reply_markup=get_main_admin_kb())


async def exit_admin_mode(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Панель администратора закрыта', reply_markup=get_main_kb(ADMIN_ID))


def register_main_admin_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(set_admin_mode, Text('АДМИН-ПАНЕЛЬ'), IDFilter(ADMIN_ID))
    dp.register_message_handler(
        ask_edit,
        Text('ИЗМЕНИТЬ СООБЩЕНИЯ ДЛЯ ДНЕЙ НЕДЕЛИ'),
        state=MainAdminFSM.adminState
    )
    dp.register_message_handler(cancel_action, Text(startswith='ОТМЕНИТЬ'), IDFilter(ADMIN_ID), state='*')
    dp.register_message_handler(
        exit_admin_mode,
        Text('ВЫЙТИ ИЗ РЕЖИМА АДМИНИСТРАТОРА'),
        state=MainAdminFSM.adminState
    )
