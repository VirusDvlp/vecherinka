from .adminHandlers import register_admin_handlers
from .daysHandlers import register_days_handlers
from .startHandlers import register_start_handlers


def register_all_handlers(dp) -> None:
    register_start_handlers(dp)
    register_admin_handlers(dp)
    register_days_handlers(dp)
