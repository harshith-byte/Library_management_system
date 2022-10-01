from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#manager for custom model 
class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class 
    """
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username :
            raise ValueError("Users must have an Username")
        user  = self.model(
                email=self.normalize_email(email),
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    
    """
      Custom user class inheriting AbstractBaseUser class 
    """
    
    email                = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username             = models.CharField(max_length=30,unique=True)
    date_joined          = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login           = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin             = models.BooleanField(default=False)
    is_active            = models.BooleanField(default=True)
    is_staff             = models.BooleanField(default=False)
    is_superuser         = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label ):
        return True

#this model is not required
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
