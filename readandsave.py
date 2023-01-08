import os,csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoApp.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,CrudOil,GoldGlobal,GoldKorea
import numpy as np
import pandas as pd

def csv_input():  
    with open("./data/gold_140324_230104.csv", "r", encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            i += 1
            print(row[0], row[1], row[2])
            GoldKorea.objects.get_or_create(
                date=row[0],
                lastvalue=row[1],
                difference=row[2],
                startvalue=row[3],
                highvalue=row[4],
                lowvalue=row[5]
            )
            print(i,'th done')

# def csv_input():  
#     with open("./data/Kosdaq(030101_230105).csv", "r", encoding='utf-8-sig') as f:
#         reader = csv.reader(f)
#         i = 0
#         for row in reader:
#             i += 1
#             usd = Kosdaq.objects.get_or_create(
#                 date = row[0],
#                 lastvalue = row[1],
#                 difference = row[2],
#                 startvalue = row[3],
#                 highvalue = row[4],
#                 lowvalue = row[5],
#                 volume = row[6],
#                 tranaction = row[7],
#                 marketcap = row[8]
#             )
#             print(i,'th done : ', row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

def read_db():  
    value = ExRateJPYKRW.objects.all()
    print(value)
    
if __name__ == '__main__':  
    csv_input()

