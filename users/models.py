from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    phone = models.IntegerField()

def __str__(self):
    return self.username