from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import AutoField
# Create your models here.

class User(AbstractUser):
    
    wallet = models.IntegerField(blank=True, default=1000)
    email =models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

class stock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.title
