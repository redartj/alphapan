from django.contrib import admin
from .models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,CrudOil,GoldGlobal,GoldKorea

# Register your models here.
admin.site.register(Kospi)
admin.site.register(Kosdaq)
admin.site.register(ExRateUSDKRW)
admin.site.register(ExRateJPYKRW)
admin.site.register(CrudOil)
admin.site.register(GoldGlobal)
admin.site.register(GoldKorea)