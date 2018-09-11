from django.shortcuts import render
# import requests
from ..models import StockSnapshot
from ..models import Stock


def index(request):
    stocks_last_snapshot = StockSnapshot.objects.all()
    all_stocks = Stock.objects.all()
    return render(request, 'index.html', {
        'all_stocks': all_stocks,
        'stocks_last_snapshot': stocks_last_snapshot
        })
