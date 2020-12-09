import django_filters

from .models import *

class UserExtFilter(django_filters.FilterSet):
    class Meta:
        model = UserExtension
        fields = [
            'first_name',
            'surname',
            'fathername',
        ]