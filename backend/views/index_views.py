from django.shortcuts import render
# import requests
from ..models import StockSnapshot


def index(request):
    stocks_last_snapshot = StockSnapshot
    return render(request, 'index.html', {})
