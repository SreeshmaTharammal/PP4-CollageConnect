"""
URL configuration for college_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from . import views
from django.views.generic import RedirectView
#from users.views import user_view
#from courses.views import course_view
#from subjects.views import subject_view
#from attendance.views import attendance_view


urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', RedirectView.as_view(url='/users/login/', permanent=True)),
    #path("", include("users.urls"), name="users-urls"),
    #path("subject/", include("subjects.urls"), name="subjects-urls"),
    #path("course/", include("courses.urls"), name="courses-urls"),
    #path("attendance/", include("attendance.urls"), name="attendance-urls"),
    #path('users/', user_view, name='user'),
    #path('courses/', course_view, name='course'),
    #path('subjects/', subject_view, name='subject'),
    #path('attendance/', attendance_view, name='attendance'),
]
