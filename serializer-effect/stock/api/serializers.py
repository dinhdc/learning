from rest_framework import serializers
from stock.models import StockCode


class StockCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockCode
        exclude = ('id',)

    def validate(self, data):
        if data['company'] is None or len(data['company']) == 0:
            raise serializers.ValidationError(
                'company cannot be null'
            )
        if data['date_of_incorporation'] is None:
            raise serializers.ValidationError(
                'date of incorporation in cannot be null'
            )
        return data
