# subjects/models.py
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    courses = models.ManyToManyField('courses.Course', related_name='subjects')

    def __str__(self):
        return self.name
