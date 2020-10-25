import django_filters
from django_filters import DateFilter,CharFilter

from .models import *

class ItemFilter(django_filters.FilterSet):

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['price','image']
        