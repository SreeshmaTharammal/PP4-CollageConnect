from django.db import models
from users.models import Student

class Course(models.Model):
    """
    Model for course
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    """
    Model for enrollment
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['student', 'course']

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
