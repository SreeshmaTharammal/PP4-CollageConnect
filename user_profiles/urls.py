from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.custom_login, name='custom_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard')
]
