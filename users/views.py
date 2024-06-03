from django.contrib.auth.views import LoginView
#from django.urls import reverse_lazy

# Create your views here.
class UserLogin(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
