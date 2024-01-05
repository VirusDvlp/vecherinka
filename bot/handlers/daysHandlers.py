from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from json import load


async def send_events(message: types.Message):
    text = message.text
    if text == 'Пятница':
        day = '4'
    elif text == 'Суббота':
        day = '5'
    elif text == 'Воскресенье':
        day = '6'
    else:
        await message.answer('Я не знаю данной команды')
        return None
    with open('daysTexts.json', 'r', encoding='utf-8') as file:
        days = load(file)
    day = days.get(day)
    if day:
        for event in day:
            keyboard = types.InlineKeyboardMarkup(1)
            for button in event['keyboard']:
                bt = types.InlineKeyboardButton(button['text'], button['url'])
                keyboard.add(bt)
            mess_text = f'''
{event['text']['caption']}\n
{event['text']['text']}\n\n
Начало: {event['text']['time']}\n
Место: {event['text']['place']}\n
Стоимость: {event['text']['price']}
'''
            if event['photo']:
                await message.answer_photo(event['photo'], mess_text, reply_markup=keyboard, parse_mode=ParseMode().HTML)
            else:
                await message.answer(mess_text, reply_markup=keyboard)
    else:
        await message.answer('Я пока не знаю событий на этот день')


def register_days_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_events)
