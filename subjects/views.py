from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def subject_view(request):
    return HttpResponse("Subjects View")