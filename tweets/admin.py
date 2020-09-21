from django.contrib import admin

# Register your models here.
from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin) # now in /admin site we can see and manipulate Tweet table
