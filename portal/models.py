from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    doj = models.DateField()
    designation = models.CharField(max_length=20)
    image = models.FileField()

    def __str__(self):
        return self.name
