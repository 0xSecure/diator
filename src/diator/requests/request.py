from uuid import UUID, uuid4

import pydantic
from pydantic import BaseModel


class Request(BaseModel):
    """
    Base class for request-type objects.

    The request is an input of the request handler.
    Often Request is used for defining queries or commands.

    Usage::

      class JoinMeetingCommand(Request):
          meeting_id: int
          user_id: int

      class ReadMeetingByIdQuery(Request):
          meeting_id: int

    """

    request_id: UUID = pydantic.Field(default_factory=uuid4)
