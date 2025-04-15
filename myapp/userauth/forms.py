from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="First Name", max_length=200)
    last_name = forms.CharField(label="Last Name", max_length=200)

    class Meta():
        model = User
        fields =[
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2"
        ]