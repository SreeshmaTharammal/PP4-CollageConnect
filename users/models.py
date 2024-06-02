from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Model for user
    """
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username

class Admin(models.Model):
    """
    Model for admin
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    """
    Model for student
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Instructor(models.Model):
    """
    Model for instructor
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
