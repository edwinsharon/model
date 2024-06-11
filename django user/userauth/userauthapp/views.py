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
            return render(request,"success.html")
        else:
            return redirect ('index')
    return render(request,"index.html")    

def loginin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            return redirect('index')  
        else:
            return render(request, 'create.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'create.html') 
    
def logout_view(request):
    logout(request)
    return redirect('index')  
        

