from django.utils.http import is_safe_url
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .algorithm import evaluate
from .forms import CardForm, RegisterForm, UserExtensionRegForm, UserExtensionEditForm
from .models import Card, UserExtension, Relation
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect


@login_required(login_url='login_or_register')
def profile(request):
    return render(request, "relfinder/profile_main.html")


@login_required(login_url='login_or_register')
def profilesettings(request):
    userEx = request.user.userExtension
    form = UserExtensionEditForm(instance=userEx)
    if request.method == 'POST':
        form = UserExtensionEditForm(
            request.POST, request.FILES, instance=userEx)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Форма заполнена неверно")
    return render(request, "relfinder/profile_settings.html", {'form': form})


@login_required(login_url='login_or_register')
def similarities(request):
    all_relations = Relation.objects.all()
    user_relations = all_relations.filter(referenced_by__user=request.user)

    return render(request, "relfinder/profile_similarities.html", {'user_relations': user_relations})


@login_required(login_url='login_or_register')
def mycards(request):
    return render(request, "relfinder/profile_mycards.html")


@login_required(login_url='login_or_register')
def logoutUser(request):
    logout(request)
    return redirect('login_or_register')


def login_or_register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            reqType = request.POST.get('type')
            if reqType == 'login':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
                else:
                    return HttpResponse("the user doesn't exist")

            elif reqType == 'register':
                userRegForm = RegisterForm(request.POST)
                userExRegForm = UserExtensionRegForm(request.POST)
                if userRegForm.is_valid() and userExRegForm.is_valid():
                    user = userRegForm.save()
                    userEx = userExRegForm.save(commit=False)
                    userEx.user = user
                    userEx.save()
                    return redirect('login_or_register')
                else:
                    return HttpResponse("Form is invalid")

            else:
                return HttpResponse("an error occurred")

        else:
            authForm = AuthenticationForm()
            userRegForm = RegisterForm()
            userExRegForm = UserExtensionRegForm()
            context = {
                'authForm': authForm,
                'userRegForm': userRegForm,
                'userExRegForm': userExRegForm
            }
            return render(request, 'relfinder/login_or_register.html', context=context)


@login_required(login_url='login_or_register')
def create(request):
    return render(request, "relfinder/profile_createcard.html")


@login_required(login_url='login_or_register')
def save_form_data(request, *args, **kwargs):
    form = CardForm(request.POST or None)
    if form.is_valid():                 # check if fields were filled correctly
        print(form.cleaned_data)
        obj = form.save(commit=False)   # returns object instance
        obj.user = request.user
        obj.save()
        evaluate(obj)
    else:
        return HttpResponse("Форма заполнена некорректно")
    print("just before redirection back to profile")
    return redirect("profile")


@login_required(login_url='login_or_register')
def get_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except ObjectDoesNotExist:
        return HttpResponse("Пользователь не существует")

    return render(request, "relfinder/profile_viewuser.html", {'user': user})


@login_required(login_url='login_or_register')
def viewcard(request, pk):
    try:
        card = Card.objects.get(id=pk)
    except ObjectDoesNotExist:
        return HttpResponse("Карточка не существует")

    return render(request, "relfinder/profile_viewcard.html", {'card': card})


@login_required(login_url='login_or_register')
def usersearch(request):
    users = User.objects.all().exclude(id=request.user.id)
    return render(request, "relfinder/profile_usersearch.html", {'users': users})


@login_required(login_url='login_or_register')
def messages(request):
    wbmessages = request.user.wbMessages_set
    wtmessages = request.user.wtMessages_set
    return render(request, "relfinder/profile_messages.html", {'wbmessages': wbmessages, 'wtmessages': wtmessages, })

