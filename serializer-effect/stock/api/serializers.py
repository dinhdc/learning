from rest_framework import serializers
from stock.models import StockCode, StockPerDay
from app.models import RuleModel


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


class StockPerDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = StockPerDay
        exclude = ('id',)

    def create(self, validated_data):
        stock = StockPerDay.objects.create(**validated_data)
        profitability = True if validated_data["net_profit"] / \
            validated_data["total_asset"] > 1 else False
        activity = True if validated_data["revenue"] / \
            validated_data["total_asset"] > 1 else False
        liquidity = True if validated_data["current_asset"] / \
            validated_data["current_debt"] > 1 else False
        debt = True if validated_data["total_liabilities"] / \
            validated_data["total_asset"] > 1 else False
        martket = True if validated_data["price"] / \
            validated_data["eps"] > 1 else False
        try:
            rule = RuleModel.objects.filter(profitability=profitability).filter(
                activity=activity).filter(liquidity=liquidity).filter(debt=debt).filter(martket)
            if rule.count() > 0:
                rule = rule.last()
                stock.label = rule.label
                stock.save()
        except Exception:
            stock.label = False
            stock.save()
        return stock


class StockPerDayGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockPerDay
        exclude = ('id',)
        depth = 2
