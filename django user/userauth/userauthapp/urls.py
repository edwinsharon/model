from django.urls import path
from . import views

urlpatterns = [
    path('',views.userlogin,name="userlogin"),
    path('login/',views.createuser,name="createuser"),
    path('logout/', views.logout_view, name='logout'),
  
]
