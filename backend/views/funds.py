from django.shortcuts import render
from itertools import groupby
from ..models import FundSnapshot
# from ..models import Stock


def index(request):
    fund_snapshots = FundSnapshot.objects.all().order_by('date')
    list_of_funds_snapshots = \
        [list(g) for t, g in groupby(fund_snapshots, key=extract_date)]
    unique_snapshots = FundSnapshot.objects\
        .order_by().values('date').distinct()
    return render(request, 'funds/funds_index.html', {
        'list_of_funds_snapshots': list_of_funds_snapshots,
        'unique_snapshots': unique_snapshots
        })


def fund_detail(request):
    fund = 'fund id'
    positions = StockSnapshot.objects.filter(ISIN=fund).order_by('date')
    return render(request, 'funds/fund_detail.html', {
        'fund': fund,
        'positions': positions
    })


# AUX FUNCTIONS

def extract_date(entity):
    'extracts the starting date from an entity'
    return entity.start_time.date()
