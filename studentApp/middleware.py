from django.shortcuts import redirect
from django.urls import reverse

class AdminLoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == reverse('admin:login'):
            return redirect('custom_admin_login')
        response = self.get_response(request)
        return response

class SuperuserRequiredMiddleware:
    """
    Middleware to ensure only superusers can access the admin panel.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_authenticated or not request.user.is_superuser:
                return redirect('login')  # Redirect to login page if not authenticated or not a superuser
        response = self.get_response(request)
        return response



