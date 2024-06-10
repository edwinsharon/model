from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)
        return render(request,"index.html",{'user':user})
    return render(request,"index.html")
def main(request):
    return render(request,"main.html")    
def loginin(request):
    
    return render(request,"login.html")    
       

        

