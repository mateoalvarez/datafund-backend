from django.shortcuts import render
from itertools import groupby, count
from ..models import FundSnapshot
# from ..models import Stock


def index(request):
    fund_snapshots = FundSnapshot.objects.all().order_by('date')
    list_of_funds_snapshots = \
        [list(g) for t, g in groupby(fund_snapshots, key=extract_date)]
    iterator = count()
    # print(list_of_funds_snapshots[0][0].fund.ISIN)
    return render(request, 'funds/funds_index.html', {
        'list_of_funds_snapshots': list_of_funds_snapshots,
        'iterator': iterator
        })


def fund_detail(request):
    fund = 'fund id'
    positions = FundSnapshot.objects.filter(ISIN=fund).order_by('date')
    return render(request, 'funds/fund_detail.html', {
        'fund': fund,
        'positions': positions
    })


# AUX FUNCTIONS

def extract_date(entity):
    'extracts the starting date from an entity'
    return entity.date.date()
