from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from project.rest_exception.errors import BaseApiException

__all__ = ('custom_exception_handler', )


def custom_exception_handler(exc, context):
    ERROR_STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR

    error = {
        'code': ERROR_STATUS_CODE,
        'devMessage': str(exc),
        'errorMessage': _('Internal Server Error.'),
    }

    if isinstance(exc, BaseApiException):
        error['code'] = exc.code
        error['devMessage'] = exc.detail
        error['errorMessage'] = exc.default_detail

        return Response({'error': error}, status=exc.status_code)
    return Response({'error': error}, status=ERROR_STATUS_CODE)

