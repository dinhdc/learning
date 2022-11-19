from rest_framework.viewsets import ModelViewSet
from stock.models import StockCode, StockPerDay
from stock.api.serializers import StockCodeSerializer, StockPerDaySerializer, StockPerDayGetSerializer
from rest_framework.response import Response


class StockCodeViewSet(ModelViewSet):
    queryset = StockCode.objects.all()
    serializer_class = StockCodeSerializer
    lookup_field = "uid"
    module = ["Stock Code"]


class StockPerDayViewSet(ModelViewSet):
    queryset = StockPerDay.objects.all()
    serializer_class = StockPerDaySerializer
    lookup_field = "uid"
    module = ["Stock Price"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StockPerDayGetSerializer
        return StockPerDaySerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = StockPerDaySerializer(data=data)
        if serializer.is_valid():
            stock = serializer.save()
            return Response(StockPerDayGetSerializer(stock).data, status=201)
        return Response(request.data, status=400)
