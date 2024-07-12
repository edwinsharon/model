from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    productname=models.CharField(max_length=100)
    prize=models.IntegerField()
    offer=models.CharField(max_length=50)
    speed=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    category=models.CharField(max_length=50)
    image=models.ImageField(upload_to='static/images/product/')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)