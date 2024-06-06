from django.urls import path
from demoapp.views import index,people

urlpatterns = [
    path('',index,name="index"),
    path('people/',people,name="people")
    
]
