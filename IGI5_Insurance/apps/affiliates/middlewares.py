from django.utils import timezone
import pytz

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tz_name = request.COOKIES.get('timezone')
        if tz_name:
            timezone.activate(pytz.timezone(tz_name))
        else:
            timezone.deactivate()

        response = self.get_response(request)
        return response