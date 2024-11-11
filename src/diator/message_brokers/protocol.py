from typing import Protocol
from uuid import UUID, uuid4

import pydantic
from pydantic import BaseModel


class Message(BaseModel):
    message_type: str
    message_name: str
    message_id: UUID = pydantic.Field(default_factory=uuid4)
    payload: dict


class MessageBroker(Protocol):
    """
    The interface over a message broker.

    Used for sending messages to message brokers (currently only redis supported).
    """

    async def send_message(self, message: Message) -> None:
        ...
