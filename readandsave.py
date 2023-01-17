import os,csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoApp.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,ExRateEURKRW,ExRateCNYKRW,CrudOil,GoldGlobal,GoldKorea
import numpy as np
import pandas as pd

# def csv_input():  
#     with open("./data/kispi.csv", "r", encoding='utf-8-sig') as f:
#         reader = csv.reader(f)
#         i = 0
#         for row in reader:
#             i += 1
#             print(row[0], row[1], row[2])
#             ExRateEURKRW.objects.get_or_create(
#                 date=row[0],
#                 lastvalue=row[1],
#                 difference=row[2]
#                 # startvalue=row[3],
#                 # highvalue=row[4],
#                 # lowvalue=row[5]
#             )
#             print(i,'th done')

def csv_input():  
    with open("./data/Kospi(030101_230105).csv", "r", encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            i += 1
            usd = Kospi.objects.get_or_create(
                date = row[0],
                lastvalue = row[1],
                difference = row[2],
                diffrate = row[3],
                startvalue = row[4],
                highvalue = row[5],
                lowvalue = row[6],
                volume = row[7],
                tranaction = row[8],
                marketcap = row[9]
            )
            print(i,'th done : ', row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

def deleteData():
    deleteData = Kosdaq.objects.all()
    print(deleteData)
    deleteData.delete()
    return

def updateData():
    return

def read_db():  
    value = Kospi.objects.all()
    print(value)
    
if __name__ == '__main__':  
    csv_input()

