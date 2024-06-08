from django.db import models

# Create your models here.
class user(models.Model):
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=50)