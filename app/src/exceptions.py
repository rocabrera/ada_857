import json
import werkzeug
from flask import Response

class InvalidBodyError(Exception):
    pass

def handle_exception(ex: Exception):

    if isinstance(ex, InvalidBodyError):
        return Response(
            response=json.dumps({"error": str(ex)}),
            status=400,
            content_type="application/json"
        )

    else:
        return Response(
            response=json.dumps({"error": "Unknown error"}),
            status=500,
            content_type="application/json"
        )