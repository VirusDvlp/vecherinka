from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext

from json import load, dump

from FSM import DeleteEventFSM, MainAdminFSM
from keyboards import get_cancel_kb, get_choice_day_kb, get_events_kb, get_choice_edit_kb


async def ask_event_day(message: types.Message):
    await DeleteEventFSM.dayState.set()
    await message.answer('Удаление вечеринки', reply_markup=get_cancel_kb('УДАЛЕНИЕ'))
    await message.answer(
        'Выберите день недели, в котором хотите удалить вечеринку',
        reply_markup=get_choice_day_kb()
    )


async def ask_event(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['day'] = callback.data.split('_')[1]
        with open('daysTexts.json', 'r', encoding='utf-8') as file:
            data['days'] = load(file)
        await DeleteEventFSM.eventState.set()
        await callback.message.answer(
            'Выберите, какое событие хотите удалить',
            reply_markup=get_events_kb(data['days'][data['day']])
        )
    await callback.answer()


async def delete_event(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        index = callback.data.split('_')[1]
        del data['days'][data['day']][int(index)]
        with open('daysTexts.json', 'w', encoding='utf-8') as file:
            dump(data['days'], file, ensure_ascii=False, indent=1)
        await state.finish()
        await callback.message.answer(
            'Событие успешно удалено',
            reply_markup=get_choice_edit_kb()
        )
    await callback.answer()


def register_delete_event_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        ask_event_day,
        Text('УДАЛИТЬ ОДНУ ИЗ ВЕЧЕРИНОК'),
        state=MainAdminFSM.adminState
    )
    dp.register_callback_query_handler(
        ask_event,
        Text(startswith='day_'),
        state=DeleteEventFSM.dayState
    )
    dp.register_callback_query_handler(
        delete_event,
        Text(startswith='event_'),
        state=DeleteEventFSM.eventState
    )
