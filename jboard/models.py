from django.db import models
from django.contrib.auth.models import User

# Main

## Daily
# 국내 시장 - Kospi,Kosdaq,Gold
class LocalMarket(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    diffrate = models.FloatField()
    startvalue = models.FloatField()
    highvalue = models.FloatField()
    lowvalue = models.FloatField()
    volume = models.FloatField()
    tranaction = models.BigIntegerField()
    marketcap = models.BigIntegerField()
    market_type = models.CharField(max_length=30)

    def __str__(self):
        return f"날짜:{self.date}, 종가:{self.lastvalue}, 변화:{self.difference}, 변화율:{self.diffrate}, 시가:{self.startvalue}, 고가:{self.highvalue}, 저가:{self.lowvalue}, 거래량:{self.volume}, 거래대금:{self.tranaction}, 시가총액:{self.marketcap}"

class Kospi(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    diffrate = models.FloatField()
    startvalue = models.FloatField()
    highvalue = models.FloatField()
    lowvalue = models.FloatField()
    volume = models.FloatField()
    tranaction = models.BigIntegerField()
    marketcap = models.BigIntegerField()

    def __str__(self):
        return f"날짜:{self.date}, 종가:{self.lastvalue}, 변화:{self.difference}, 변화율:{self.diffrate}, 시가:{self.startvalue}, 고가:{self.highvalue}, 저가:{self.lowvalue}, 거래량:{self.volume}, 거래대금:{self.tranaction}, 시가총액:{self.marketcap}"

class Kosdaq(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    diffrate = models.FloatField()
    startvalue = models.FloatField()
    highvalue = models.FloatField()
    lowvalue = models.FloatField()
    volume = models.FloatField()
    tranaction = models.BigIntegerField()
    marketcap = models.BigIntegerField()

    def __str__(self):
        return f"날짜:{self.date}, 종가:{self.lastvalue}, 변화:{self.difference}, 변화율:{self.diffrate}, 시가:{self.startvalue}, 고가:{self.highvalue}, 저가:{self.lowvalue}, 거래량:{self.volume}, 거래대금:{self.tranaction}, 시가총액:{self.marketcap}"

class GoldKorea(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    startvalue = models.FloatField()
    highvalue = models.FloatField()
    lowvalue = models.FloatField()
    
    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}, {self.startvalue}, {self.highvalue}, {self.lowvalue}"

# 국내 환시장
class ExRate(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    Curr_Type=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"

class ExRateUSDKRW(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"

class ExRateJPYKRW(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"

class ExRateEURKRW(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"

class ExRateCNYKRW(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"

# 원자재 시장 - crudoil,gold,copper
class MaterialMarket(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    market_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"

class CrudOil(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"


class GoldGlobal(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"

class CopperGlobal(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}"


## Macro
# Portfolio
class PFKStocks(models.Model):
    code = models.CharField(max_length=30)
    buyprice = models.IntegerField()
    buynum = models.IntegerField()
    date = models.DateField()

    # def __str__(self):
    #     return "f{self.code}, {self.buyprice}, {self.buynum}, {self.date}"

class PFBonds(models.Model):
    code = models.CharField(max_length=30)
    buyprice = models.IntegerField()
    buynum = models.IntegerField()
    date = models.DateField()

class PFExrate(models.Model):
    curr_type = models.IntegerField()
    buyprice = models.IntegerField()
    buynum = models.IntegerField()
    date = models.DateField()

class PFUSStocks(models.Model):
    code = models.CharField(max_length=30)
    buyprice = models.IntegerField()
    buynum = models.IntegerField()
    date = models.DateField()



    # def __str__(self):
    #     return "f{self.code}, {self.buyprice}, {self.buynum}, {self.date}"


    # def save(self, *args, **kwargs):
    #     print(self.start_date.isocalendar()[1])
    #     if self.week_number == "":
    #         self.week_number = self.start_date.isocalendar()[1]
    #     super().save(*args,**kwargs)

    # spot price
    # class rt_01125_3909(models.Model):
    #     lastvalue = models.FloatField()