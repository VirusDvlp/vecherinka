from .mainAdminHandlers import register_main_admin_handlers
from .addEventHandlers import register_add_event_handlers
from .deleteEventHandlers import register_delete_event_handlers
from .clearDayHandlers import register_clear_day_handlers

def register_admin_handlers(dp) -> None:
    register_main_admin_handlers(dp)
    register_add_event_handlers(dp)
    register_delete_event_handlers(dp)
    register_clear_day_handlers(dp)