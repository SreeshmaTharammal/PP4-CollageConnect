from django.shortcuts import render
from django.views import generic
from .models import Subject

# Create your views here.
class SubjectList(generic.ListView):
    model = Subject