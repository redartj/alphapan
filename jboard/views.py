from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,CrudOil,GoldGlobal,GoldKorea
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.express as px


# test
def index(request):
    return HttpResponse('Hello!!')

# template views
class HomeView(TemplateView):
    template_name = 'jboard/home.html'


class DailyView(TemplateView):
    template_name = 'jboard/daily.html'
    def get_context_data(self, **kwargs):
        qs = ExRateUSDKRW.objects.all()
        start = self.request.GET.get('start')
        end = self.request.GET.get('end')
        if start:
            qs = qs.filter(date__gte=start)
        if end:
            qs = qs.filter(date__lte=end)

        fig = px.line(
            x=[r.date for r in qs],
            y=[r.lastvalue for r in qs],
            title='원달러 환율',
            labels={'x':'일자','y':'환율'}
        )
        fig.update_layout(title={
            'font_size':22,
            'xanchor':'center',
            'x':0.5
        })
        fig.update_xaxes(
            #dtick="M1",
            minor=dict(ticks="inside", showgrid=True),
            tickformat="%m\n%Y")

        chart = fig.to_html()
        context = super(DailyView, self).get_context_data(**kwargs)
        context['ExRateUSDKRW']=ExRateUSDKRW.objects.all()
        context['chart']=chart
        return context

class MacroView(TemplateView):
    template_name = 'jboard/macro.html'

class datainput(TemplateView):
    template_name = 'jboard/datainput.html'


class PortfolioView(TemplateView):
    template_name = 'jboard/portfolio.html'


