from django.shortcuts import render
<<<<<<< HEAD
from itertools import groupby
from ..models import StockSnapshot
=======
from itertools import groupby, count
from ..models import FundSnapshot
>>>>>>> feature--stocks
# from ..models import Stock


def index(request):
<<<<<<< HEAD
    stocks_snapshots = StockSnapshot.objects.all().order_by('date')
    list_of_stocks_snapshots = \
        [list(g) for t, g in groupby(stocks_snapshots, key=extract_date)]
    unique_snapshots = StockSnapshot.objects\
        .order_by().values('date').distinct()
    return render(request, 'funds/funds_index.html', {
        'list_of_stocks_snapshots': list_of_stocks_snapshots,
        'unique_snapshots': unique_snapshots
=======
    fund_snapshots = FundSnapshot.objects.all().order_by('date')
    list_of_funds_snapshots = \
        [list(g) for t, g in groupby(fund_snapshots, key=extract_date)]
    iterator = count()
    # print(list_of_funds_snapshots[0][0].fund.ISIN)
    return render(request, 'funds/funds_index.html', {
        'list_of_funds_snapshots': list_of_funds_snapshots,
        'iterator': iterator
>>>>>>> feature--stocks
        })


def fund_detail(request):
    fund = 'fund id'
<<<<<<< HEAD
    positions = StockSnapshot.objects.filter(ISIN=fund).order_by('date')
=======
    positions = FundSnapshot.objects.filter(ISIN=fund).order_by('date')
>>>>>>> feature--stocks
    return render(request, 'funds/fund_detail.html', {
        'fund': fund,
        'positions': positions
    })


# AUX FUNCTIONS

def extract_date(entity):
    'extracts the starting date from an entity'
<<<<<<< HEAD
    return entity.start_time.date()
=======
    return entity.date.date()
>>>>>>> feature--stocks
