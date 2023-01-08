import os,csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoApp.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,CrudOil,GoldGlobal,GoldKorea
import numpy as np
import pandas as pd

def csv_input():  
    with open("./data/(amend)exrateusd2.csv", "r", encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            i += 1
            print(row[0], row[1], row[2])
            usd = ExRateUSDKRW.objects.get_or_create(
                date=row[0],
                lastvalue=row[1],
                difference=row[2]
            )
            print(i,'th done')

def read_db():  
    value = ExRateUSDKRW.objects.all()
    print(value)
    
if __name__ == '__main__':  
    csv_input()

