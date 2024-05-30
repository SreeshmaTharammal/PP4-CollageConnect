from django.db import models
from users.models import Student, Instructor
from subjects.models import Subject

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
