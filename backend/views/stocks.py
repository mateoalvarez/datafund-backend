from django.shortcuts import render
from itertools import groupby
from ..models import StockSnapshot
# from ..models import Stock


def index(request):
    cosa='cosa'
    return render('stocks/stocks_index.html', {
        'cosa':cosa
    })
