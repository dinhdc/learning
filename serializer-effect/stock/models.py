from core.models import BaseCustomModel
from django.db import models


class StockCode(BaseCustomModel):
    code = models.CharField(max_length=40)
    company = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_of_incorporation = models.DateField()  # ngay thanh lap

    def __str__(self) -> str:
        return self.code
