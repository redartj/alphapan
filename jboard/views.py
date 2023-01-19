from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse, reverse_lazy
from jboard.models import Kospi,Kosdaq,ExRateUSDKRW,ExRateJPYKRW,ExRateEURKRW,ExRateCNYKRW,CrudOil,GoldGlobal,GoldKorea,\
                        PFKstocks,PFBonds
from jboard.forms import ExRDateForm,MktDateForm
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
    def get_context_data(self,*args, **kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        
        context['kospi'] = Kospi.objects.latest('date')
        context['kosdaq'] = Kosdaq.objects.latest('date')
        context['usdkrw'] = ExRateUSDKRW.objects.latest('date')
        context['jpykrw'] = ExRateJPYKRW.objects.latest('date')
        context['eurkrw'] = ExRateEURKRW.objects.latest('date')
        context['cnykrw'] = ExRateCNYKRW.objects.latest('date')
        context['crud'] = CrudOil.objects.latest('date')
        context['gldglobal'] = GoldGlobal.objects.latest('date')
        context['gldkor'] = GoldKorea.objects.latest('date')
        
        return context

class DailyView(TemplateView):
    template_name = 'jboard/daily.html'
    
### chart drawing
    def get_context_data(self, **kwargs):
        context = super(DailyView, self).get_context_data(**kwargs)

## Exchage rate

        # 초기날짜 자동세팅 필요. 최근 3년
        # 테이블별 날짜 변경 가능하게.
        
        whatchart = self.request.GET.get('chart')
        start = self.request.GET.get('start')
        end = self.request.GET.get('end')
        print(f"{whatchart},{start},{end}")
        
        qsUSDKRW = ExRateUSDKRW.objects.filter(date__gte="2018-01-01").all().values()
        qsJPYKRW = ExRateJPYKRW.objects.filter(date__gte="2018-01-01").all().values()
        qsEURKRW = ExRateEURKRW.objects.filter(date__gte="2018-01-01").all().values()
        qsCNYKRW = ExRateCNYKRW.objects.filter(date__gte="2018-01-01").all().values()
        
        if whatchart:
            match whatchart:
                case 'USDKRW':
                    if start or end:
                        if start:
                            qsUSDKRW = ExRateUSDKRW.objects.filter(date__gte=start).all().values()
                        if end:
                            qsUSDKRW = qsUSDKRW.filter(date__lte=end).all().values()
                            qsJPYKRW = ExRateJPYKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsEURKRW = ExRateEURKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsCNYKRW = ExRateCNYKRW.objects.filter(date__gte="2018-01-01").all().values()

                case 'JPYKRW':
                        if start:
                            qsJPYKRW = ExRateJPYKRW.objects.filter(date__gte=start).all().values()
                        if end:
                            qsJPYKRW = qsJPYKRW.filter(date__lte=end).all().values()
                            qsUSDKRW = ExRateUSDKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsEURKRW = ExRateEURKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsCNYKRW = ExRateCNYKRW.objects.filter(date__gte="2018-01-01").all().values()

                case 'EURKRW':
                        if start:
                            qsEURKRW = ExRateEURKRW.objects.filter(date__gte=start).all().values()
                        if end:
                            qsEURKRW = qsEURKRW.filter(date__lte=end).all().values()
                            qsUSDKRW = ExRateUSDKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsJPYKRW = ExRateJPYKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsCNYKRW = ExRateCNYKRW.objects.filter(date__gte="2018-01-01").all().values()

                case 'CNYKRW':
                        if start:
                            qsCNYKRW = ExRateCNYKRW.objects.filter(date__gte=start).all().values()
                        if end:
                            qsCNYKRW = qsCNYKRW.filter(date__lte=end).all().values()
                            qsUSDKRW = ExRateUSDKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsJPYKRW = ExRateJPYKRW.objects.filter(date__gte="2018-01-01").all().values()
                            qsEURKRW = ExRateEURKRW.objects.filter(date__gte="2018-01-01").all().values()

        dfUSDKRW = pd.DataFrame(qsUSDKRW)
        dfUSDKRW['date'] = pd.to_datetime(dfUSDKRW['date'])
        dfUSDKRW.set_index('date',inplace=True)

        dfJPYKRW = pd.DataFrame(qsJPYKRW)
        dfJPYKRW['date'] = pd.to_datetime(dfJPYKRW['date'])
        dfJPYKRW.set_index('date',inplace=True)

        dfEURKRW = pd.DataFrame(qsEURKRW)
        dfEURKRW['date'] = pd.to_datetime(dfEURKRW['date'])
        dfEURKRW.set_index('date',inplace=True)

        dfCNYKRW = pd.DataFrame(qsCNYKRW)
        dfCNYKRW['date'] = pd.to_datetime(dfCNYKRW['date'])
        dfCNYKRW.set_index('date',inplace=True)

        fig = make_subplots(
            rows=2, cols=2,
            start_cell = 'top-left',
            subplot_titles=(["원-달러 환율","원-엔 환율","원-유로 환율","원-위안 환율"]),
        )
        fig.update_layout(
            height=500, width=1200,
            margin=dict(l=20,r=20,t=20,b=20),
            showlegend=False,
            # title_text="환율",title_x=0.5,title_xanchor='auto',
        )
        fig.update_xaxes(
            dict(rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            label='1m',
                            step='month',
                            stepmode='backward'),
                        dict(count=6,
                            label='6m',
                            step='month',
                            stepmode='backward'),
                        dict(count=1,
                            label="YTD",
                            step="year",
                            stepmode="todate"),
                        dict(count=1,
                            label="1y",
                            step="year",
                            stepmode="backward"),
                        dict(step='all')
                    ])
                ),type='date'
            ),
            minor=dict(ticks="inside", showgrid=True),
            tickformat="%m\n%Y"
        )
        fig.add_trace(
            go.Scatter(
                x=dfUSDKRW.index,y=dfUSDKRW['lastvalue'],
                mode='lines',name='원-달러',
                line=dict(color='royalblue',width=1),
            ),row=1, col=1
        )

        fig.add_trace(
            go.Scatter(
                x=dfJPYKRW.index,y=dfJPYKRW['lastvalue'],
                mode='lines',name='원-엔',
                line=dict(color='firebrick',width=1),
            ),row=1, col=2
        )

        fig.add_trace(
            go.Scatter(
                x=dfEURKRW.index,y=dfEURKRW['lastvalue'],
                mode='lines',name='원-유로',
                line=dict(width=1),
            ),row=2, col=1
        )

        fig.add_trace(
            go.Scatter(
                x=dfCNYKRW.index,y=dfCNYKRW['lastvalue'],
                mode='lines',name='원-위안',
                line=dict(width=1),
            ),row=2, col=2
        )
        ExRateChart = fig.to_html()
        context['ExRateChart']=ExRateChart

## Kospi, Kosdaq plot

        whatchart = self.request.GET.get('chart')
        start = self.request.GET.get('start')
        end = self.request.GET.get('end')

        qsKospi = Kospi.objects.filter(date__gte="2018-01-01").all().values()    
        qsKosdaq = Kosdaq.objects.filter(date__gte="2018-01-01").all().values()

        if whatchart:
            match whatchart:
                case 'KOSPI':
                    if start or end:
                        if start:
                            qsKospi = Kospi.objects.filter(date__gte=start).all().values() 
                        if end:
                            qsKospi = qsKospi.filter(date__lte=end).all().values() 
                            qsKosdaq = Kosdaq.objects.filter(date__gte="2018-01-01").all().values()

                case 'KOSDAQ':
                        if start:
                            qsKosdaq = Kosdaq.objects.filter(date__gte=start).all().values()
                        if end:
                            qsKosdaq = qsKosdaq.filter(date__lte=end).all().values()
                            qsKospi = Kospi.objects.filter(date__gte="2018-01-01").all().values()

        # qsKospi = Kospi.objects.all().values()
        dfKospi = pd.DataFrame(qsKospi)
        dfKospi['date'] = pd.to_datetime(dfKospi['date'])
        dfKospi.set_index('date',inplace=True)
        dfKospi.head()

        # qsKosdaq = Kosdaq.objects.all().values()
        dfKosdaq = pd.DataFrame(qsKosdaq)
        dfKosdaq['date'] = pd.to_datetime(dfKosdaq['date'])
        dfKosdaq.set_index('date',inplace=True)
        dfKosdaq.head()

        fig = make_subplots(
            rows=1, cols=2,
            start_cell = 'top-left',
            subplot_titles=(["Kospi 지수","Kosdaq 지수"])
        )

        kospi = go.Candlestick(
                        x=dfKospi.index,
                        open=dfKospi['startvalue'],
                        high=dfKospi['highvalue'],
                        low=dfKospi['lowvalue'],
                        close=dfKospi['lastvalue']
                    )
        fig.add_trace(kospi,row=1,col=1)

        kosdaq = go.Candlestick(
                        x=dfKosdaq.index,
                        open=dfKospi['startvalue'],
                        high=dfKospi['highvalue'],
                        low=dfKospi['lowvalue'],
                        close=dfKospi['lastvalue']
                    )
        fig.add_trace(kosdaq,row=1,col=2)

        fig.update_layout(
            height=300, width=1200,
            showlegend=False,
            margin=dict(l=20,r=20,t=20,b=20),
        )
        fig.update_xaxes(dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            label='1m',
                            step='month',
                            stepmode='backward'),
                        dict(count=6,
                            label='6m',
                            step='month',
                            stepmode='backward'),
                        dict(count=1,
                            label="YTD",
                            step="year",
                            stepmode="todate"),
                        dict(count=1,
                            label="1y",
                            step="year",
                            stepmode="backward"),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(
                    visible=False
                ),
                type='date'
            ),
        )
        fig.update_yaxes(
            autorange=True
        )

        MktChart = fig.to_html()
        context['MktChart']=MktChart

## Crudoil price
        qsOil = CrudOil.objects.all().values()
        dfOil = pd.DataFrame(qsOil)
        dfOil['date']=pd.to_datetime(dfOil['date'])
        dfOil.set_index('date',inplace=True)
        dfOil.sort_index(ascending=True,inplace=True)

        trace = go.Scatter(x=dfOil.index,
                    y=dfOil['lastvalue'],
                    line=dict(color='black',width=1))

        data = [trace]
        layout  = dict(
            height=300, width=1200,
            margin=dict(l=20,r=20,t=20,b=20),
            xaxis = dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            label='1m',
                            step='month',
                            stepmode='backward'),
                        dict(count=6,
                            label='6m',
                            step='month',
                            stepmode='backward'),
                        dict(count=1,
                            label="YTD",
                            step="year",
                            stepmode="todate"),
                        dict(count=1,
                            label="1y",
                            step="year",
                            stepmode="backward"),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(
                    visible=False
                ),
                type='date'
            )
        )

        fig = go.FigureWidget(data=data,layout=layout)

        # def zoom(layout, xrange):
        #     print('yaxis updated')
        #     in_view = dfOil.loc[fig.layout.xaxis.range[0]:fig.layout.xaxis.range[1]]
        #     fig.layout.yaxis.range = [in_view.High.min() - 10, in_view.High.max() + 10]

        # fig.layout.on_change(zoom, 'xaxis.range')

        OilChart = fig.to_html()
        context['OilChart'] = OilChart
        
        context['ExRForm']=ExRDateForm()
        context['MktForm']=MktDateForm()

        return context


class MacroView(TemplateView):
    template_name = 'jboard/macro.html'

class datainput(TemplateView):
    template_name = 'jboard/datainput.html'


def portfolio(request):

    samsung = 61000
    kgb_01125_3909 = 7180

    qsPFKstocks = PFKstocks.objects.all()
    qsPFKbons = PFBonds.objects.all()

    content = {'bond': qsPFKstocks}
    content = {'kstock':qsPFKbons}

    return render(request,'jboard/portfolio.html',content)

class create_pf_stocks(CreateView):
    model = PFKstocks
    fields = '__all__'
    successful_url = reverse_lazy('jboard:portfolio')

class create_pf_bonds(CreateView):
    model = PFBonds
    fields = '__all__'
    successful_url = reverse_lazy('jboard:portfolio')

# class PortfolioView(TemplateView):
#     template_name = 'jboard/portfolio.html'




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



            # candledata = go.Candlestick(
        #             x=dfKospi.index,
        #             open=dfKospi['startvalue'],
        #             high=dfKospi['highvalue'],
        #             low=dfKospi['lowvalue'],
        #             close=dfKospi['lastvalue']
        #             )

        # candlefig = go.Figure(data=candledata)
        # candlefig.update_layout(
        #     height=500, width=1200,
        #     title_text="Kospi지수",
        #     title_x=0.5,
        #     title_xanchor='auto',
        #     xaxis_rangeslider_visible=False
        # )
        # candlefig.update_xaxes(dict(
        #         rangeselector=dict(
        #             buttons=list([
        #                 dict(count=1,
        #                     label='1m',
        #                     step='month',
        #                     stepmode='backward'),
        #                 dict(count=6,
        #                     label='6m',
        #                     step='month',
        #                     stepmode='backward'),
        #                 dict(count=1,
        #                     label="YTD",
        #                     step="year",
        #                     stepmode="todate"),
        #                 dict(count=1,
        #                     label="1y",
        #                     step="year",
        #                     stepmode="backward"),
        #                 dict(step='all')
        #             ])
        #         ),type='date'
        #     ),
        # )
        # print(candlefig)


        