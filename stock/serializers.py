from rest_framework import serializers

from stock.models import StockModel


class StockSerializers(serializers.ModelSerializer):

    class Meta:
        model = StockModel
        fields = '__all__'
        # depth=1
        # It will also work and includes all the field but we don't want the rate and the item field as they are
        # already present in the product field
        # exclude = []