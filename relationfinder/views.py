from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse




# Create your views here.
def home_view22(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello</h1>')
    # print(request.user)
    return render(request, "pages/home.html", context={}, status=200)



def index(request):
    return render(request, "relationfinder/index.html")