from dataclasses import fields
from django.contrib.auth.views import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from .models import *
from django.contrib.auth.views import LoginView
User = get_user_model()



class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","username")  
        field_classes = {"username": UsernameField}

class User_change(UserChangeForm):
     class Meta:
        model = User
        fields = ("img","first_name","last_name","username","email", "bio", "facebook", "instagram", "telegram", "pinterest", "website")  
        field_classes = {"username": UsernameField}

