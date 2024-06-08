from django.shortcuts import render
from .models import *

# Create your views here.
def authenticate(request):
    if request.method == "POST":
        

