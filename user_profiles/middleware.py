from .models import UserProfile

class EnsureUserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check if user profile exists
            if not UserProfile.objects.filter(user=request.user).exists():
                # Create user profile if it doesn't exist
                UserProfile.objects.create(user=request.user)
        response = self.get_response(request)
        return response
