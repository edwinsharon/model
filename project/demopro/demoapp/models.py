from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location=models.CharField(max_length=100)