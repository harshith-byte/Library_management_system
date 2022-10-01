from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import requests
from .models import *
from .serializers import AdministratorSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'books-list':'/adminviewapi/',  #read
        'create-book':'/api/savebook/', #create
        'updatebook':'api/updatebook/<str:pk>/', #update
    }


    return Response(api_urls)



def home(request):
    book=Books.objects.all()
    return render(request,'main/home.html',context={'book':book})

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
        try:
            Administrator.objects.get(Admin_email=Admin_email)
            return render(request, 'main/signup.html',context={'message':"This email has already taken. Try other email"})
        except ObjectDoesNotExist:
            data={'Admin_Firstname':Admin_Firstname,'Admin_Lastname':Admin_Lastname,'Admin_email':Admin_email,'Admin_password':Admin_password}
            headers={'Content-Type': 'application/json'}

            r=requests.post('http://0.0.0.0:8000/api/signup/',json=data,headers=headers)

            return render(request, 'main/signup.html')
    else:
        return render(request, 'main/signup.html')



def admin_view(request):
    book=Books.objects.all()
    return render(request,'main/adminview.html',context={'book':book})


@api_view(['GET'])
def admin_view_api(request):
    book=Books.objects.all()
    serializer=BookSerializer(book, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def savebook(request):

    if request.method=="POST":
        serialize=BookSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status.HTTP_201_CREATED)
        return Response(serialize.data, status.HTTP_400_BAD_REQUEST)


def Create_Book(request):

    if request.method=="POST":
        Book_name=request.POST.get('bookname')
        Book_author=request.POST.get('bookauthor')
        Book_prize=request.POST.get('bookprice')

        try:
            Books.objects.get(Book_name=Book_name)
            return render(request, 'main/bookcreate.html',context={'message':"this book has been created"})
        except ObjectDoesNotExist:
            data={'Book_name':Book_name,'Book_author':Book_author,'Book_prize':Book_prize}
            headers={'Content-Type': 'application/json'}

            r=requests.post('http://0.0.0.0:8000/api/savebook/',json=data,headers=headers)

            return HttpResponseRedirect(reverse('admin_view'))
    else:
        return render(request, 'main/bookcreate.html')


@api_view(['POST'])
def updatebook(request,pk):
    book=Books.objects.filter(id=pk)
    print("hello")
    if request.method=="POST":
        serialize=Books.objects.filter(id=pk).update(Book_name=request.data['Book_name'],Book_author=request.data['Book_author'],Book_prize=request.data['Book_prize'])

        serialize.save()
            
        return Response(serialize.data,status.HTTP_201_CREATED)


def update_book(request,pk):
    book=Books.objects.filter(id=pk)
    if request.method=="POST":
        Book_name=request.POST.get('bookname')
        Book_author=request.POST.get('bookauthor')
        Book_prize=request.POST.get('bookprize')

        try:
            Books.objects.get(Book_name=Book_name)
            return render(request, 'main/updatebook.html',context={'message':"this book has been created"})
        except ObjectDoesNotExist:
            data={'Book_name':Book_name,'Book_author':Book_author,'Book_prize':Book_prize}
            headers={'Content-Type': 'application/json'}
            url="http://0.0.0.0:8000/api/updatebook/"+pk+"/"
            r=requests.post(url=url,json=data,headers=headers)

            return HttpResponseRedirect(reverse('admin_view'))
    else:
        return render(request, 'main/updatebook.html',context={'book':book})


def deletebook(request,pk):
    book=Books.objects.get(id=pk)
    book.delete()
    return HttpResponseRedirect(reverse('admin_view'))