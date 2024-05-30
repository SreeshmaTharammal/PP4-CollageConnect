from django.contrib import admin
from .models import User, Admin, Student, Instructor

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Instructor)
