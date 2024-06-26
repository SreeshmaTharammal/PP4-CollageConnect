# attendance/models.py
from django.db import models
from user_profiles.models import UserProfile
from subjects.models import Subject

class Attendance(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    is_absent = models.BooleanField(default=False)
