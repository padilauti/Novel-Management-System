from django.utils.deprecation import MiddlewareMixin

class SeparateSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Memeriksa apakah request menuju ke admin
        if request.path.startswith('/admin/'):
            request.session.cookie_name = 'admin_sessionid'
        else:
            request.session.cookie_name = 'web_sessionid'