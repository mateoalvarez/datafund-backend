from django.db import models
import datetime
from datetime import date

class Stock(models.Model):
    ISIN = models.CharField(max_length=14)
    date = models.DateTimeField(date)
    exchange = models.CharField(max_length=3)
    company = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Fund(models.Model):
    ISIN = models.CharField(max_length=14)
    fund_name = models.CharField(max_length=50)
    fund_country = models.CharField(max_length=3)

class StockSnapshot(models.Model):
    stock = models.ForeignKey(Stock)
    date = models.DateTimeField(date)
    value = models.FloatField()

class FundSnapshot(models.Model):
    fund = models.ForeignKey(Fund)
    date = models.DateTimeField(date)
    value = models.FloatField()
    comment = models.CharField(max_length=50000)

class FundSnapshotStockSnapshot(models.Model):
    fund_snapshot = models.ForeignKey(FundSnapshot)
    stock_snapshot = models.ForeignKey(StockSnapshot)
