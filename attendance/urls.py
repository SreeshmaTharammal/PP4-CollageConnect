from . import views
from django.urls import path

urlpatterns = [
    path('', views.AttendanceList.as_view(), name='home3'),
]