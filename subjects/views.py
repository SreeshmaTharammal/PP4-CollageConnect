from django.db import models
from courses.models import Course

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    courses = models.ManyToManyField(Course, related_name='subjects')
