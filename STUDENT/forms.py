from django.contrib.auth.forms import UserCreationForm
from .models import User,Student
from django import forms

class RegisterForm(UserCreationForm):
     username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}))
     firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter firstname'}))
     lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter lastname'}))
     email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}))
     password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password'}))
     password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}))
   
     class Meta:
        model=User
        #fields="__all__"
        fields=["username","email","password1","password2","firstname","lastname"]

 