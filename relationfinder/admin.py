from django.contrib import admin
from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import FormData, UserExtension, Message, Relation


admin.site.register(FormData)
admin.site.register(UserExtension)
admin.site.register(Message)
admin.site.register(Relation)


# class UserAdmin(admin.ModelAdmin):
#   #  list_display = ['__str__', 'user']
#   #  search_fields = ['content', 'user__username', 'user__email']
#     # fields = ["username"]
#     class Meta:
#         model = User

# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)
