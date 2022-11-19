from core.models import BaseCustomModel
from django.db import models


class StockCode(BaseCustomModel):
    code = models.CharField(max_length=40)
    company = models.TextField()
    date_of_incorporation = models.DateField()  # ngay thanh lap

    def __str__(self) -> str:
        return self.code


class StockPerDay(BaseCustomModel):
    stock = models.ForeignKey(StockCode, to_field="uid", on_delete=models.SET_NULL, null=True)
    net_profit = models.BigIntegerField()  # lợi nhuận ròng
    total_asset = models.BigIntegerField()  # tổng tài sản
    revenue = models.BigIntegerField()  # tổng doanh thu
    current_asset = models.BigIntegerField()  # tài sản hiện tại
    current_debt = models.BigIntegerField()  # nợ hiện tại
    total_liabilities = models.BigIntegerField()  # tổng nợ
    price = models.IntegerField()  # giá chứng khoán
    eps = models.IntegerField()  # lợi nhuận trên 1 cổ phiếu
    # nhãn đánh giá mã cổ phiếu cuốn hút hay không
    label = models.BooleanField(default=False)

    def __str__(self):
        return "ATTRACTIVE" if self.label is True else "NON_ATTRACTIVE"