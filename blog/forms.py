from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



