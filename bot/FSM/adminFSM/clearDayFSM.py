from aiogram.dispatcher.filters.state import StatesGroup, State


class ClearDayFSM(StatesGroup):
    dayState = State()
