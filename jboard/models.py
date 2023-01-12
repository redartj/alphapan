from django.db import models
from django.contrib.auth.models import User

## Jboard
    #  Daily
class Kospi(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    startvalue = models.FloatField()
    highvalue = models.FloatField()
    lowvalue = models.FloatField()
    volume = models.FloatField()
    tranaction = models.BigIntegerField()
    marketcap = models.BigIntegerField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}, {self.startvalue}, {self.highvalue}, {self.lowvalue}, {self.volume}, {self.tranaction}, {self.marketcap}"



class Kosdaq(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    startvalue = models.FloatField()
    highvalue = models.FloatField()
    lowvalue = models.FloatField()
    volume = models.FloatField()
    tranaction = models.BigIntegerField()
    marketcap = models.BigIntegerField()

    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}, {self.startvalue}, {self.highvalue}, {self.lowvalue}, {self.volume}, {self.tranaction}, {self.marketcap}"



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


class GoldKorea(models.Model):
    date = models.DateField()
    lastvalue = models.FloatField()
    difference = models.FloatField()
    startvalue = models.FloatField()
    highvalue = models.FloatField()
    lowvalue = models.FloatField()
    
    def __str__(self):
        return f"{self.date}, {self.lastvalue}, {self.difference}, {self.startvalue}, {self.highvalue}, {self.lowvalue}"


    # Macro

## Portfolio
