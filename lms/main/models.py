from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class Administrator(models.Model):

    Admin_Firstname=models.CharField(max_length=100)
    Admin_Lastname=models.CharField(max_length=100)
    Admin_email=models.EmailField(unique=True, error_messages={'unique':"This email has already been registered."})
    Admin_password=models.CharField(max_length=10)
    

    def __str__(self):
        return self.Admin_Firstname + " " + self.Admin_Lastname


class Books(models.Model):

    Book_name=models.CharField(max_length=100)
    Book_author=models.CharField(max_length=100)
    Book_prize=models.IntegerField()

    def __str__(self):
        return self.Book_name + " " + self.Book_author
