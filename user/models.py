from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11,blank=False)
    address = models.CharField(max_length=50,blank=False)