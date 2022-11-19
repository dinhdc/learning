from rest_framework.viewsets import ModelViewSet
from app.models import RuleModel
from app.api.serializers import RuleSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status


class RuleViewSet(ModelViewSet):
    pagination_class = LimitOffsetPagination
    queryset = RuleModel.objects.all()
    serializer_class = RuleSerializer
    lookup_field = "uid"
    module = ["Rule Table"]

    def list(self, request, *args, **kwargs):
        if request.GET.get('limit') is not None and request.GET.get('offset') is not None:
            return super().list(request, *args, **kwargs)
        else:
            rules = RuleModel.objects.all()
            return Response({"results": RuleSerializer(rules, many=True).data, "count": rules.count()}, status=status.HTTP_200_OK)
