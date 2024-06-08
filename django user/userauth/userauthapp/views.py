from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login
# Create your views here.
userobj=user
def index(request):
    
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        userobj=user.objects.get()
        
        userddd=authenticate(email=email,password=password)
        print(userddd)
        if userddd is not None:
            login(request,user)
            print("hai")
            return render(request,'lgin.html')
        else:

            return render(request,'index.html')
    else:
        return render(request,'index.html')    

def done(request):
    return render(request,'lgin.html')        

        

