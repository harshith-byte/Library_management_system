from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),  
    path('api/',views.apioverview,name="api"),

    path('api/signup/',views.savesignup,name="admin_signup"),
    path('signup/',views.Administrator_signup,name="signup"),
    path('api/login/',views.api_login,name="admin_login"),    
    path('api/login/',views.Administrator_login,name="login"),    

    path('api/savebook/',views.savebook,name="savebook_api"),      
    path('adminview/savebook/',views.Create_Book,name="createbook"),   

    path('adminview/',views.admin_view,name="admin_view"),
    path('adminviewapi/',views.admin_view_api,name="admin_view_api"),

    path('api/updatebook/<str:pk>/',views.updatebook,name="updatebook_api"),
    path('adminview/updatebook/<str:pk>/',views.update_book,name="updatebook"),

    path('adminview/deletebook/<str:pk>/',views.deletebook,name="deletebook"),
]