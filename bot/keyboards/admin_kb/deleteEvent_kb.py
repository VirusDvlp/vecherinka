from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_events_kb(events: list) -> InlineKeyboardMarkup:
    events_kb = InlineKeyboardMarkup(1)
    for i in range(len(events)):
        event = events[i]
        caption = event['text']['caption']
        bt = InlineKeyboardButton(caption, callback_data=f'event_{i}')
        events_kb.add(bt)
    return events_kb
