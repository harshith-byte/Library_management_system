from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),     
    path('api/signup',views.savesignup,name="admin_signup"),
    path('signup',views.Administrator_signup,name="signup"),
    path('api/login',views.api_login,name="admin_login"),    
    path('api/login',views.Administrator_login,name="login"),       
]