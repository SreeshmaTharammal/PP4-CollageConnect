from . import views
from django.urls import path

urlpatterns = [
    path('', views.SubjectList.as_view(), name='home1'),
]