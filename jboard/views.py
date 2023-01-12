from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,CrudOil,GoldGlobal,GoldKorea
from jboard.forms import ExRDateForm
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# test
def index(request):
    return HttpResponse('Hello!!')

# template views
class HomeView(TemplateView):
    template_name = 'jboard/home.html'


class DailyView(TemplateView):
    template_name = 'jboard/daily.html'
    
    def get_context_data(self, **kwargs):
        
        qsUSDKRW = ExRateUSDKRW.objects.all().values()
        qsUSDKRW2 = ExRateUSDKRW.objects.all()
        dfUSDKRW = pd.DataFrame(qsUSDKRW)
        print(qsUSDKRW)
        print('--------------------------')
        print(qsUSDKRW2)
        print('--------------------------')
        print(dfUSDKRW['date'])
        print(dfUSDKRW['lastvalue'])
        print('--------------------------')

        qsJPYKRW = ExRateJPYKRW.objects.all().values()
        dfJPYKRW = pd.DataFrame(qsJPYKRW)

        # start = self.request.GET.get('start')
        # end = self.request.GET.get('end')
        # if start:
        #     qsUSDKRW = qsUSDKRW.filter(date__gte=start)
        # if end:
        #     qsUSDKRW = qsUSDKRW.filter(date__lte=end)
        
        # start = self.request.GET.get('start')
        # end = self.request.GET.get('end')
        # if start:
        #     qsJPYKRW = qsJPYKRW.filter(date__gte=start)
        # if end:
        #     qsJPYKRW = qsJPYKRW.filter(date__lte=end)

    
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=("원달러 환율","원엔 환율")
        )

        fig.add_trace(
            go.Scatter(
                x=dfUSDKRW['date'],y=dfUSDKRW['lastvalue'],
                mode='lines',
                line=dict(color='royalblue',width=1),
            ),row=1, col=1
        )
        # fig.add_trace(
        #     go.Scatter(
        #         # x=qsUSDKRW['date'],
        #         # y=qsUSDKRW['lastvalue'],
        #         x=[r['date'] for r in qsUSDKRW],
        #         y=[r['lastvalue'] for r in qsUSDKRW],
        #         name='원-달러',
        #         line=dict(color='royalblue',width=1),
        #         # labels={'x':'일자','y':'환율'}
        #     ),row=1, col=1
        # )

        fig.add_trace(
            go.Scatter(
                x=[r['date'] for r in qsJPYKRW],
                y=[r['lastvalue'] for r in qsJPYKRW],
                name='원-엔',
                line=dict(color='firebrick',width=1),
                # labels={'x':'일자','y':'환율'}
            ),row=1, col=2
        )

        fig.update_xaxes(
            minor=dict(ticks="inside", showgrid=True),
            tickformat="%m\n%Y")

        fig.update_layout(
            height=500, width=1200,
            title_text="환율",
            )

        ExRateChart = fig.to_html()

        context = super(DailyView, self).get_context_data(**kwargs)
        
        context['ExRateChart']=ExRateChart
        
        context['ExRForm']= ExRDateForm()
        # print(context)

        return context


class MacroView(TemplateView):
    template_name = 'jboard/macro.html'

class datainput(TemplateView):
    template_name = 'jboard/datainput.html'


class PortfolioView(TemplateView):
    template_name = 'jboard/portfolio.html'





    # def get_context_data(self, **kwargs):
    #     qs = ExRateUSDKRW.objects.all()
    #     start = self.request.GET.get('start')
    #     end = self.request.GET.get('end')
    #     if start:
    #         qs = qs.filter(date__gte=start)
    #     if end:
    #         qs = qs.filter(date__lte=end)

    #     figUSDKRW = px.line(
    #         x=[r.date for r in qs],
    #         y=[r.lastvalue for r in qs],
    #         title='원달러 환율',
    #         labels={'x':'일자','y':'환율'},
    #         width=600, height=600
    #     )
    #     figUSDKRW.update_layout(title={
    #         'font_size':22,
    #         'xanchor':'center',
    #         'x':0.5
    #     })
    #     figUSDKRW.update_xaxes(
    #         #dtick="M1",
    #         minor=dict(ticks="inside", showgrid=True),
    #         tickformat="%m\n%Y")

    #     ExRateUSDKRWChart = figUSDKRW.to_html()
    #     context = super(DailyView, self).get_context_data(**kwargs)
    #     context['ExRateUSDKRW']=ExRateUSDKRW.objects.all()
    #     context['USDKRWchart']=ExRateUSDKRWChart
    
    #     qs = ExRateJPYKRW.objects.all()
    #     start = self.request.GET.get('start')
    #     end = self.request.GET.get('end')
    #     if start:
    #         qs = qs.filter(date__gte=start)
    #     if end:
    #         qs = qs.filter(date__lte=end)

    #     figJPYKRW = px.line(
    #         x=[r.date for r in qs],
    #         y=[r.lastvalue for r in qs],
    #         title='원엔 환율',
    #         labels={'x':'일자','y':'환율'},
    #         width=600, height=600            
    #     )
    #     figJPYKRW.update_layout(title={
    #         'font_size':22,
    #         'xanchor':'center',
    #         'x':0.5
    #     })
    #     figJPYKRW.update_xaxes(
    #         #dtick="M1",
    #         minor=dict(ticks="inside", showgrid=True),
    #         tickformat="%m\n%Y")

    #     ExRateJPYKRWchart = figJPYKRW.to_html()
    #     # context = super(DailyView, self).get_context_data(**kwargs)
    #     context['ExRateJPYKRW']=ExRateJPYKRW.objects.all()
    #     context['JPYKRWchart']=ExRateJPYKRWchart
    #     print(context)
    #     return context