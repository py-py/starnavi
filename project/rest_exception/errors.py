from rest_framework import exceptions
from rest_framework import status

__all__ = ('Error400', 'Error401', )


class BaseApiException(exceptions.APIException):
    def __init__(self, code, devMessage, errorMessage):
        self.code = code
        self.detail = devMessage
        self.default_detail = errorMessage


class Error400(BaseApiException):
    status_code = status.HTTP_400_BAD_REQUEST


class Error401(BaseApiException):
    status_code = status.HTTP_401_UNAUTHORIZED

