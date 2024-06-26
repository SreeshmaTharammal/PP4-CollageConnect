
from django.db import models
from user_profiles.models import UserProfile

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courses', null=True, default=None)

    def __str__(self):
        return self.name



class Enrollment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, default=None)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} enrolled in {self.course}"
