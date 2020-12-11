from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Card, UserExtension, Message


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class DateInput(forms.DateInput):
    input_type = 'date'


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
        widgets = {
            'birth_date': DateInput(format='%Y-%m-%d')
        }


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
        exclude = ['user', 'card_name']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['written_to', 'text']
