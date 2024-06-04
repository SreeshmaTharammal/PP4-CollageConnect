from django.contrib.auth.views import LoginView

# Create your views here.
class UserLogin(LoginView):
    """
    Login class
    """
    template_name = 'users/login.html'
    redirect_authenticated_user = True
