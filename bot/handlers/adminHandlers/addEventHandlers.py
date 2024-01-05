from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext

from json import load, dump

from createBot import ADMIN_ID
from keyboards import get_add_button_kb, get_cancel_kb, get_choice_day_kb, get_choice_edit_kb
from FSM import MainAdminFSM, AddEventFSM


async def ask_what_change(message: types.Message):
    await AddEventFSM.dayState.set()
    await message.answer('Добавление вечеринки', reply_markup=get_cancel_kb('ДОБАВЛЕНИЕ'))
    await message.answer(
        'Выберите, для какого дня недели хотите добавить вечеринку',
        reply_markup=get_choice_day_kb()
    )


async def ask_photo(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['day'] = callback.data.split('_')[1]
        data['keyboard'] = []
        data['photo'] = None
        data['text'] = None
        data['caption'] = None
        data['time'] = None
        data['place'] = None
        data['price'] = None
    await AddEventFSM.photoState.set()
    await callback.message.answer(
        '''Пришлите фото, которое хотите добавить в сообщение.\n
Если его не должно быть, то пришлите любой текст'''
    )
    await callback.answer()


async def ask_caption(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.photo:
            data['photo'] = message.photo[0].file_id
    await AddEventFSM.captionState.set()
    await message.answer(
        '''Пришлите название вечеринки'''
    )


async def ask_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['caption'] = message.text
    await AddEventFSM.timeState.set()
    await message.answer(
        '''Пришлите время начала вечеринки'''
    )


async def ask_place(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await AddEventFSM.placeState.set()
    await message.answer(
        '''Пришлите место вечеринки'''
    )


async def ask_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place'] = message.text
    await AddEventFSM.priceState.set()
    await message.answer(
        '''Пришлите стоимость входа'''
    )


async def ask_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await AddEventFSM.textState.set()
    await message.answer(
        '''Пришлите текст описания вечерикни'''
    )


async def ask_button(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = {
            'caption': data['caption'],
            'time': data['time'],
            'place': data['place'],
            'price': data['price'],
            'text': message.text
        }
    await AddEventFSM.buttonState.set()
    await message.answer(
        '''Теперь решите, будут ли в вашем сообщении кнопки, если да,
то нажмите "ДОБАВИТЬ КНОПКУ", а если нет, то жмите кнопку "ГОТОВО"''',\
        reply_markup=get_add_button_kb()
    )


async def finish_message(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        with open('daysTexts.json', 'r', encoding='utf-8') as file:
            days = load(file)
            days[data['day']].append(
                {
                    'text': data['text'],
                    'photo': data['photo'],
                    'keyboard': data['keyboard']
                }
            )
        with open('daysTexts.json', 'w', encoding='utf-8') as file:
            dump(days, file, ensure_ascii=False, indent=1)
    await MainAdminFSM.adminState.set()
    await callback.message.answer('Вечеринка успешно добавлена', reply_markup=get_choice_edit_kb())
    await callback.answer()


async def ask_button_text(callback: types.CallbackQuery, state: FSMContext):
    await AddEventFSM.buttonTextState.set()
    await callback.message.answer('Пришлите текст кнопки')
    await callback.answer()


async def ask_button_url(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['button_text'] = message.text
    await AddEventFSM.buttoUrlState.set()
    await message.answer('Пришлите ссылку, на которую будет ввести ваша кнопка')


async def get_button_url(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['button_url'] = message.text
        data['keyboard'].append(
            {
                'text': data['button_text'],
                'url': data['button_url']
            }
        )
    await AddEventFSM.buttonState.set()
    await message.answer('Кнопка успешно добавлена', reply_markup=get_add_button_kb())


def register_add_event_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(ask_what_change, Text('ДОБАВИТЬ ВЕЧЕРИНКУ'), state=MainAdminFSM.adminState)
    dp.register_callback_query_handler(ask_photo, Text(startswith='day_'), state=AddEventFSM.dayState)
    dp.register_message_handler(ask_caption, content_types=['photo', 'text'], state=AddEventFSM.photoState)
    dp.register_message_handler(ask_time, state=AddEventFSM.captionState)
    dp.register_message_handler(ask_place, state=AddEventFSM.timeState)
    dp.register_message_handler(ask_price, state=AddEventFSM.placeState)
    dp.register_message_handler(ask_text, state=AddEventFSM.priceState)
    dp.register_message_handler(ask_button, state=AddEventFSM.textState)
    dp.register_callback_query_handler(finish_message, Text('complete'), state=AddEventFSM.buttonState)
    dp.register_callback_query_handler(ask_button_text, Text('button'), state=AddEventFSM.buttonState)
    dp.register_message_handler(ask_button_url, state=AddEventFSM.buttonTextState)
    dp.register_message_handler(get_button_url, state=AddEventFSM.buttoUrlState)
