from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
#from jboard.models import 
from django.http import HttpResponse

# Create your views here.



def index(request):
    return HttpResponse('Hello!!')


class HomeView(TemplateView):
    template_name = 'jboard/home.html'


class DailyView(TemplateView):
    template_name = 'jboard/daily.html'


class MacroView(TemplateView):
    template_name = 'jboard/macro.html'


class PortfolioView(TemplateView):
    template_name = 'jboard/portfolio.html'


