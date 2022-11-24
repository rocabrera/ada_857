from flask import Response


class PredictionError(Exception):
    pass


def exception_handler(ex: Exception):

    if isinstance(ex, PredictionError):

        return Response(response=str(ex), status=400, content_type="application/text")

    else:
        return Response(
            response="Unknown Error", status=500, content_type="application/text"
        )
