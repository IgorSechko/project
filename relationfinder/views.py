from django.utils.http import is_safe_url
from django.conf import settings
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import TweetSerializer
from .algorithm import evaluate
from .forms import FormDataForm
from .models import FormData
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect



# Create your views here.
def home_view22(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello</h1>')
    # print(request.user)
    return render(request, "pages/home.html", context={}, status=200)


def create_form(request, *args, **kwargs):
    form = FormDataForm(request.POST or None)
    if form.is_valid():     # check if fields were filled correctly
        obj = form.save()   # returns object instance
        evaluate(obj)
    return redirect("/relf")

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



def index(request):
    return render(request, "relationfinder/index.html")