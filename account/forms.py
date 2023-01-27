from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms

class SigninForm (forms.Form):
    first_name = forms.CharField(max_length=255, label = "Имя") 
    last_name = forms.CharField(max_length=255, label = "Фамилия") 
    username = forms.CharField(max_length=255, label = "Имя пользователя")
    password = forms.CharField(max_length=255, label = "Пароль")
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset = Group.objects.all())

class LoginForm (forms.Form):
    username = forms.CharField(max_length=255, label = "Имя пользователя")
    password = forms.CharField(max_length=255, label = "Пароль")


