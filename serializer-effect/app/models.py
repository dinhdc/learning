from django.db import models
from core.models import BaseCustomModel
import uuid


class RuleModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=10)
    profitability = models.BooleanField()
    activity = models.BooleanField()
    liquidity = models.BooleanField()
    debt = models.BooleanField()
    market = models.BooleanField()
    label = models.BooleanField()

    def __str__(self) -> str:
        return self.code
