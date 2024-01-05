from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from createBot import ADMIN_ID


def get_main_kb(id: int) -> ReplyKeyboardMarkup:
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    fr_bt = KeyboardButton('Пятница')
    st_bt = KeyboardButton('Суббота')
    sn_bt = KeyboardButton('Воскресенье')
    main_kb.row(fr_bt, st_bt, sn_bt)
    if id == ADMIN_ID:
        admin_bt = KeyboardButton('АДМИН-ПАНЕЛЬ')
        main_kb.add(admin_bt)
    return main_kb
