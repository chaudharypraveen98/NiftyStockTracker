# filters.py
import django_filters
from django_filters import rest_framework as filters

from stock.models import StockModel

class StockFilter(django_filters.FilterSet):
    # For DecimalFields (turnover, open_price, high_price, low_price, close_price)
    turnover__gte = django_filters.NumberFilter(field_name='turnover', lookup_expr='gte')
    turnover__lte = django_filters.NumberFilter(field_name='turnover', lookup_expr='lte')
    turnover__gt = django_filters.NumberFilter(field_name='turnover', lookup_expr='gt')
    turnover__lt = django_filters.NumberFilter(field_name='turnover', lookup_expr='lt')

    open_price__gte = django_filters.NumberFilter(field_name='open_price', lookup_expr='gte')
    open_price__lte = django_filters.NumberFilter(field_name='open_price', lookup_expr='lte')
    open_price__gt = django_filters.NumberFilter(field_name='open_price', lookup_expr='gt')
    open_price__lt = django_filters.NumberFilter(field_name='open_price', lookup_expr='lt')

    high_price__gte = django_filters.NumberFilter(field_name='high_price', lookup_expr='gte')
    high_price__lte = django_filters.NumberFilter(field_name='high_price', lookup_expr='lte')
    high_price__gt = django_filters.NumberFilter(field_name='high_price', lookup_expr='gt')
    high_price__lt = django_filters.NumberFilter(field_name='high_price', lookup_expr='lt')

    low_price__gte = django_filters.NumberFilter(field_name='low_price', lookup_expr='gte')
    low_price__lte = django_filters.NumberFilter(field_name='low_price', lookup_expr='lte')
    low_price__gt = django_filters.NumberFilter(field_name='low_price', lookup_expr='gt')
    low_price__lt = django_filters.NumberFilter(field_name='low_price', lookup_expr='lt')

    close_price__gte = django_filters.NumberFilter(field_name='close_price', lookup_expr='gte')
    close_price__lte = django_filters.NumberFilter(field_name='close_price', lookup_expr='lte')
    close_price__gt = django_filters.NumberFilter(field_name='close_price', lookup_expr='gt')
    close_price__lt = django_filters.NumberFilter(field_name='close_price', lookup_expr='lt')

    # For BigIntegerField (shares_traded)
    shares_traded__gte = django_filters.NumberFilter(field_name='shares_traded', lookup_expr='gte')
    shares_traded__lte = django_filters.NumberFilter(field_name='shares_traded', lookup_expr='lte')
    shares_traded__gt = django_filters.NumberFilter(field_name='shares_traded', lookup_expr='gt')
    shares_traded__lt = django_filters.NumberFilter(field_name='shares_traded', lookup_expr='lt')
    class Meta:
        model = StockModel
        # fields = {
        #     'index_name__name': ['exact'],
        #     'shares_traded': ['exact', 'year__gt'],
        # }

        fields =['index_name__name', 'shares_traded','turnover', 'open_price', 'high_price','open_price','high_price']
