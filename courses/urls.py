from . import views
from django.urls import path

urlpatterns = [
    path('', views.CourseList.as_view(), name='home2'),
    path('guest_dashboard/', views.guest_dashboard, name='guest_dashboard'),
]