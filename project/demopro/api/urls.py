from django.urls import path
from demoapp.views import index

urlpatterns = [
    path('',index,name="index"),
]
