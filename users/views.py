# views.py

from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

#@login_required(login_url='/user/login/')
def ShowUser(request):
    
    if request.user.is_authenticated:
    #student = request.user
    #courses = Course.objects.filter(enrollment__student=student)
    #attendance_records = Attendance.objects.filter(student=student)

    #context = {
    #    'courses': courses,
    #    'attendance_records': attendance_records,
    #}
        return render(request, 'users/admin_dashboard.html')

