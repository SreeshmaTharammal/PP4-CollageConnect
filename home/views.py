# home/views.py
from django.shortcuts import render
from courses.models import Course

def home_page(request):
    courses = Course.objects.all()
    return render(request, 'home/index.html', {'courses': courses})
