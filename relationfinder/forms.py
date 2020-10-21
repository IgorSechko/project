from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import FormData, UserExtension



class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1","password2"]


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







class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = [
            'first_name',
            'surname',
            'fathername',
            'birth_year',
            'death_year',
            'place1_x',
            'place1_y',
            'place1_radius',
            'place1_start_year',
            'place1_end_year',
            'place2_x',
            'place2_y',
            'place2_radius',
            'place2_start_year',
            'place2_end_year',
            'place3_x',
            'place3_y',
            'place3_radius',
            'place3_start_year',
            'place3_end_year',
            'information'
            ]
        exclude = ['user']

