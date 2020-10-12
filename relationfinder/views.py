from django.utils.http import is_safe_url
from django.conf import settings
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import TweetSerializer
from .algorithm import evaluate
from .forms import FormDataForm, RegisterForm
from .models import FormData
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect



# Create your views here.
def home_view22(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello</h1>')
    # print(request.user)
    return render(request, "pages/home.html", context={}, status=200)




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
    return render(request, "relfinder/home.html")

def register(request):
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

def profile(request):
    if request.user.is_authenticated:
        return render(request, "relfinder/profile.html")
    else:
        return render(request, "relfinder/home.html")

def create(request):
    if request.user.is_authenticated:
        return render(request, "relfinder/formtofill.html")
    else:
        return render(request, "relfinder/home.html")

def save_form_data(request, *args, **kwargs):
    if request.user.is_authenticated:
        form = FormDataForm(request.POST or None)
        if form.is_valid():     # check if fields were filled correctly
            obj = form.save(commit=False)   # returns object instance
            obj.user = request.user
            obj.save()
            evaluate(obj)
        else:
            print("form is invalid")
        return redirect("/profile/")   
    else:
        return render(request, "relfinder/home.html")
    
    #return redirect("/relf")
