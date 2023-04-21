from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os
from app.middlewares import DataAccessMiddleware

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
dp.message.middleware.register(DataAccessMiddleware())
dp.callback_query.middleware.register(DataAccessMiddleware())
