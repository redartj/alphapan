from django.urls import path
from .views import HomeView,DailyView,MacroView,PortfolioView
from . import views

app_name='jboard'

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('datainput/',views.datainput,name='datainput'),
    path('daily/',views.DailyView.as_view(),name='daily'),
    path('macro/',views.MacroView.as_view(),name='macro'),
    path('portfolio/',views.PortfolioView.as_view(),name='portfolio'),
 
]