import uuid 
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HTTPRequest
from src.http_types.http_response import HTTPResponse
from src.errors.error_types.http_not_found import HTTPNotFoundError
from src.errors.error_types.http_conflict import HTTPConflictError

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
        ): raise HTTPConflictError("This event is already full")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendee(body)

        return HTTPResponse(
            body={ "response": "Attendee successfully registered" },
              status_code=201
            )
    
    def find_attendee_badge(self, http_request: HTTPRequest) -> HTTPResponse:
        attendee_id = http_request.param["attendee_id"]
        badge = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
        if not badge: raise HTTPNotFoundError("Attendee not found")

        return HTTPResponse(
            body={
                "badge": {
                    "name": badge.name,
                    "email": badge.email,
                    "event_title": badge.title
                }
            },
            status_code=200
        )
    
    def find_attendees_from_event(self, http_request: HTTPRequest) -> HTTPResponse:
        event_id = http_request.param["event_id"]
        attendees = self.__attendees_repository.get_attendees_by_event_id(event_id)
        if not attendees : raise HTTPNotFoundError("Attendees not found.")

        formatted_attendees = []
        for attendee in attendees:
            formatted_attendees.append(
                {
                    "id": attendee.id,
                    "name": attendee.name,
                    "email": attendee.email,
                    "checked_in_at": attendee.checked_in_at,
                    "createdAt": attendee.createdAt 
                }
            )
        return HTTPResponse(
            body={ "attendees": formatted_attendees },
            status_code=200
        )