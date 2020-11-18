from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import Card, UserExtension


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class UserExtensionEditForm(forms.ModelForm):
    class Meta:
        model = UserExtension
        fields = [
            'first_name',
            'surname',
            'fathername',
            'birth_date',
            'information',
            'photo',
        ]


class UserExtensionRegForm(forms.ModelForm):
    class Meta:
        model = UserExtension
        fields = [
            'first_name',
            'surname',
            'fathername',
            'birth_date',
        ]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        exclude = ['user','card_name']
