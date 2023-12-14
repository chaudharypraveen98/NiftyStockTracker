from django.contrib import admin

from stock.models import IndexModel, StockModel

admin.site.register(StockModel)
admin.site.register(IndexModel)