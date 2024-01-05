from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteEventFSM(StatesGroup):
    dayState = State()
    eventState = State()
