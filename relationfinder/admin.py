from django.contrib import admin
from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Card, UserExtension, Message, Relation


admin.site.register(Card)
admin.site.register(UserExtension)
admin.site.register(Message)
admin.site.register(Relation)


