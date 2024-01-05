from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_admin_kb() -> ReplyKeyboardMarkup:
    main_admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    edit_bt = KeyboardButton('ИЗМЕНИТЬ СООБЩЕНИЯ ДЛЯ ДНЕЙ НЕДЕЛИ')
    exit_bt = KeyboardButton('ВЫЙТИ ИЗ РЕЖИМА АДМИНИСТРАТОРА')
    return main_admin_kb.add(edit_bt).add(exit_bt)


def get_choice_edit_kb() -> ReplyKeyboardMarkup:
    choice_edit_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    add_bt = KeyboardButton('ДОБАВИТЬ ВЕЧЕРИНКУ')
    clear_bt = KeyboardButton('УДАЛИТЬ ВСЕ ВЕЧЕРИНКИ')
    delete_bt = KeyboardButton('УДАЛИТЬ ОДНУ ИЗ ВЕЧЕРИНОК')
    cancel_bt = KeyboardButton('ОТМЕНИТЬ РЕДАКТИРОВАНИЕ❌')
    return choice_edit_kb.add(add_bt).add(clear_bt).add(delete_bt).add(cancel_bt)


def get_cancel_kb(action: str) -> ReplyKeyboardMarkup:
    cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_bt = KeyboardButton(f'ОТМЕНИТЬ {action}❌')
    return cancel_kb.add(cancel_bt)
