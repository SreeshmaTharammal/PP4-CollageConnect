from django.db import models
from courses.models import Course
from users.models import Instructor

class Subject(models.Model):
    """
    Model for subject
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
