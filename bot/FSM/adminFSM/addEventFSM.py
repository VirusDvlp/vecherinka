from aiogram.dispatcher.filters.state import StatesGroup, State


class AddEventFSM(StatesGroup):
    dayState = State()
    photoState = State()
    captionState = State()
    timeState = State()
    placeState = State()
    priceState = State()
    textState = State()
    buttonState = State()
    buttonTextState = State()
    buttoUrlState = State()