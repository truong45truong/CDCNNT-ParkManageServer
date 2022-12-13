from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=10)
    avatar = models.ImageField(null=True, default="avatar.svg")
    password = models.CharField(max_length=200)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.email