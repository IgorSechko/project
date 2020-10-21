from django.utils.http import is_safe_url
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import TweetSerializer
from .algorithm import evaluate
from .forms import FormDataForm, RegisterForm, UserExtensionRegForm, UserExtensionEditForm
from .models import FormData, UserExtension, Relation
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect



# # Create your views here.
# def home_view22(request, *args, **kwargs):
#     # return HttpResponse('<h1>Hello</h1>')
#     # print(request.user)
#     return render(request, "pages/home.html", context={}, status=200)

# def create_form_hhh(request, *args, **kwargs):
#     user = request.user
#     if not request.user.is_authenticated:
#         user = None
#         if request.is_ajax():
#             return JsonResponse({}, status=401)
#         return redirect(settings.LOGIN_URL)
#     form = TweetForm(request.POST or None)
#     next_url = request.POST.get("next") or None
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = user
#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(), status=201)
#         if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
#             return redirect(next_url)
#         form = TweetForm()
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors, status = 400)
#     return render(request, "components/form.html", context = {"form": form})

# def index(request):
#     return render(request, "relationfinder/index.html")

def home(request):
    return redirect('login_or_register')

@login_required(login_url='login')
def profile(request):
    return render(request, "relfinder/profile_main.html")

@login_required(login_url='login')
def profilesettings(request):
    userEx = request.user.userExtension
    form = UserExtensionEditForm(instance=userEx)
    if request.method == 'POST':
        form = UserExtensionEditForm(request.POST, request.FILES, instance=userEx)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Форма заполнена неверно")
    return render(request, "relfinder/profile_settings.html", {'form':form})

@login_required(login_url='login')
def similarities(request):
    return render(request, "relfinder/profile_similarities.html")
    
@login_required(login_url='login')
def mycards(request):
    return render(request, "relfinder/profile_mycards.html")

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                print("form is valid")
                form.save()
                return redirect('home')
            else:
                print("form is INvalid")
                return HttpResponse("Form is invalid")
        else:
            form = RegisterForm()
            return render(request, "relfinder/register.html", {"form": form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    form = AuthenticationForm()
    return render(request, 'relfinder/login.html', {'form': form})


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

def login_or_register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            reqType = request.POST.get('type')
            if reqType == 'login':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username,password=password)
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
                'userExRegForm':userExRegForm
                }
            return render(request, 'relfinder/login_or_register.html', context=context)


@login_required(login_url='login')
def create(request):
    return render(request, "relfinder/formtofill.html")


@login_required(login_url='login')
def save_form_data(request, *args, **kwargs):
    form = FormDataForm(request.POST or None)
    if form.is_valid():                 # check if fields were filled correctly
        obj = form.save(commit=False)   # returns object instance
        obj.user = request.user
        obj.save()
        evaluate(obj)
    else:
        return HttpResponse("Форма заполнена некорректно")
    return redirect("/profile")   


@login_required(login_url='login')
def get_user(request, pk):
    user = User.objects.get(id=pk)
    return render(request, "relfinder/test.html", {'user': user})

@login_required(login_url='login')
def usersearch(request):
    users = User.objects.all().exclude(id=request.user.id)    
    return render(request, "relfinder/profile_usersearch.html", {'users': users})


@login_required(login_url='login')
def messages(request):
    wbmessages = request.user.wbMessages_set
    wtmessages = request.user.wtMessages_set
    return render(request, "relfinder/profile_messages.html", {'wbmessages': wbmessages,'wtmessages': wtmessages,})


