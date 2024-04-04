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
    
    def find_by_id(self, http_request: HTTPRequest) -> HTTPResponse:
        event_id = http_request.param["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event: raise Exception("Event not found")

        event_attendees_count = self.__events_repository.count_event_attendees(event_id)
        
        return HTTPResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximum_attendees": event.maximum_attendees,
                    "attendees_amount": event_attendees_count["attendees_amount"] 
                }
            },
            status_code=200
                )
