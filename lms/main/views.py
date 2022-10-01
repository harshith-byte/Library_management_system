
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import requests
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .backend import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from .forms import RegistrationForm
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
# Create your views here.



@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'books-list':'/adminviewapi/',  #read
        'create-book':'/api/savebook/', #create
        'updatebook':'api/updatebook/<str:pk>/', #update
    }
    return Response(api_urls)


@unauthenticated_user
def registration_view(request):      # signup function

    form = RegistrationForm()
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created '+ user)
            return redirect('login')
        else:
            messages.error(request, "Please Correct Below Errors")
            context = {'form':form}
    else:
        
        context = {'form':form}
    return render(request, "main/signup.html", context)



def logout_view(request):       #logout function
    logout(request)
    return redirect('home')



@unauthenticated_user
def  login_view(request):       #login function

    if request.method=='POST':
        email   = request.POST.get('email')
        password = request.POST.get('password')
        user =  authenticate(request,email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect('admin_view')
        else:
            messages.error(request,"Email or password is incorrect")
    
        
    return render(request, "main/login.html")

def home(request):          #students page
    book=Books.objects.all()
    return render(request,'main/home.html',context={'book':book})

@login_required(login_url='login') 
def admin_view(request):    #admin page
    book=Books.objects.all()
    return render(request,'main/adminview.html',context={'book':book})



@api_view(['GET'])
def admin_view_api(request):    #admin page api
    book=Books.objects.all()
    serializer=BookSerializer(book, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def savebook(request):  #creating book api

    if request.method=="POST":
        serialize=BookSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status.HTTP_201_CREATED)
        return Response(serialize.data, status.HTTP_400_BAD_REQUEST)

@login_required(login_url='login')
def Create_Book(request):   #view for creating books

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
def updatebook(request,pk): #api to update book
    book=Books.objects.filter(id=pk)
    print("hello")
    if request.method=="POST":
        serialize=Books.objects.filter(id=pk).update(Book_name=request.data['Book_name'],Book_author=request.data['Book_author'],Book_prize=request.data['Book_prize'])

        serialize.save()
            
        return Response(serialize.data,status.HTTP_201_CREATED)

@login_required(login_url='login')
def update_book(request,pk):    #view to update book
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

@login_required(login_url='login')  
def deletebook(request,pk):         #view to delete books
    book=Books.objects.get(id=pk)
    book.delete()
    return HttpResponseRedirect(reverse('admin_view'))