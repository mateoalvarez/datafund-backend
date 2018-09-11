from django.db import models
import datetime
from datetime import date


class Stock(models.Model):
    ISIN = models.CharField(max_length=14)
    date = models.DateTimeField(date)
    stock_exchange = models.CharField(max_length=15)
    stock_currency = models.CharField(max_length=3)
    stock_company = models.CharField(max_length=50)
    stock_name = models.CharField(max_length=50)


class Fund(models.Model):
    ISIN = models.CharField(max_length=14)
    fund_name = models.CharField(max_length=50)
    fund_country = models.CharField(max_length=3)
    fund_type = models.CharField(max_length=30)
    fund_objective = models.CharField(max_length=30)


class StockSnapshot(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    date = models.DateTimeField(date)
    stock_snapshot_adjusted_close = models.FloatField()
    stock_snapshot_close = models.FloatField()
    stock_snapshot_volume = models.FloatField()
    stock_snapshot_high = models.FloatField()
    stock_snapshot_low = models.FloatField()
    stock_snapshot_is_quarter_snapshot = models.BooleanField(default=False)


class FundSnapshot(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.PROTECT)
    date = models.DateTimeField(date)
    fund_snapshot_value = models.FloatField()
    fund_snapshot_comment = models.CharField(max_length=50000)
    fund_snapshot_is_quarter_snapshot = models.BooleanField(default=False)


class FundPositionSnapshot(models.Model):
    fund_snapshot = models.ForeignKey(FundSnapshot, on_delete=models.PROTECT)
    stock_snapshot = models.ForeignKey(StockSnapshot, on_delete=models.PROTECT)
    position_percentage = models.FloatField()
    position_quantity = models.FloatField()
    position_currency = models.CharField(max_length=3)
