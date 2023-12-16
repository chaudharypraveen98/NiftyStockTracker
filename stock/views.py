from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from stock.filters import StockFilter
from stock.models import StockModel
from stock.pagination import StandardResultsSetPagination
from stock.serializers import StockSerializers


class ProductViewset(ModelViewSet):
    serializer_class = StockSerializers
    queryset = StockModel.objects.all().order_by('date')
    lookup_field = 'entry_id'
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    #filterset_fields = ['index_name__name', 'shares_traded','turnover', 'open_price', 'high_price','open_price','high_price']
    filterset_class = StockFilter
    search_fields = ('index_name__name', 'open_price', 'high_price')
    ordering_fields = ('date',)
    pagination_class = StandardResultsSetPagination
