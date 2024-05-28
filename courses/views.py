from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course_view(request):
    return HttpResponse("Courses View")