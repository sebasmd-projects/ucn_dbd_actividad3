import logging
from datetime import datetime

from django.conf import settings
from django.db import transaction
from django.utils.translation import gettext as _

from .models import RequestLogModel

logger = logging.getLogger(__name__)


class APILogMiddleware:
    """Middleware to log API requests."""

    def __init__(self, get_response):
        """Initialize the APILogMiddleware.

        :param get_response: The function to get the response.
        :type get_response: function
        """
        self.get_response = get_response
        self.request_log = None

    def __call__(self, request):
        """Handle the middleware logic.

        :param request: The HTTP request.
        :type request: HttpRequest

        :return: The HTTP response.
        :rtype: HttpResponse
        """
        response = self.get_response(request)

        logger.warning(f"Referring page {request.META.get('HTTP_REFERER', '')}")
        logger.warning(f"Origin page {request.META.get('HTTP_ORIGIN', '')}")
        logger.warning(f"META {request.META}")
        logger.warning(f"GET {request.GET}")
        logger.warning(f"POST {request.POST}")

        if request.path.startswith('/api/') and request.path not in settings.MIDDLEWARE_NOT_INCLUDE:
            self.request_log = RequestLogModel.get_instance()
            self.save_request_log(request, response)
        return response

    def save_request_log(self, request, response):
        """Save the request log entry.

        :param request: The HTTP request.
        :type request: HttpRequest
        :param response: The HTTP response.
        :type response: HttpResponse
        """
        client_ip = self.get_client_ip(request)
        referring_page = request.META.get('HTTP_REFERER', '')
        origin = request.META.get('HTTP_ORIGIN', '')

        entry = {
            _('timestamp'): datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S'),
            _('method'): request.method,
            _('url'): request.path,
            _('status'): response.status_code,
            _('client_ip'): client_ip,
            _('referring_page'): referring_page,
            _('origin'): origin,
        }

        print(datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S'))

        with transaction.atomic():
            self.request_log.add_request_entry(entry)

    def get_client_ip(self, request):
        """Get the client's IP address from the request.

        :param request: The HTTP request.
        :type request: HttpRequest

        :return: The client's IP address.
        :rtype: str
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
