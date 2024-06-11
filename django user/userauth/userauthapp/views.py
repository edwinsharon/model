from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)  
            return redirect(request,success,{'user',user})
        else:
            return redirect (request,index)
    return render(request,"index.html")    
def loginin(request):
    user=None 
    if request.POST:
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      user=User.objects.create_user(username=username,password=password,email=email)
      if user is not None:
          return redirect(request,index)
      else:
          return render(request,"create.html")
    return render(request,"create.html")  
      
def success(request):
    return render(request,"success.html")
        

