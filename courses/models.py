from django.db import models
from users.models import Student

# Create your models here.
class Course(models.Model):
    """
    Model for course
    """
    name = models.CharField(max_length = 100)
    description = models.TextField()

class Enrollment(models.Model):
    """
    Model for enrollment
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null = True, blank = True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

