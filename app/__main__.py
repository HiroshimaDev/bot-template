from aiogram import executor
from app import dp
from app.database import Dal


async def on_startup(dispatcher):
    """
    On startup.
    """
    pass


async def on_shutdown(dispatcher):
    """
    On shutdown.
    """
    Dal.engine.dispose()


executor.start_polling(dp, skip_updates=True,
                       on_startup=on_startup, on_shutdown=on_shutdown)
