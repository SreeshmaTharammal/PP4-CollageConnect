#from . import views
from django.urls import path
from .views import ShowUser
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
#from django.contrib.auth import views as auth_views

app_name = 'users'  # Namespace for the 'users' app

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),       
    path('test', ShowUser, name='users'),   
]