import uuid 
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HTTPRequest
from src.http_types.http_response import HTTPResponse

class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def registry(self, http_request: HTTPRequest) -> HTTPResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]

        events_attendees_count = self.__events_repository.count_event_attendees(event_id)
        if (
            events_attendees_count["attendees_amount"]
            and events_attendees_count["maximum_attendees"] < events_attendees_count["attendees_amount"]
        ): raise Exception("This event is already full")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendee(body)

        return HTTPResponse(
            body={ "response": "Attendee successfully registered" },
              status_code=201
            )