from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.

def home_redirect(request):
    context = ""
    if request.user.is_authenticated:
        context = ["IN",request.user.username,request.user.password,request.user.id]
    else:
        context = "OUT"
    return render(request, "register/home.html", {"corn": context})
    #return redirect("/register")


def register(request):
    print(request.path)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
        else:
            print("form is INvalid")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})
