from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)