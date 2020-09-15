from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, "pages/home.html", context={}, status=200)

    
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        # "image": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        #raise Http404
        data['message'] = "Not Found"
        status = 404
    
    return JsonResponse(data, status=status)
    #return HttpResponse(f'<h1>Hello {tweet_id} - {obj.content}</h1>')