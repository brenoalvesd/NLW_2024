from src.http_types.http_response import HTTPResponse
from .error_types.http_conflict import HTTPConflictError
from .error_types.http_not_found import HTTPNotFoundError

def handle_errors(error: Exception) -> HTTPResponse:
    if isinstance(error, (HTTPConflictError, HTTPNotFoundError)):
        return HTTPResponse(
            body={
                "errors": [{
                    "title": error.name,
                    "details": error.message
                }]
            },
            status_code=error.status_code
        )
    elif hasattr(error, 'status_code'):
        # Handling for exceptions with a 'status_code' attribute
        return HTTPResponse(
            body={
                "errors": [{
                    "title": type(error).__name__,
                    "details": str(error)
                }]
            },
            status_code=error.status_code
        )
    else:
        # Handling for standard exceptions without a 'status_code' attribute
        return HTTPResponse(
            body={
                "errors": [{
                    "title": "Event ID not found",
                    "details": str(error)
                }]
            },
            status_code=500  # Internal Server Error
        )
