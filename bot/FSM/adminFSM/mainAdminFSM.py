from aiogram.dispatcher.filters.state import StatesGroup, State


class MainAdminFSM(StatesGroup):
    adminState = State()