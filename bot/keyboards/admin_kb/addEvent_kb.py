from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_add_button_kb() -> InlineKeyboardMarkup:
    add_button_kb = InlineKeyboardMarkup(1)
    button_bt = InlineKeyboardButton('ДОБАВИТЬ КНОПКУ', callback_data='button')
    comp_bt = InlineKeyboardButton('ГОТОВО✅', callback_data='complete')
    return add_button_kb.add(button_bt, comp_bt)


def get_choice_day_kb() -> InlineKeyboardMarkup:
    choice_day_kb = InlineKeyboardMarkup(1)
    friday_bt = InlineKeyboardButton('Пятница', callback_data='day_4')
    saturday_bt = InlineKeyboardButton('Суббота', callback_data='day_5')
    sunday_bt = InlineKeyboardButton('Воскресенье', callback_data='day_6')
    return choice_day_kb.add(friday_bt, saturday_bt, sunday_bt)
