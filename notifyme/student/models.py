from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    email = models.email(max_length=100)
    password = models.charfield(max_lenght=100)
