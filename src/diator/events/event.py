from datetime import datetime
from uuid import UUID, uuid4

import pydantic
from pydantic import BaseModel


class Event(BaseModel):
    ...


class DomainEvent(Event):
    """
    The base class for domain events.
    """


class NotificationEvent(Event):
    """
    The base class for notification events.

    Contains only identification information about state change.

    Example plain structure::

      {
          "event_id": "82a0b10e-1b3d-4c3c-9bdd-3934f8f824c2",
          "event_timestamp": "2023-03-06 12:11:35.103792",
          "changed_user_id": 987
      }

    """

    event_id: UUID = pydantic.Field(default_factory=uuid4)
    event_timestamp: datetime = pydantic.Field(default_factory=datetime.now)
    _event_type = "notification_event"


class ECSTEvent(Event):
    """
    Base class for ECST events.

    ECST means event-carried state transfer.

    Contains full information about state change.

    Example plain structure::

      {
          "event_id": "82a0b10e-1b3d-4c3c-9bdd-3934f8f824c2",
          "event_timestamp": "2023-03-06 12:11:35.103792",
          "user_id": 987,
          "new_user_last_name": "Doe",
          "new_user_nickname": "kend"
      }

    """

    event_id: UUID = pydantic.Field(default_factory=uuid4)
    event_timestamp: datetime = pydantic.Field(default_factory=datetime.utcnow)
    _event_type = "ecst_event"
