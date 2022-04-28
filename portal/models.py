from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=20)
    dept_desc = models.CharField(max_length=300)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    doj = models.DateField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=40)
    image = models.FileField()

    def __str__(self):
        return self.name
