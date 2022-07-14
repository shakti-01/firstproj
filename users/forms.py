from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required to give valid email')
    #order of form

    class Meta:
        model = User
        fields = ['username','email','password1','password2']