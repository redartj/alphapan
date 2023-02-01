from django.contrib import admin
from .models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,ExRateEURKRW,ExRateCNYKRW,CrudOil,GoldGlobal,GoldKorea,PFKStocks,PFBonds

# Register your models here.
admin.site.register(Kospi)
admin.site.register(Kosdaq)
admin.site.register(ExRateUSDKRW)
admin.site.register(ExRateJPYKRW)
admin.site.register(ExRateEURKRW)
admin.site.register(ExRateCNYKRW)
admin.site.register(CrudOil)
admin.site.register(GoldGlobal)
admin.site.register(GoldKorea)

admin.site.register(PFKStocks)
admin.site.register(PFBonds)
