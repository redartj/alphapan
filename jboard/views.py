from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,CrudOil,GoldGlobal,GoldKorea
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.express as px


# inputting data
def datainput(request):
    # csv에서 불러오기

    # 값 뽑아서 변수에 넣음


    # 모델에 값 넣기


    return HttpResponse("Done")

# test
def index(request):
    return HttpResponse('Hello!!')

# template views
class HomeView(TemplateView):
    template_name = 'jboard/home.html'


class DailyView(TemplateView):
    template_name = 'jboard/daily.html'


class MacroView(TemplateView):
    template_name = 'jboard/macro.html'


class PortfolioView(TemplateView):
    template_name = 'jboard/portfolio.html'


