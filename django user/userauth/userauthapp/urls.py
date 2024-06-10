from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('',views.main,name="main"),
    path('loginin/',views.loginin,name="loginin"),




]
