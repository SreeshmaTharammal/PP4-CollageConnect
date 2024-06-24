# attendance/models.py
from django.db import models
from users.models import User
from subjects.models import Subject

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    is_absent = models.BooleanField(default=False)
