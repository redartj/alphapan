import os,csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoApp.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,CrudOil,GoldGlobal,GoldKorea
import numpy as np
import pandas as pd

def test():  
    with open("./data/exrate_usdkrw_030101_230104.csv", "r", encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0], row[1], row[2])
            usd = ExRateUSDKRW.objects.get_or_create(
                date=row[0],
                lastvalue=[1],
                difference=[2]
            )
if __name__ == '__main__':  
   test()




# data = pd.read_csv("./data/exrate_usdkrw_030101_230104.csv")
# df = pd.DataFrame(data,index="date")
# print(data)