from pydantic import BaseModel


class Response(BaseModel):
    """
    Base class for response type objects.

    The response is a result of the request handling, which hold by RequestHandler.

    Often the response is used for defining the result of the query.

    Usage::

        class ReadMeetingQueryResult(Response):
            meeting_id: int
            link: str
            status: MeetingStatusEnum

    """
