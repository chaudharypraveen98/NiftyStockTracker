from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from stock.models import StockModel
from stock.pagination import StandardResultsSetPagination
from stock.serializers import StockSerializers

class ProductViewset(ModelViewSet):
    serializer_class = StockSerializers
    queryset = StockModel.objects.all()
    lookup_field = 'entry_id'
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    # use filter field if custom filter class is not present
    filter_fields = ('index_name__name')
    filter_class = StockModel
    search_fields = ('index_name', 'open_price','high_price')
    ordering_fields = ('date')
    pagination_class = StandardResultsSetPagination

    # It extend the url
    # @action(detail=True, methods=['GET'])
    # def det(self, request, index_name):
    #     invoice_order = StockModel.objects.filter(index_name=index_name)
    #     serializer = StockSerializers(invoice_order, many=True)
    #     return Response(serializer.data, status=200)