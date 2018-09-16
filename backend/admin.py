from django.contrib import admin
from .models import Stock, Fund, StockSnapshot, FundSnapshot, FundPositionSnapshot

admin.site.register(Stock)
admin.site.register(Fund)
admin.site.register(StockSnapshot)
admin.site.register(FundSnapshot)
admin.site.register(FundPositionSnapshot)
