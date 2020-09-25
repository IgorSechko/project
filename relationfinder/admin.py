from django.contrib import admin

# Register your models here.
from .models import FormData


class FormDataAdmin(admin.ModelAdmin):
  #  list_display = ['__str__', 'user']
  #  search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = FormData


admin.site.register(FormData, FormDataAdmin) # now in /admin site we can see and manipulate Tweet table
