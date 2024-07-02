from django.db import models
from django.shortcuts import render, redirect
from .models import Course, Enrollment
from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()



@login_required
def guest_dashboard(request):
    user_profile = request.user.userprofile
    if not user_profile.is_guest:
        return redirect('dashboard')

    courses = Course.objects.all()
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        if not Enrollment.objects.filter(user_profile=user_profile).exists():
            Enrollment.objects.create(course=course, user_profile=user_profile)
            return redirect('guest_dashboard')
        else:
            error = "You can only request enrollment for one course at a time."
            return render(request, 'courses/guest_dashboard.html', {'courses': courses, 'error': error})

    return render(request, 'courses/guest_dashboard.html', {'courses': courses})
