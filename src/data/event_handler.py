import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HTTPRequest
from src.http_types.http_response import HTTPResponse

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request: HTTPRequest) -> HTTPResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HTTPResponse(
            body={ "eventID": body["uuid"] },
            status_code=200
        )