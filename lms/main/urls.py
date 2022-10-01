from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),  #student page
    path('api/',views.apioverview,name="api"), # listof all api's present in the project

    path('signup/',views.registration_view, name="signup"),# Signup, login and logout
    path('logout/',views.logout_view, name="logout" ),
    path('login/',views.login_view, name="login" ),  

    path('api/savebook/',views.savebook,name="savebook_api"),   # api and view for saving new book
    path('adminview/savebook/',views.Create_Book,name="createbook"),   

    path('adminview/',views.admin_view,name="admin_view"),      # api and view for visiting admin page    
    path('adminviewapi/',views.admin_view_api,name="admin_view_api"),

    path('api/updatebook/<str:pk>/',views.updatebook,name="updatebook_api"), #api and view for updating a particular book
    path('adminview/updatebook/<str:pk>/',views.update_book,name="updatebook"),

    path('adminview/deletebook/<str:pk>/',views.deletebook,name="deletebook"), #view for deleting particular book
]