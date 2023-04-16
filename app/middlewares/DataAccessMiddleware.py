from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from app.database import Dal, User


class DataAccessMiddleware(BaseMiddleware):
    """
    DataAccessMiddleware class.

    This middleware is used to provide access to the database
    """
    async def on_process_update(self, update: Message, data):
        """
        On process message.
        """
        self.session = Dal()
        user = self.session.query(User).filter(
            User.id == update.from_user.id).first()
        data["user"] = user
        data['session'] = self.session

    async def on_process_post_process(self, call, data):
        """
        On process post process.
        """
        self.session.close()

    async def __call__(self, handler, event, data: Dict[str, Any]) -> Any:
        """
        Execute middleware

        :param handler: Wrapped handler in middlewares chain
        :param event: Incoming event (Subclass of :class:`aiogram.types.base.TelegramObject`)
        :param data: Contextual data. Will be mapped to handler arguments
        :return: :class:`Any`
        """
        await self.on_process_update(event, data)
        result = await handler(event, data)
        await self.on_process_post_process(event, data)
        return result
