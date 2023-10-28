from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Create your models here.
