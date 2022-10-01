from django.shortcuts import render
import requests
from .models import Administrator
from .serializers import AdministratorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def api_login(request):
    return render(request, 'main/login.html')

def Administrator_login(request):
    return render(request, 'main/login.html')


@api_view(['POST'])
def savesignup(request):
    if request.method=="POST":
        serialize=AdministratorSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status.HTTP_201_CREATED)
        return Response(serialize.data, status.HTTP_400_BAD_REQUEST)

def Administrator_signup(request):
    if request.method=="POST":
        Admin_Firstname=request.POST.get('firstname')
        Admin_Lastname=request.POST.get('lastname')
        Admin_email=request.POST.get('Email')
        Admin_password=request.POST.get('Password')

        data={'Admin_Firstname':Admin_Firstname,'Admin_Lastname':Admin_Lastname,'Admin_email':Admin_email,'Admin_password':Admin_password}
        headers={'Content-Type': 'application/json'}

        r=requests.post('http://0.0.0.0:8000/api/signup',json=data,headers=headers)

        return render(request, 'main/signup.html')
    else:
        return render(request, 'main/signup.html')