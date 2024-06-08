from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login
# Create your views here.
userobj=user
def index(request):
    
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            print("hai")
            return redirect(request,'lgin.html')
        else:

            return render(request,'index.html')
    else:
        return render(request,'index.html')    

def done(request):
    return render(request,'lgin.html')        

        

