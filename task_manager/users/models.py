from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class NewUser(AbstractUser):
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)