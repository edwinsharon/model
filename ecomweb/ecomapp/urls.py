from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('seller/',views.sellerlogin,name="sellerlogin"),
    path('sellercreate/',views.createseller,name="createseller"),
    path('sellerindex/',views.sellerindex,name="sellerindex"),
    path('logout/',views.logoutseller,name="logout"),
    path('user/',views.userlogin,name="userlogin"),
    path('usersignup/',views.usersignup,name="usersignup"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('verification/<str:email>/',views.verification,name='verification'),
    path('getemail/',views.getemail,name="getemail"),
    
]
