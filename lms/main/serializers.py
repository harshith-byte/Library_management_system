from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Administrator, Books

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administrator
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"