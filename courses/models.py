
from django.db import models
from user_profiles.models import UserProfile 

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courses')
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField(default=20)

    def __str__(self):
        return self.name


