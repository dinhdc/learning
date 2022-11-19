from rest_framework.viewsets import ModelViewSet
from stock.models import StockCode
from stock.api.serializers import StockCodeSerializer


class StockCodeViewSet(ModelViewSet):
    queryset = StockCode.objects.all()
    serializer_class = StockCodeSerializer
    lookup_field = "uid"
    module = ["Stock Code"]
