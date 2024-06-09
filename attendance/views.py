from django.shortcuts import render
from django.views import generic
from .models import Attendance

# Create your views here.
class AttendanceList(generic.ListView):
    model = Attendance