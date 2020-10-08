from django.contrib import admin
from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import FormData, UserDetails


class FormDataAdmin(admin.ModelAdmin):
  #  list_display = ['__str__', 'user']
  #  search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = FormData


class UserDetailsAdmin(admin.ModelAdmin):
  #  list_display = ['__str__', 'user']
  #  search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = UserDetails


class UserAdmin(admin.ModelAdmin):
  #  list_display = ['__str__', 'user']
  #  search_fields = ['content', 'user__username', 'user__email']
    # fields = ["username"]
    class Meta:
        model = User

admin.site.register(FormData, FormDataAdmin) # now in /admin site we can see and manipulate Tweet table
admin.site.register(UserDetails, UserDetailsAdmin)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)