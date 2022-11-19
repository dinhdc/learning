from rest_framework import serializers
from app.models import RuleModel


class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RuleModel
        exclude = ('id',)
