from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

# Create your models here.

class Administrator(models.Model):

    Admin_Firstname=models.CharField(max_length=100)
    Admin_Lastname=models.CharField(max_length=100)
    Admin_email=models.EmailField(unique=True)
    Admin_password=models.CharField(max_length=10)
    

    def __str__(self):
        return self.Admin_Firstname + " " + self.Admin_Lastname


