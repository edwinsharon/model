from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('verification/',views.verification,name='verification'),
    path('getemail/',views.getemail,name="getemail"),
    path('addproduct/',views.addproduct,name="additem"),
    path('delete_g/<int:pk>',views.delete_g,name="delete"),
    path('edit_g/<int:pk>',views.edit_g,name="edit"),  
    path('productsdispaly/<int:pk>',views.productsdisplay,name="productsdisplay"),
    
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
