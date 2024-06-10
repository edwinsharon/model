from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)
        return render(request,"main.html",{'user':user})
    return render(request,"index.html")
def main(request):
    return render(request,"main.html")    
def loginin(request):
    user=None 
    if request.POST:
      username=request.POST['username']
      password=request.POST['password']
      user=authenticate(username=username,password=password)
      if user is not None:
          return render(request,"main.html",{"user":user})
      else:
          return render(request,"login.html")
    return render(request,"login.html")    
       

        

